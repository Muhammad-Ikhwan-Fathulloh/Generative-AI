import os

builders = {}

builders['d:\\Generative-AI\\AI_for_Teacher\\Session1_HandsOn.html'] = '''
    <!-- Prompt Builder Sesi 1 -->
    <div id="prompt-builder" class="slide">
        <div class="case-badge case-both">🛠️ ALAT BANTU</div>
        <h2>Alat Pembuat Instruksi Dasar (RTC)</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Isi formulir di bawah ini untuk merangkai instruksi (prompt) dengan cepat menggunakan metode Role, Task, Context.</p>
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%;">
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Peran (Role) AI</label>
                <input type="text" id="pb1-role" placeholder="Contoh: Guru Matematika berpengalaman" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-size:1rem; font-family:inherit;">
            </div>
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Tugas (Task)</label>
                <input type="text" id="pb1-task" placeholder="Contoh: Buatkan 5 soal cerita tentang pecahan" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-size:1rem; font-family:inherit;">
            </div>
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Konteks (Context)</label>
                <textarea id="pb1-context" rows="3" placeholder="Contoh: Untuk siswa SD kelas 4 yang baru belajar dasar pecahan." style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-size:1rem; font-family:inherit; resize:vertical;"></textarea>
            </div>
            <button onclick="generatePromptSesi1()" class="btn-nav" style="margin-top:0; padding:12px 25px;"><i class="fas fa-magic"></i> Rangkai Instruksi</button>
            
            <div style="margin-top: 30px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Hasil Instruksi (Salin & Tempel ke AI)</label>
                <textarea id="pb1-result" rows="5" readonly style="width:100%; padding:15px; border-radius:12px; border:2px solid var(--primary); font-size:1.1rem; font-family:monospace; background: #fff;"></textarea>
                <button onclick="copyPrompt('pb1-result')" style="margin-top:10px; padding:10px 20px; background:#e2e8f0; color:#1e293b; border:none; border-radius:8px; cursor:pointer; font-weight:600;"><i class="fas fa-copy"></i> Salin Instruksi</button>
            </div>
        </div>
        <script>
            function generatePromptSesi1() {
                const role = document.getElementById('pb1-role').value;
                const task = document.getElementById('pb1-task').value;
                const context = document.getElementById('pb1-context').value;
                let prompt = [];
                if(role) prompt.push("Bertindaklah sebagai " + role + ".");
                if(task) prompt.push("Tugas Anda adalah: " + task + ".");
                if(context) prompt.push("Konteks tambahan: " + context);
                document.getElementById('pb1-result').value = prompt.join('\\n\\n');
            }
            function copyPrompt(id) {
                const ta = document.getElementById(id);
                ta.select();
                document.execCommand('copy');
                alert('Instruksi berhasil disalin!');
            }
        </script>
    </div>
'''

builders['d:\\Generative-AI\\AI_for_Teacher\\Session2_HandsOn.html'] = '''
    <!-- Prompt Builder Sesi 2 -->
    <div id="prompt-builder" class="slide">
        <div class="case-badge case-both">🛠️ ALAT BANTU</div>
        <h2>Alat Pembuat Instruksi Lanjutan (CREATE)</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Rangkai instruksi komprehensif menggunakan kerangka CREATE (Character, Request, Explanation, Adjustments, Type, Extras).</p>
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                <div>
                    <label style="display:block; font-weight:600; margin-bottom: 8px;">C - Character (Karakter)</label>
                    <input type="text" id="pb2-c" placeholder="Cth: Ahli Kurikulum Merdeka" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
                </div>
                <div>
                    <label style="display:block; font-weight:600; margin-bottom: 8px;">R - Request (Permintaan)</label>
                    <input type="text" id="pb2-r" placeholder="Cth: Buatkan struktur modul ajar" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
                </div>
            </div>
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">E - Explanation (Penjelasan)</label>
                <textarea id="pb2-e" rows="2" placeholder="Cth: Modul ini ditujukan untuk SMP kelas 7 pada topik ekosistem..." style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit; resize:vertical;"></textarea>
            </div>
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">A - Adjustments (Penyesuaian Gaya)</label>
                <input type="text" id="pb2-a" placeholder="Cth: Gunakan bahasa yang mudah dipahami remaja, nada ramah." style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
                <div>
                    <label style="display:block; font-weight:600; margin-bottom: 8px;">T - Type (Tipe Keluaran)</label>
                    <input type="text" id="pb2-t" placeholder="Cth: Format Tabel dengan 4 kolom" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
                </div>
                <div>
                    <label style="display:block; font-weight:600; margin-bottom: 8px;">E - Extras (Tambahan)</label>
                    <input type="text" id="pb2-ex" placeholder="Cth: Tambahkan 3 soal latihan di akhir" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
                </div>
            </div>
            <button onclick="generatePromptSesi2()" class="btn-nav" style="margin-top:0; padding:12px 25px;"><i class="fas fa-magic"></i> Rangkai Instruksi Lanjutan</button>
            <div style="margin-top: 30px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Hasil Instruksi</label>
                <textarea id="pb2-result" rows="6" readonly style="width:100%; padding:15px; border-radius:12px; border:2px solid var(--primary); font-size:1rem; font-family:monospace; background: #fff;"></textarea>
                <button onclick="copyPrompt('pb2-result')" style="margin-top:10px; padding:10px 20px; background:#e2e8f0; border:none; border-radius:8px; cursor:pointer; font-weight:600;"><i class="fas fa-copy"></i> Salin Instruksi</button>
            </div>
        </div>
        <script>
            function generatePromptSesi2() {
                const c = document.getElementById('pb2-c').value;
                const r = document.getElementById('pb2-r').value;
                const e = document.getElementById('pb2-e').value;
                const a = document.getElementById('pb2-a').value;
                const t = document.getElementById('pb2-t').value;
                const ex = document.getElementById('pb2-ex').value;
                
                let prompt = [];
                if(c) prompt.push("Bertindaklah sebagai: " + c);
                if(r) prompt.push("Tolong: " + r);
                if(e) prompt.push("Penjelasan: " + e);
                if(a) prompt.push("Gaya/Penyesuaian: " + a);
                if(t) prompt.push("Format Keluaran: " + t);
                if(ex) prompt.push("Catatan Tambahan: " + ex);
                
                document.getElementById('pb2-result').value = prompt.join('\\n\\n');
            }
            function copyPrompt(id) {
                const ta = document.getElementById(id);
                ta.select();
                document.execCommand('copy');
                alert('Instruksi berhasil disalin!');
            }
        </script>
    </div>
'''

builders['d:\\Generative-AI\\AI_for_Teacher\\Session3_HandsOn.html'] = '''
    <!-- Prompt Builder Sesi 3 -->
    <div id="prompt-builder" class="slide" style="margin-bottom: 40px;">
        <div class="case-badge case-both">🛠️ ALAT BANTU</div>
        <h2>Alat Pembuat Instruksi Riset (NotebookLM)</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Rangkai instruksi khusus untuk Obrolan Berbasis Data pada dokumen yang Anda unggah.</p>
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%;">
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Tindakan Spesifik</label>
                <select id="pb3-action" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
                    <option value="Berdasarkan dokumen yang diunggah, buatkan ringkasan tentang">Ringkas Dokumen</option>
                    <option value="Berdasarkan dokumen yang diunggah, bandingkan konsep/data tentang">Bandingkan Konsep/Dokumen</option>
                    <option value="Berdasarkan dokumen yang diunggah, buatkan soal tentang">Buatkan Soal Latihan</option>
                    <option value="Berdasarkan dokumen yang diunggah, temukan kesenjangan (gap) terkait">Temukan Kesenjangan (Gap)</option>
                    <option value="Berdasarkan dokumen yang diunggah, jelaskan dengan cara mudah untuk">Jelaskan Konsep Khusus</option>
                </select>
            </div>
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Topik / Fokus Pencarian</label>
                <input type="text" id="pb3-topic" placeholder="Cth: metodologi kualitatif di artikel A dan B" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
            </div>
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Format Tambahan</label>
                <input type="text" id="pb3-format" placeholder="Cth: Tampilkan dalam tabel 3 kolom dengan referensi kutipan" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
            </div>
            
            <button onclick="generatePromptSesi3()" class="btn-nav" style="margin-top:0; padding:12px 25px; background:var(--orange);"><i class="fas fa-magic"></i> Rangkai Instruksi Riset</button>
            <div style="margin-top: 30px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Hasil Instruksi (Salin ke NotebookLM)</label>
                <textarea id="pb3-result" rows="4" readonly style="width:100%; padding:15px; border-radius:12px; border:2px solid var(--orange); font-size:1rem; font-family:monospace; background: #fff;"></textarea>
                <button onclick="copyPrompt('pb3-result')" style="margin-top:10px; padding:10px 20px; background:#e2e8f0; border:none; border-radius:8px; cursor:pointer; font-weight:600;"><i class="fas fa-copy"></i> Salin Instruksi</button>
            </div>
        </div>
        <script>
            function generatePromptSesi3() {
                const action = document.getElementById('pb3-action').value;
                const topic = document.getElementById('pb3-topic').value;
                const format = document.getElementById('pb3-format').value;
                
                let prompt = action + ' ' + (topic ? topic : 'seluruh materi tersebut.');
                if(format) prompt += '\\n\\nFormat yang diminta: ' + format;
                
                document.getElementById('pb3-result').value = prompt;
            }
            function copyPrompt(id) {
                const ta = document.getElementById(id);
                ta.select();
                document.execCommand('copy');
                alert('Instruksi berhasil disalin!');
            }
        </script>
    </div>
'''

builders['d:\\Generative-AI\\AI_for_Teacher\\Session4_HandsOn.html'] = '''
    <!-- Prompt Builder Sesi 4 -->
    <div id="prompt-builder" class="slide" style="margin-bottom: 40px;">
        <div class="case-badge case-both">🛠️ ALAT BANTU</div>
        <h2>Alat Perancang Aplikasi Otomatisasi (Opal)</h2>
        <p style="font-size: 1.2rem; color: var(--dim); margin-bottom: 30px;">Desain deskripsi awal aplikasi Anda dengan struktur input-proses-output. Deskripsi ini nanti dapat Anda tempel di kotak "Buat Aplikasi" pada Opal.</p>
        <div style="background: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid var(--border); width: 100%;">
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Masukan Aplikasi (Input Pengguna)</label>
                <input type="text" id="pb4-input" placeholder="Cth: Menerima unggahan dokumen dari siswa" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
            </div>
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Proses AI Khusus (Kartu Logika / Otak AI)</label>
                <input type="text" id="pb4-process" placeholder="Cth: Menganalisis dokumen tersebut dan memberikan umpan balik rinci" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
            </div>
            <div style="margin-bottom: 20px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Kondisi/Peninjau (Opsional)</label>
                <input type="text" id="pb4-logic" placeholder="Cth: Tambahkan opsi Peninjau bagi guru sebelum hasil dikirim ke siswa" style="width:100%; padding:12px; border-radius:8px; border:1px solid #cbd5e1; font-family:inherit;">
            </div>
            
            <button onclick="generatePromptSesi4()" class="btn-nav" style="margin-top:0; padding:12px 25px; background:var(--primary);"><i class="fas fa-magic"></i> Rangkai Deskripsi Aplikasi</button>
            <div style="margin-top: 30px;">
                <label style="display:block; font-weight:600; margin-bottom: 8px;">Hasil Deskripsi (Tempel di Opal)</label>
                <textarea id="pb4-result" rows="4" readonly style="width:100%; padding:15px; border-radius:12px; border:2px solid var(--primary); font-size:1rem; font-family:monospace; background: #fff;"></textarea>
                <button onclick="copyPrompt('pb4-result')" style="margin-top:10px; padding:10px 20px; background:#e2e8f0; border:none; border-radius:8px; cursor:pointer; font-weight:600;"><i class="fas fa-copy"></i> Salin Deskripsi</button>
            </div>
        </div>
        <script>
            function generatePromptSesi4() {
                const inp = document.getElementById('pb4-input').value;
                const proc = document.getElementById('pb4-process').value;
                const logic = document.getElementById('pb4-logic').value;
                
                let prompt = "Buatkan aplikasi cerdas yang mengatur alur berikut:\\n";
                if(inp) prompt += "1. Masukan: " + inp + "\\n";
                if(proc) prompt += "2. Proses Utama: " + proc + "\\n";
                if(logic) prompt += "3. Alur Logika: " + logic + "\\n";
                
                document.getElementById('pb4-result').value = prompt;
            }
            function copyPrompt(id) {
                const ta = document.getElementById(id);
                ta.select();
                document.execCommand('copy');
                alert('Instruksi berhasil disalin!');
            }
        </script>
    </div>
'''

for filepath, html_block in builders.items():
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid adding multiple times if script is run twice
    if "prompt-builder" in content:
        print(f"Prompt Builder already exists in {filepath}")
        continue
    
    if '<!-- Slide Penutup -->' in content:
        content = content.replace('<!-- Slide Penutup -->', html_block + '\n    <!-- Slide Penutup -->')
    else:
        content = content.replace('</body>', html_block + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Processed {filepath}')

