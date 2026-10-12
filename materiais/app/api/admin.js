import { list, get, put } from '@vercel/blob';
import { MATERIAIS } from '../lib/materiais.js';
import { isAdmin } from '../lib/auth.js';

const COLS = ['criadoEm', 'material', 'temperatura', 'pontos', 'nome', 'email', 'whatsapp', 'instagram', 'profissao', 'seguidores', 'lancou', 'quando', 'desafio', 'origem'];
const csvCell = (v) => { const s = String(v ?? ''); return /[",\n;]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s; };

async function readBody(req) { const chunks = []; for await (const c of req) chunks.push(c); return Buffer.concat(chunks); }

async function allLeads() {
  const out = []; let cursor;
  do {
    const r = await list({ prefix: 'leads/', cursor, limit: 1000 });
    for (const b of r.blobs) {
      const g = await get(b.pathname, { access: 'private' });
      if (g?.statusCode === 200) out.push(JSON.parse(await new Response(g.stream).text()));
    }
    cursor = r.hasMore ? r.cursor : undefined;
  } while (cursor);
  return out.sort((a, b) => b.criadoEm.localeCompare(a.criadoEm));
}

export default async function handler(req, res) {
  if (!isAdmin(req)) return res.status(401).json({ erro: 'Senha inválida' });
  const action = req.query.action || 'leads';
  if (req.method === 'POST' && action === 'upload') {
    const m = req.query.m;
    if (!MATERIAIS[m]) return res.status(400).json({ erro: 'Material inválido' });
    const buf = await readBody(req);
    if (buf.slice(0, 4).toString() !== '%PDF') return res.status(400).json({ erro: 'Arquivo não é PDF' });
    await put(`pdfs/${m}.pdf`, buf, { access: 'private', contentType: 'application/pdf', addRandomSuffix: false, allowOverwrite: true });
    return res.json({ ok: true, material: m, bytes: buf.length });
  }
  if (action === 'pdfs') {
    const r = await list({ prefix: 'pdfs/' });
    return res.json(Object.keys(MATERIAIS).map((m) => {
      const b = r.blobs.find((x) => x.pathname === `pdfs/${m}.pdf`);
      return { material: m, titulo: MATERIAIS[m], enviado: !!b, tamanho: b?.size || 0, atualizadoEm: b?.uploadedAt || null };
    }));
  }
  const leads = await allLeads();
  const m = req.query.m;
  const rows = m ? leads.filter((l) => l.material === m) : leads;
  if (req.query.format === 'csv') {
    res.setHeader('Content-Type', 'text/csv; charset=utf-8');
    res.setHeader('Content-Disposition', `attachment; filename="leads-${m || 'todos'}-${new Date().toISOString().slice(0, 10)}.csv"`);
    return res.send('﻿' + [COLS.join(';'), ...rows.map((l) => COLS.map((c) => csvCell(l[c])).join(';'))].join('\n'));
  }
  return res.json({ total: rows.length, leads: rows });
}
