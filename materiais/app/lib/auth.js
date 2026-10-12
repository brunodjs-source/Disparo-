import crypto from 'node:crypto';
const secret = () => process.env.TOKEN_SECRET || 'dev';
export const sign = (s) => crypto.createHmac('sha256', secret()).update(s).digest('base64url').slice(0, 32);
export const verify = (s, t) => { const a = Buffer.from(sign(s)); const b = Buffer.from(String(t || '')); return a.length === b.length && crypto.timingSafeEqual(a, b); };
export function isAdmin(req) {
  const h = req.headers.authorization || '';
  const pass = h.startsWith('Bearer ') ? h.slice(7) : (req.query?.k || '');
  const want = process.env.ADMIN_PASSWORD || '';
  if (!want || !pass) return false;
  const a = Buffer.from(pass), b = Buffer.from(want);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}
