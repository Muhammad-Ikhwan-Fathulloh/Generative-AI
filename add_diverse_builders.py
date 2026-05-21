import os
import re

files = [
    r'd:\Generative-AI\AI_for_Teacher\Session1_HandsOn.html',
    r'd:\Generative-AI\AI_for_Teacher\Session2_HandsOn.html',
    r'd:\Generative-AI\AI_for_Teacher\Session3_HandsOn.html',
    r'd:\Generative-AI\AI_for_Teacher\Session4_HandsOn.html'
]

html_sesi1 = '''
    <!-- ALAT BANTU SESI 1 -->
    <div id="tools-sesi1" class="slide">
        <div class="case-badge case-both">🛠️ ALAT BANTU (MULTIPART)</div>
        <h2>Koleksi Alat Bantu Sesi 1</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Berbagai alat bantu berbasis metode dasar untuk mempermudah Anda selama fase Ideasi.</p>
        
        <!-- Tool 1: RTC -->
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%; margin-bottom: 30px;">
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
            <button onclick="genT1()" class="btn-nav" style="margin-top:0; padding:10px 20px; font-size:1rem;"><i class="fas fa-magic"></i> Rangkai</button>
            <textarea id="t1-res" rows="3" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid var(--primary);"></textarea>
        </div>

        <!-- Tool 2: Evaluator -->
        <div style="background: #fffbeb; padding: 30px; border-radius: 16px; border: 1px solid #fde68a; width: 100%;">
            <h3 style="margin-bottom: 15px; color: #d97706;">2. Evaluator Ide (Kritik AI)</h3>
            <div style="margin-bottom: 15px;">
                <label style="display:block; font-weight:600; margin-bottom: 5px;">Ide yang dievaluasi</label>
                <input type="text" id="t1b-idea" placeholder="Cth: Menggunakan game Minecraft untuk belajar Sejarah..." style="width:100%; padding:10px; border-radius:8px; border:1px solid #fcd34d;">
            </div>
            <button onclick="genT1b()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#f59e0b; font-size:1rem;"><i class="fas fa-search"></i> Rangkai Penilaian</button>
            <textarea id="t1b-res" rows="3" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid #f59e0b; background:#fff;"></textarea>
        </div>
        <script>
            function genT1() {
                const r=document.getElementById("t1-role").value, t=document.getElementById("t1-task").value, c=document.getElementById("t1-context").value;
                document.getElementById("t1-res").value = `Bertindaklah sebagai ${r||'Ahli'}. Tugas Anda: ${t||'Bantu saya'}. Konteks: ${c||'-'}`;
            }
            function genT1b() {
                const idea=document.getElementById("t1b-idea").value;
                document.getElementById("t1b-res").value = `Tolong evaluasi ide pembelajaran berikut secara kritis: "${idea}". Berikan 3 potensi kelemahan dan cara memperbaikinya.`;
            }
        </script>
    </div>
'''

html_sesi2 = '''
    <!-- ALAT BANTU SESI 2 -->
    <div id="tools-sesi2" class="slide">
        <div class="case-badge case-both">🛠️ ALAT BANTU (MULTIPART)</div>
        <h2>Koleksi Alat Bantu Sesi 2</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Tiga varian pembuat instruksi (CREATE, CoT, Few-Shot) untuk menajamkan kualitas *prompt* Anda.</p>
        
        <!-- Tool 1: CREATE -->
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%; margin-bottom: 30px;">
            <h3 style="margin-bottom: 15px; color: var(--primary);">1. Kerangka Lanjutan (CREATE)</h3>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:15px; margin-bottom:15px;">
                <input type="text" id="t2-c" placeholder="C: Character (Karakter)" style="padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
                <input type="text" id="t2-r" placeholder="R: Request (Permintaan Utama)" style="padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
            </div>
            <textarea id="t2-e" rows="2" placeholder="E: Explanation (Penjelasan Latar Belakang)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;"></textarea>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:15px; margin-bottom:15px;">
                <input type="text" id="t2-a" placeholder="A: Adjustments (Gaya/Nada Bahasa)" style="padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
                <input type="text" id="t2-t" placeholder="T: Type (Tipe/Format Keluaran)" style="padding:10px; border-radius:8px; border:1px solid #cbd5e1;">
            </div>
            <input type="text" id="t2-ex" placeholder="E: Extras (Batasan Tambahan/Larangan)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;">
            
            <button onclick="genT2a()" class="btn-nav" style="margin-top:0; padding:10px 20px; font-size:1rem;"><i class="fas fa-magic"></i> Rangkai CREATE</button>
            <textarea id="t2a-res" rows="3" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid var(--primary);"></textarea>
        </div>

        <!-- Tool 2: Chain of Thought -->
        <div style="background: #eff6ff; padding: 30px; border-radius: 16px; border: 1px solid #bfdbfe; width: 100%; margin-bottom: 30px;">
            <h3 style="margin-bottom: 15px; color: #3b82f6;">2. Alat Pemecah Masalah Kompleks (CoT)</h3>
            <textarea id="t2b-prob" rows="2" placeholder="Masalah yang rumit (Cth: Susun jadwal ujian untuk 5 kelas dengan syarat tertentu...)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #93c5fd; margin-bottom:15px;"></textarea>
            <button onclick="genT2b()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#3b82f6; font-size:1rem;"><i class="fas fa-brain"></i> Rangkai CoT</button>
            <textarea id="t2b-res" rows="3" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid #3b82f6; background:#fff;"></textarea>
        </div>
        
        <!-- Tool 3: Few Shot -->
        <div style="background: #fdf4ff; padding: 30px; border-radius: 16px; border: 1px solid #f5d0fe; width: 100%;">
            <h3 style="margin-bottom: 15px; color: #d946ef;">3. Alat Analogi Masukan-Keluaran (Few-Shot)</h3>
            <input type="text" id="t2c-ex1" placeholder="Contoh 1 (Cth: Input: Sedih -> Output: Biasa Saja)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #e879f9; margin-bottom:10px;">
            <input type="text" id="t2c-target" placeholder="Input Target Aktual (Cth: Input: Marah -> Output: ?)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #e879f9; margin-bottom:15px;">
            <button onclick="genT2c()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#d946ef; font-size:1rem;"><i class="fas fa-clone"></i> Rangkai Few-Shot</button>
            <textarea id="t2c-res" rows="3" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid #d946ef; background:#fff;"></textarea>
        </div>
        <script>
            function genT2a() {
                const c=document.getElementById("t2-c").value, r=document.getElementById("t2-r").value;
                const e=document.getElementById("t2-e").value, a=document.getElementById("t2-a").value;
                const t=document.getElementById("t2-t").value, ex=document.getElementById("t2-ex").value;
                document.getElementById("t2a-res").value = `Peran: ${c}\\nTolong: ${r}\\nKonteks: ${e}\\nGaya: ${a}\\nFormat: ${t}\\nAturan: ${ex}`;
            }
            function genT2b() {
                document.getElementById("t2b-res").value = `Tolong pecahkan masalah berikut: "${document.getElementById("t2b-prob").value}". Mari kita berpikir pelan-pelan tahap demi tahap (step-by-step) untuk memastikan solusinya akurat.`;
            }
            function genT2c() {
                document.getElementById("t2c-res").value = `Saya ingin Anda memproses data dengan pola berikut:\\nContoh:\\n${document.getElementById("t2c-ex1").value}\\n\\nSekarang kerjakan ini:\\n${document.getElementById("t2c-target").value}`;
            }
        </script>
    </div>
'''

html_sesi3 = '''
    <!-- ALAT BANTU SESI 3 -->
    <div id="tools-sesi3" class="slide">
        <div class="case-badge case-both">🛠️ ALAT BANTU (MULTIPART)</div>
        <h2>Koleksi Alat Bantu Riset (NotebookLM)</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Alat ini dikhususkan untuk memanfaatkan kemampuan analisis dokumen berganda pada NotebookLM secara mendalam.</p>
        
        <!-- Tool 1: Panduan Belajar -->
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%; margin-bottom: 30px;">
            <h3 style="margin-bottom: 15px; color: var(--primary);">1. Ekstraktor Panduan Belajar</h3>
            <input type="text" id="t3-topic" placeholder="Fokus Topik (Cth: Bab 3 Mitosis)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;">
            <button onclick="genT3a()" class="btn-nav" style="margin-top:0; padding:10px 20px; font-size:1rem;"><i class="fas fa-book"></i> Buat Instruksi Kajian</button>
            <textarea id="t3a-res" rows="3" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid var(--primary);"></textarea>
        </div>

        <!-- Tool 2: Soal HOTS -->
        <div style="background: #fffbeb; padding: 30px; border-radius: 16px; border: 1px solid #fde68a; width: 100%; margin-bottom: 30px;">
            <h3 style="margin-bottom: 15px; color: #d97706;">2. Pembangun Soal HOTS (Tingkat Tinggi)</h3>
            <select id="t3-level" style="width:100%; padding:10px; border-radius:8px; border:1px solid #fcd34d; margin-bottom:15px;">
                <option value="C4 (Analisis)">C4: Kemampuan Analisis Kelemahan/Kekuatan</option>
                <option value="C5 (Evaluasi)">C5: Kemampuan Evaluasi/Menilai Kasus</option>
                <option value="C6 (Mencipta)">C6: Kemampuan Menciptakan/Sintesis Opini</option>
            </select>
            <button onclick="genT3b()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#f59e0b; font-size:1rem;"><i class="fas fa-question"></i> Buat Instruksi Evaluasi</button>
            <textarea id="t3b-res" rows="3" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid #f59e0b; background:#fff;"></textarea>
        </div>

        <!-- Tool 3: Gap Analysis -->
        <div style="background: #eff6ff; padding: 30px; border-radius: 16px; border: 1px solid #bfdbfe; width: 100%;">
            <h3 style="margin-bottom: 15px; color: #3b82f6;">3. Pencarian Kesenjangan Referensi (Gap Jurnal)</h3>
            <input type="text" id="t3-gap" placeholder="Tema Penelitian Jurnal yang Diunggah" style="width:100%; padding:10px; border-radius:8px; border:1px solid #93c5fd; margin-bottom:15px;">
            <button onclick="genT3c()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#3b82f6; font-size:1rem;"><i class="fas fa-search-plus"></i> Buat Instruksi Kesenjangan</button>
            <textarea id="t3c-res" rows="3" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid #3b82f6; background:#fff;"></textarea>
        </div>
        <script>
            function genT3a() {
                const t=document.getElementById("t3-topic").value;
                document.getElementById("t3a-res").value = `Berdasarkan seluruh bahan yang saya unggah, tolong sari-kan intisari materi tentang: ${t}. Buatkan poin-poin utama dan konsep kunci yang patut dipelajari siswa.`;
            }
            function genT3b() {
                const l=document.getElementById("t3-level").value;
                document.getElementById("t3b-res").value = `Gunakan materi di dalam dokumen ini untuk merumuskan 5 butir soal obyektif dengan tingkat kognitif ${l}. Sertakan juga rubrik kunci jawabannya yang mengutip isi dokumen.`;
            }
            function genT3c() {
                const t=document.getElementById("t3-gap").value;
                document.getElementById("t3c-res").value = `Berdasarkan semua jurnal yang terlampir yang membahas tentang ${t}, tolong temukan gap metodologi atau celah kajian yang belum dibahas sepenuhnya secara holistik, beserta kutipan paragraf pendukungnya.`;
            }
        </script>
    </div>
'''

html_sesi4 = '''
    <!-- ALAT BANTU SESI 4 -->
    <div id="tools-sesi4" class="slide">
        <div class="case-badge case-both">🛠️ ALAT BANTU (MULTIPART)</div>
        <h2>Koleksi Alat Perangkai Aplikasi (Opal)</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Tiga komponen pembantu bahasa *Prompt* untuk merakit Kartu Input, Kartu AI Generate, dan Kartu Kondisi di Opal.</p>
        
        <!-- Tool 1: Input -->
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%; margin-bottom: 30px;">
            <h3 style="margin-bottom: 15px; color: var(--primary);">1. Deskripsi Kartu Masukan (Input Card)</h3>
            <input type="text" id="t4-in" placeholder="Data apa yang pengguna harus lampirkan?" style="width:100%; padding:10px; border-radius:8px; border:1px solid #cbd5e1; margin-bottom:15px;">
            <button onclick="genT4a()" class="btn-nav" style="margin-top:0; padding:10px 20px; font-size:1rem;"><i class="fas fa-sign-in-alt"></i> Buat Deskripsi Input</button>
            <textarea id="t4a-res" rows="2" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid var(--primary);"></textarea>
        </div>

        <!-- Tool 2: Generate Process -->
        <div style="background: #fffbeb; padding: 30px; border-radius: 16px; border: 1px solid #fde68a; width: 100%; margin-bottom: 30px;">
            <h3 style="margin-bottom: 15px; color: #d97706;">2. Deskripsi Kartu AI Utama (Generate Card)</h3>
            <textarea id="t4-proc" rows="2" placeholder="Bagaimana AI harus memproses Input data tersebut?" style="width:100%; padding:10px; border-radius:8px; border:1px solid #fcd34d; margin-bottom:15px;"></textarea>
            <button onclick="genT4b()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#f59e0b; font-size:1rem;"><i class="fas fa-cogs"></i> Buat Deskripsi Proses</button>
            <textarea id="t4b-res" rows="2" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid #f59e0b; background:#fff;"></textarea>
        </div>

        <!-- Tool 3: Logic -->
        <div style="background: #eff6ff; padding: 30px; border-radius: 16px; border: 1px solid #bfdbfe; width: 100%;">
            <h3 style="margin-bottom: 15px; color: #3b82f6;">3. Deskripsi Syarat & Kondisi (Logic/Conditional)</h3>
            <input type="text" id="t4-cond" placeholder="Syarat kelulusan/verifikasi proses (Cth: Bila hasil memenuhi KKM...)" style="width:100%; padding:10px; border-radius:8px; border:1px solid #93c5fd; margin-bottom:15px;">
            <button onclick="genT4c()" class="btn-nav" style="margin-top:0; padding:10px 20px; background:#3b82f6; font-size:1rem;"><i class="fas fa-random"></i> Buat Logika</button>
            <textarea id="t4c-res" rows="2" readonly style="width:100%; margin-top:15px; padding:10px; border-radius:8px; border:2px solid #3b82f6; background:#fff;"></textarea>
        </div>
        <script>
            function genT4a() { document.getElementById("t4a-res").value = `Aplikasi menerima masukan berupa: ${document.getElementById("t4-in").value}`; }
            function genT4b() { document.getElementById("t4b-res").value = `Gunakan kecerdasan buatan untuk: ${document.getElementById("t4-proc").value}`; }
            function genT4c() { document.getElementById("t4c-res").value = `Apabila ${document.getElementById("t4-cond").value}, maka proses dilanjutkan, bila tidak berhenti.`; }
        </script>
    </div>
'''

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

    # 1. Remove previously added prompt builders (using a regex to strip from <!-- Prompt Builder to end of file, except </body></html>)
    # The previous code injected just before <!-- Slide Penutup --> or </body>.
    # We can use regex to match `<div id="prompt-builder" ... </div> ...` safely because we know it was at the end.
    content = re.sub(r'<!-- Prompt Builder Sesi.*?</div>\s*(?=</body>|<!-- Slide Penutup -->)', '', content, flags=re.DOTALL)
    
    # Just in case, clean up any trailing scripts we added:
    content = re.sub(r'<!-- Prompt Builder Sesi.*$', '</body>\n</html>', content, flags=re.DOTALL)

    # 2. Find the injection point BEFORE the completion slide.
    # The completion slide is usually `<div class="slide" style="text-align: center;">`
    # Or we can look for `Sesi 1 Selesai`, `Lanjut ke Sesi`, etc.
    # A generic way: find the index of the slide that contains the completion text.
    # Let's search for `<div` that contains `Selesai</h2>` or `<div class="slide"` containing `Misi Final` or `Tugas Selesai`.
    # As a simple heuristic, the LAST `<div class="slide"` or the one right before `<!-- Slide Penutup -->`
    
    # Let's split by `<div class="slide"`
    parts = content.split('<div class="slide"')
    
    if len(parts) >= 2:
        # We want to insert our new block before the last slide (which is usually the completion slide)
        # However, for Session1, the last slide is the completion one.
        # But wait, parts[-1] is the last slide.
        # We can insert `insertion_code + '\n    <div class="slide"'` right into the last split.
        parts[-1] = insertion_code + '\n    <div class="slide"' + parts[-1]
        
    content = '<div class="slide"'.join(parts)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")
