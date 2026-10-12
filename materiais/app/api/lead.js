import crypto from 'node:crypto';
import { put } from '@vercel/blob';
import { MATERIAIS, GRUPO_URL } from '../lib/materiais.js';
import { sign } from '../lib/auth.js';

const clean = (v, n = 200) => String(v ?? '').replace(/[\u0000-\u001f]/g, ' ').trim().slice(0, n);

function score(d) {
  let s = 0;
  s += { '0-5k': 0, '5-20k': 1, '20-100k': 3, '100k+': 3 }[d.seguidores] ?? 0;
  s += { nunca: 1, 'sim-ate-10k': 2, 'sim-10-100k': 3, 'sim-100k+': 3 }[d.lancou] ?? 0;
  s += { '30dias': 3, '90dias': 2, 'sem-data': 0 }[d.quando] ?? 0;
  return { pontos: s, temperatura: s >= 7 ? 'quente' : s >= 4 ? 'morno' : 'frio' };
}

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ erro: 'Método não permitido' });
  const b = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
  if (b.site) return res.status(200).json({ ok: true });
  const material = clean(b.material, 30);
  if (!MATERIAIS[material]) return res.status(400).json({ erro: 'Material inválido' });
  const d = {
    nome: clean(b.nome, 120), email: clean(b.email, 160).toLowerCase(), whatsapp: clean(b.whatsapp, 30),
    instagram: clean(b.instagram, 60).replace(/^@?/, '@'), profissao: clean(b.profissao, 120),
    seguidores: clean(b.seguidores, 20), lancou: clean(b.lancou, 20), quando: clean(b.quando, 20),
    desafio: clean(b.desafio, 600),
  };
  if (!d.nome || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email) || d.whatsapp.replace(/\D/g, '').length < 10 || !b.consentimento)
    return res.status(400).json({ erro: 'Preencha nome, e-mail, WhatsApp e aceite o contato.' });
  const id = crypto.randomUUID();
  const criadoEm = new Date().toISOString();
  const lead = { id, criadoEm, material, ...d, ...score(d), origem: clean(b.origem, 60) || 'instagram', utm: clean(b.utm, 200) };
  await put(`leads/${criadoEm.slice(0, 10)}/${criadoEm}-${id}.json`, JSON.stringify(lead), {
    access: 'private', contentType: 'application/json', addRandomSuffix: false,
  });
  return res.status(200).json({ ok: true, download: `/api/material?m=${material}&id=${id}&t=${sign(material + ':' + id)}`, grupo: GRUPO_URL });
}
