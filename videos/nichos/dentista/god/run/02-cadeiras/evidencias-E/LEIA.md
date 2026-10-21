# Evidências da cadeira E (Primeiros princípios) · 21/10/2026

Somente leitura de raw.wav, voz_master.wav e rn_*.wav (scratchpad/dent). Nada instalado: faster-whisper small e arnndn já estavam no scratchpad; scipy existe no cbenv.

- trecho_whisper.py / .log: retranscrição do trecho 24,5 a 29,6 s (B02).
- inteligibilidade.py / .log: confiança do whisper no arquivo inteiro das 5 versões existentes.
- piso_percentil.py / .log: distância fala-piso por percentil (janelas de 50 ms), sem depender do alinhamento.
- leve_teste.py, joelho_teste.py, gate_teste_E.py / .log: curva inteligibilidade x piso (arnndn sh mix 0,6 a 1,0; afftdn 12 dB; gate).
- cadeia_E.sh: cadeia proposta. Saída medida: E_voz_final.wav e E_voz_final.m4a (cadeia_E_medida.log).
- dr02_compara.py / .log: método DR02 do livro de fatos aplicado ao voz_master e ao E_voz_final.
- E_sh_mix08.wav: etapa intermediária (arnndn sh, mix 0,8). Os outros intermediários foram apagados; os scripts os recriam.

Ressalva: confiança de ASR é proxy de inteligibilidade, não ouvido humano. Nada aqui substitui a escuta do Bruno.
