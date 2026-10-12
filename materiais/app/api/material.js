import { get } from '@vercel/blob';
import { Readable } from 'node:stream';
import { MATERIAIS } from '../lib/materiais.js';
import { verify, isAdmin } from '../lib/auth.js';

export default async function handler(req, res) {
  const { m, id, t } = req.query;
  if (!MATERIAIS[m]) return res.status(404).send('Material não encontrado');
  if (!isAdmin(req) && !verify(`${m}:${id}`, t)) return res.status(403).send('Preencha o formulário pra baixar o material.');
  const r = await get(`pdfs/${m}.pdf`, { access: 'private' });
  if (!r || r.statusCode !== 200) return res.status(404).send('Material ainda não disponível.');
  res.setHeader('Content-Type', 'application/pdf');
  res.setHeader('Content-Disposition', `attachment; filename="estrategista-${m}.pdf"`);
  res.setHeader('Cache-Control', 'private, no-store');
  Readable.fromWeb(r.stream).pipe(res);
}
