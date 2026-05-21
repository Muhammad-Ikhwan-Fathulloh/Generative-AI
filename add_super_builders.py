import os
import re

files = [
    r'd:\Generative-AI\AI_for_Teacher\Session1_HandsOn.html',
    r'd:\Generative-AI\AI_for_Teacher\Session2_HandsOn.html',
    r'd:\Generative-AI\AI_for_Teacher\Session3_HandsOn.html',
    r'd:\Generative-AI\AI_for_Teacher\Session4_HandsOn.html'
]

master_ui = '''
        <!-- MASTER PROMPT -->
        <div style="background: #1e293b; color: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid #334155; width: 100%; margin-top: 30px;">
            <h3 style="margin-bottom: 15px; color: #38bdf8;"><i class="fas fa-layer-group"></i> Instruksi Terpadu (Super Prompt)</h3>
            <p style="font-size: 1rem; color: #94a3b8; margin-bottom: 15px;">Kumpulan instruksi dari alat bantu di atas akan digabungkan di sini menjadi satu *prompt* yang sangat kuat (powerful).</p>
            <textarea id="master-res" rows="6" placeholder="Hasil instruksi gabungan akan muncul di sini..." style="width:100%; padding:15px; border-radius:12px; border:2px solid #38bdf8; font-size:1.1rem; font-family:monospace; background: #0f172a; color: #f8fafc;"></textarea>
            <div style="margin-top:15px; display: flex; gap: 10px;">
                <button onclick="copyMaster('master-res')" style="padding:12px 25px; background:#38bdf8; color:#0f172a; border:none; border-radius:8px; cursor:pointer; font-weight:700; flex-grow:1;"><i class="fas fa-copy"></i> Salin Super Prompt</button>
                <button onclick="clearMaster()" style="padding:12px 25px; background:#ef4444; color:white; border:none; border-radius:8px; cursor:pointer; font-weight:700;"><i class="fas fa-trash"></i> Bersihkan</button>
            </div>
        </div>
        <script>
            function appendToMaster(text) {
                const master = document.getElementById("master-res");
                if(master.value.trim() !== '') {
                    master.value += '\\n\\n' + text;
                } else {
                    master.value = text;
                }
            }
            function clearMaster() {
                document.getElementById("master-res").value = '';
            }
            function copyMaster(id) {
                const ta = document.getElementById(id);
                if (!ta.value) return alert('Prompt masih kosong!');
                ta.select();
                document.execCommand('copy');
                alert('Super Prompt berhasil disalin!');
            }
        </script>
    </div>
'''

html_sesi1 = '''
    <!-- ALAT BANTU SESI 1 -->
    <div id="tools-sesi1" class="slide">
        <div class="case-badge case-both">🛠️ ALAT BANTU (MULTIPART)</div>
        <h2>Koleksi Alat Bantu Sesi 1</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Setiap komponen alat bantu di bawah ini dapat digabungkan (dikombinasikan) untuk menghasilkan satu instruksi yang sangat kuat (Super Prompt).</p>
        
        <!-- Tool 1: RTC -->
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%; margin-bottom: 20px;">
            <h3 style="margin-bottom: 15px; color: var(--primary);">1. Alat Pembuat Instruksi Dasar (Konsep R-T-C)</h3>
            <div style="margin-bottom: 15px;">
                <label style="display:block; font-weight:600; margin-bottom: 5px;">Peran (Role) AI</label>
                <input type="text" id="t1-role" placeholder="Cth: Guru Matematika" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
            </div>
            <div style="margin-bottom: 15px;">
                <label style="display:block; font-weight:600; margin-bottom: 5px;">Tugas (Task)</label>
                <input type="text" id="t1-task" placeholder="Cth: Buatkan 5 soal cerita" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
            </div>
            <div style="margin-bottom: 15px;">
                <label style="display:block; font-weight:600; margin-bottom: 5px;">Konteks (Context)</label>
                <textarea id="t1-context" rows="2" placeholder="Cth: Untuk siswa SD kelas 4 Topik Pecahan" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1;"></textarea>
            </div>
            <button onclick="genT1()" class="btn-nav" style="margin-top:0; padding:10px 20px; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan ke Super Prompt</button>
        </div>

        <!-- Tool 2: Evaluator -->
        <div style="background: #fffbeb; padding: 30px; border-radius: 16px; border: 1px solid #fde68a; width: 100%;">
            <h3 style="margin-bottom: 15px; color: #d97706;">2. Alat Evaluator Ide (Kritik AI)</h3>
            <div style="margin-bottom: 15px;">
                <label style="display:block; font-weight:600; margin-bottom: 5px;">Ide yang dievaluasi / dianalisis</label>
                <input type="text" id="t1b-idea" placeholder="Cth: Menggunakan game Minecraft untuk belajar Sejarah..." style="width:100%; padding:10px; border-radius:8px; border:1px solid #fcd34d;">
            </div>
            <button onclick="genT1b()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#f59e0b; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan ke Super Prompt</button>
        </div>
        
        <script>
            function genT1() {
                const r=document.getElementById("t1-role").value, t=document.getElementById("t1-task").value, c=document.getElementById("t1-context").value;
                appendToMaster(`Bertindaklah sebagai ${r||'seorang ahli'}. Tugas Utama Anda: ${t||'bantu menyelesaikan masalah saya'}. Konteks tambahan untuk diperhatikan: ${c||'-'}`);
            }
            function genT1b() {
                const idea=document.getElementById("t1b-idea").value;
                appendToMaster(`Selain itu, tolong evaluasi ide pembelajaran berikut secara kritis: "${idea}". Berikan 3 potensi kelemahan dan cara memperbaikinya agar lebih efektif.`);
            }
        </script>
''' + master_ui

html_sesi2 = '''
    <!-- ALAT BANTU SESI 2 -->
    <div id="tools-sesi2" class="slide">
        <div class="case-badge case-both">🛠️ ALAT BANTU (MULTIPART)</div>
        <h2>Koleksi Alat Bantu Sesi 2</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Kombinasikan metode CREATE dengan instruksi struktural tahap demi tahap (CoT) untuk menghasilkan sebuah *Prompt* yang menyeluruh dan aman dari kegagalan logika.</p>
        
        <!-- Tool 1: CREATE -->
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%; margin-bottom: 20px;">
            <h3 style="margin-bottom: 15px; color: var(--primary);">1. Kerangka Dasar Lanjutan (CREATE)</h3>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:15px; margin-bottom:15px;">
                <input type="text" id="t2-c" placeholder="C: Character (Karakter Ahli)" style="padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
                <input type="text" id="t2-r" placeholder="R: Request (Permintaan Utama)" style="padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
            </div>
            <textarea id="t2-e" rows="2" placeholder="E: Explanation (Penjelasan Latar Belakang Lengkap)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;"></textarea>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:15px; margin-bottom:15px;">
                <input type="text" id="t2-a" placeholder="A: Adjustments (Gaya/Nada Bahasa)" style="padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
                <input type="text" id="t2-t" placeholder="T: Type (Tipe/Format Keluaran)" style="padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
            </div>
            <input type="text" id="t2-ex" placeholder="E: Extras (Batasan Tambahan/Larangan/Syarat Khusus)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;">
            <button onclick="genT2a()" class="btn-nav" style="margin-top:0; padding:10px 20px; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan ke Super Prompt</button>
        </div>

        <!-- Tool 2: Chain of Thought -->
        <div style="background: #eff6ff; padding: 30px; border-radius: 16px; border: 1px solid #bfdbfe; width: 100%; margin-bottom: 20px;">
            <h3 style="margin-bottom: 15px; color: #3b82f6;">2. Pendukung Pemecahan Masalah Sistematis (CoT)</h3>
            <textarea id="t2b-prob" rows="2" placeholder="Detail tantangan yang harus diurai (Opsional jika sudah ada di CREATE)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #93c5fd; margin-bottom:15px;"></textarea>
            <button onclick="genT2b()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#3b82f6; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan Logika CoT</button>
        </div>
        
        <!-- Tool 3: Few Shot -->
        <div style="background: #fdf4ff; padding: 30px; border-radius: 16px; border: 1px solid #f5d0fe; width: 100%;">
            <h3 style="margin-bottom: 15px; color: #d946ef;">3. Pendukung Analogi (Few-Shot)</h3>
            <input type="text" id="t2c-ex1" placeholder="Contoh Pemicu & Respon (Cth: Input: Sedih -> Output: Biasa Saja)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #e879f9; margin-bottom:10px;">
            <input type="text" id="t2c-target" placeholder="Target Akhir (Cth: Sekarang kerjakan untuk -> Marah)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #e879f9; margin-bottom:15px;">
            <button onclick="genT2c()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#d946ef; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan Contoh Pola</button>
        </div>
        
        <script>
            function genT2a() {
                const c=document.getElementById("t2-c").value, r=document.getElementById("t2-r").value;
                const e=document.getElementById("t2-e").value, a=document.getElementById("t2-a").value;
                const t=document.getElementById("t2-t").value, ex=document.getElementById("t2-ex").value;
                let text = `Peran Anda: ${c}\\nTujuan Utama: ${r}\\nLatar Belakang: ${e}\\nGaya Bahasa: ${a}\\nFormat Hasil: ${t}\\nAturan Tambahan: ${ex}`;
                appendToMaster(text);
            }
            function genT2b() {
                const prob = document.getElementById("t2b-prob").value;
                let text = "Mari pikirkan langkah demi langkah (berpikir sistematis tahap demi tahap) untuk membangun solusi yang akurat dan solid.";
                if(prob) text += ` Khususnya dalam menghadapi tantangan berikut: "${prob}".`;
                appendToMaster(text);
            }
            function genT2c() {
                appendToMaster(`Gunakan logika dan pola penulisan seperti contoh berikut ini:\\nContoh: ${document.getElementById("t2c-ex1").value}\\n\\nSekarang terapkan pola tersebut untuk target ini: ${document.getElementById("t2c-target").value}`);
            }
        </script>
''' + master_ui

html_sesi3 = '''
    <!-- ALAT BANTU SESI 3 -->
    <div id="tools-sesi3" class="slide" style="margin-bottom: 20px;">
        <div class="case-badge case-both">🛠️ ALAT BANTU (MULTIPART)</div>
        <h2>Koleksi Alat Bantu Riset (NotebookLM)</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Terkadang Anda butuh rangkuman, sekaligus soal evaluasi, dan pencarian kesenjangan dari sumber yang sama. Gabungkan semuanya di sini!</p>
        
        <!-- Tool 1: Panduan Belajar -->
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%; margin-bottom: 20px;">
            <h3 style="margin-bottom: 15px; color: var(--primary);">1. Komponen Panduan Belajar & Ringkasan</h3>
            <input type="text" id="t3-topic" placeholder="Fokus Utama (Cth: Keseluruhan tentang Perang Dunia II)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;">
            <button onclick="genT3a()" class="btn-nav" style="margin-top:0; padding:10px 20px; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan ke Super Prompt</button>
        </div>

        <!-- Tool 2: Soal HOTS -->
        <div style="background: #fffbeb; padding: 30px; border-radius: 16px; border: 1px solid #fde68a; width: 100%; margin-bottom: 20px;">
            <h3 style="margin-bottom: 15px; color: #d97706;">2. Pendukung Pembuatan Evaluasi Khusus</h3>
            <select id="t3-level" style="width:100%; padding:10px; border-radius:8px; border:1px solid #fcd34d; margin-bottom:15px;">
                <option value="C4 (Analisis)">Soal Evaluasi C4 (Kemampuan Analisis Informasi Tambahan)</option>
                <option value="C5 (Evaluasi)">Soal Evaluasi C5 (Kemampuan Evaluasi/Kritik Data)</option>
                <option value="C6 (Mencipta)">Soal Evaluasi C6 (Sintesis Opini Baru Berbasis Bukti)</option>
            </select>
            <button onclick="genT3b()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#f59e0b; font-size:1rem;"><i class="fas fa-plus"></i> Sertakan Pembuatan Soal</button>
        </div>

        <!-- Tool 3: Gap Analysis -->
        <div style="background: #eff6ff; padding: 30px; border-radius: 16px; border: 1px solid #bfdbfe; width: 100%;">
            <h3 style="margin-bottom: 15px; color: #3b82f6;">3. Pendukung Riset Literatur Lanjut</h3>
            <input type="text" id="t3-gap" placeholder="Area Jurnal/Materi yang ingin dikupas tuntas" style="width:100%; padding:10px; border-radius:8px; border:1px solid #93c5fd; margin-bottom:15px;">
            <button onclick="genT3c()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#3b82f6; font-size:1rem;"><i class="fas fa-plus"></i> Sertakan Evaluasi Metodologi/Gap</button>
        </div>
        
        <script>
            function genT3a() {
                const t=document.getElementById("t3-topic").value;
                appendToMaster(`Berdasarkan informasi konklusif dari seluruh dokumen yang difilter, buatkan ringkasan inti yang mudah dipahami tentang: ${t}. Fokus pada penyajian data pokok.`);
            }
            function genT3b() {
                const l=document.getElementById("t3-level").value;
                appendToMaster(`Selain pemaparan ringkasan, saya juga meminta Anda merumuskan 5 skenario studi kasus (soal level ${l}) beserta kunci rujukan kutipannya untuk menguji pendalaman konsep tersebut.`);
            }
            function genT3c() {
                const t=document.getElementById("t3-gap").value;
                appendToMaster(`Penting: Berikan analisis komparatif antar literatur terkait ${t}, temukan kontradiksi atau kesenjangan (gap) informasi yang masih memerlukan kajian lanjutan. Berikan selalu kutipan klik untuk klaim Anda.`);
            }
        </script>
''' + master_ui

html_sesi4 = '''
    <!-- ALAT BANTU SESI 4 -->
    <div id="tools-sesi4" class="slide" style="margin-bottom: 20px;">
        <div class="case-badge case-both">🛠️ ALAT BANTU (MULTIPART)</div>
        <h2>Koleksi Alat Perangkai Aplikasi (Opal)</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Setiap aplikasi mini memerlukan Masukan, Proses, dan Logika percabangan. Gabungkan deskripsi dari ketiga komponen ini agar ruang aplikasi terbentuk sempurna dengan sekali *Prompt*!</p>
        
        <!-- Tool 1: Input -->
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%; margin-bottom: 20px;">
            <h3 style="margin-bottom: 15px; color: var(--primary);">1. Deskripsi Jalur Masukan (Input)</h3>
            <input type="text" id="t4-in" placeholder="Informasi/file apa yang akan selalu dimasukkan calon pengguna Anda?" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;">
            <button onclick="genT4a()" class="btn-nav" style="margin-top:0; padding:10px 20px; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan ke Deskripsi App</button>
        </div>

        <!-- Tool 2: Generate Process -->
        <div style="background: #fffbeb; padding: 30px; border-radius: 16px; border: 1px solid #fde68a; width: 100%; margin-bottom: 20px;">
            <h3 style="margin-bottom: 15px; color: #d97706;">2. Deskripsi Otak Utama (Generate)</h3>
            <textarea id="t4-proc" rows="2" placeholder="Bagaimana AI akan mengolah masukan tersebut dan format keluaran seperti apa yang dihasilkan?" style="width:100%; padding:10px; border-radius:8px; border:1px solid #fcd34d; margin-bottom:15px;"></textarea>
            <button onclick="genT4b()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#f59e0b; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan ke Deskripsi App</button>
        </div>

        <!-- Tool 3: Logic -->
        <div style="background: #eff6ff; padding: 30px; border-radius: 16px; border: 1px solid #bfdbfe; width: 100%;">
            <h3 style="margin-bottom: 15px; color: #3b82f6;">3. Deskripsi Sistem Peninjau (Conditional Logic)</h3>
            <input type="text" id="t4-cond" placeholder="Syarat ekstra sebelum pengguna menerima output (Cth: Harus disetujui Guru terlebih dahulu)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #93c5fd; margin-bottom:15px;">
            <button onclick="genT4c()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#3b82f6; font-size:1rem;"><i class="fas fa-plus"></i> Tambahkan ke Deskripsi App</button>
        </div>
        
        <script>
            function genT4a() { appendToMaster(`Aplikasi ini ditujukan untuk memfasilitasi data berikut:\\n- Masukan Pengguna: ${document.getElementById("t4-in").value}`); }
            function genT4b() { appendToMaster(`Tahapan Pemrosesan AI Utama:\\n- Saat input diterima, proses AI akan melakukan: ${document.getElementById("t4-proc").value}`); }
            function genT4c() { appendToMaster(`Alur Validasi Tambahan:\\n- Proses ini akan diberhentikan/mendapat percabangan baru jika: ${document.getElementById("t4-cond").value}`); }
        </script>
''' + master_ui


d = {
    'd:\\Generative-AI\\AI_for_Teacher\\Session1_HandsOn.html': html_sesi1,
    'd:\\Generative-AI\\AI_for_Teacher\\Session2_HandsOn.html': html_sesi2,
    'd:\\Generative-AI\\AI_for_Teacher\\Session3_HandsOn.html': html_sesi3,
    'd:\\Generative-AI\\AI_for_Teacher\\Session4_HandsOn.html': html_sesi4,
}

for filepath, insertion_code in d.items():
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Need to remove the PREVIOUS tool builders I just injected.
    # The previous injection was `<!-- ALAT BANTU SESI X -->` to the end of the `</div>` before the `<div class="slide"` that closed it.
    # Actually, my previous script injected:
    # `<!-- ALAT BANTU SESI X --> ... </div>\n    <div class="slide"`
    
    # We can use regex to strip `<div id="tools-sesiX".*?</div>` ? Wait, there is a master <div class="slide"> that contains everything, and it ends with `</script> \n </div>`.
    # Let's cleanly remove it:
    content = re.sub(r'<!-- ALAT BANTU SESI \d+ -->.*?</div>\s*<div class="slide"', '<div class="slide"', content, flags=re.DOTALL)
    # Also if it was inserted before the last </div> or something, let's also remove `<!-- ALAT BANTU SESI \d+ -->` to the end of file (just in case) if `<div class="slide"` doesn't follow.
    content = re.sub(r'<!-- ALAT BANTU SESI \d+ -->.*?(?=</body>|</html>)', '', content, flags=re.DOTALL)
    
    # Wait, the previous script did: 
    # `parts[-1] = insertion_code + '\n    <div class="slide"' + parts[-1]`
    # And then `<div class="slide"`.join(parts)
    # So the insertion code was exactly between slides!
    # And it started with `<!-- ALAT BANTU SESI X -->` and ended with `</div>`.
    # Then `\n    <div class="slide"` came next.
    # By replacing `<!-- ALAT BANTU SESI \d+ -->.*?<div class="slide"` with `<div class="slide"`, we effectively undo it.
    
    # Clean check:
    content = re.sub(r'<!-- ALAT BANTU SESI \d+ -->.*?(?=<div class="slide")', '', content, flags=re.DOTALL)

    parts = content.split('<div class="slide"')
    if len(parts) >= 2:
        parts[-1] = insertion_code + '\n    <div class="slide"' + parts[-1]
        
    content = '<div class="slide"'.join(parts)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")
