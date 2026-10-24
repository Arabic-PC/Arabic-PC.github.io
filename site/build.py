# يبني صفحات الموقع: نسخة المعاينة (artifact) ونسخة النشر (github)
# كل الألعاب معرّفة في GAMES تحت، وكل لعبة تطلع لها بطاقة في الرئيسية وصفحة خاصة
import os, shutil, html
B = os.path.dirname(os.path.abspath(__file__)); S = os.path.join(B, 'src')
BRAND = 'ألعاب بالعربي'      # اسم الموقع — يتغيّر من هنا
SOCIAL = {'x': 'https://x.com/Arabic_PC', 'discord': 'https://discord.gg/qZZn2CJPyR', 'youtube': 'https://www.youtube.com/channel/UCnYWo-6GKKKt775nzAENU2Q'}   # روابط الحسابات — رابط ديسكورد يُضاف هنا

exec(open(os.path.join(B, 'pending', 'anno1800.py'), encoding='utf-8').read())
exec(open(os.path.join(B, 'pending', 'manorlords.py'), encoding='utf-8').read())
exec(open(os.path.join(B, 'pending', 'bannerlord.py'), encoding='utf-8').read())
GAMES = [
  dict(
    id='operator', ar_name='ذا أوبريتر', seo_desc='تعريب لعبة The Operator (ذا أوبريتر) كامل بالعربية الفصحى: واجهة الحاسوب والمحادثات والوثائق. يُركَّب ببرنامج صغير بضغطة واحدة ويُزال بضغطة واحدة.', name='The Operator', subtitle='تعريب كامل بالعربية الفصحى',
    platforms=['Steam'], texts='أكثر من 3,200 نص', size='0.5 ميغابايت', exe='Arabic-TheOperator.exe', download='https://arabic-pc.github.io/downloads/Arabic-TheOperator.exe',
    cover='img/operator-cover.jpg', shot='img/operator-shot.jpg', shots=[('img/operator-shot.jpg','قاعدة بيانات المواطنين والسيارات'),('img/operator-shot2.jpg','قراءة الوثائق والشهادات'),('img/operator-shot3.jpg','المحادثة مع HAL في الطرفية')],
    card='لعبة تحقيق تعمل فيها مشغّلاً في جهاز تحقيقات فيدرالي عام 1992، تبحث في قواعد البيانات وتساعد العملاء في الميدان.',
    term='&gt; SEARCH citizens: <span>WELLS, Ray</span><br>&gt; 1 record found · FDI · 1992',
    about='تعمل في اللعبة مشغّلاً في جهاز تحقيقات فيدرالي عام 1992. تجلس أمام حاسوب المكتب، تبحث في سجلات المواطنين والسيارات والملفات، وتوجّه العملاء في الميدان عبر المحادثة.',
    translated=['واجهة الحاسوب داخل اللعبة والقوائم والإعدادات.', 'المحادثات مع العملاء وكل رسائل الدردشة.', 'الوثائق والملفات والتقارير.', 'خط عربي واضح يدعم اتصال الحروف.'],
    names_note='أسماء الأشخاص والشوارع والرموز تبقى بالحروف اللاتينية، لأن اللعبة تطلب منك كتابتها في خانات البحث.',
    sample_en="What I'm looking for is WELLS's home address.", sample_ar='ما أبحث عنه هو عنوان منزل <b class="ltr">WELLS</b>.',
    close_launcher='', open_note='ستجدها بالعربية مباشرة، بدون تغيير أي إعداد.',
    notes=['إذا تحدّثت اللعبة أو فحصت ملفاتها من المشغّل، شغّل البرنامج مرة أخرى.', 'ملفات الحفظ لا تتأثر.'],
    tech=[('الملف الذي يُعدَّل', 'OPERATOR_Data\\resources.assets'), ('بصمة الملف الأصلي', 'ef6dff357b0da76bd12e4202d6d7c653'), ('بصمة الملف بعد التعريب', 'f8669c74cac8859d5c51a099c2f0baa5'), ('مكان النسخة الاحتياطية', 'C:\\ProgramData\\ArabicGames\\operator\\backup')],
    video='l0V6hPcY2Us', video_img='img/operator-video.jpg',
    mock=True),
  dict(
    id='watchdogs', ar_name='واتش دوغز', seo_desc='تعريب لعبة Watch Dogs (واتش دوغز) كامل بالعربية الفصحى: القوائم والمهمات والحوارات. يُركَّب ببرنامج صغير بضغطة واحدة ويُزال بضغطة واحدة.', name='Watch Dogs', subtitle='تعريب كامل للقوائم والمهمات والحوارات',
    platforms=['Ubisoft Connect'], texts='أكثر من 40,000 نص', size='1.1 ميغابايت', exe='Arabic-WatchDogs.exe', download='https://arabic-pc.github.io/downloads/Arabic-WatchDogs.exe',
    version='1.1',
    card='تلعب بدور هاكر في شيكاغو تتحكم في شبكة المدينة الذكية. تخترق الكاميرات والإشارات والهواتف لتكشف من يقف خلف مقتل ابنة أختك.',
    cover='img/watchdogs-cover.jpg', shot='img/watchdogs-menu.jpg', shots=[('img/watchdogs-menu.jpg','قائمة الخيارات بالعربية'),('img/watchdogs-shot2.jpg','اختراق مركز تحكم ctOS'),('img/watchdogs-profiler.jpg','نافذة كشف الأشخاص: العمر والمهنة والدخل')],
    about='تلعب بدور الهاكر «إيدن بيرس» في مدينة شيكاغو التي يديرها نظام واحد اسمه ctOS. تخترق الكاميرات وإشارات المرور والهواتف والحسابات البنكية، وتطارد المسؤولين عن مقتل ابنة أختك.',
    translated=['القوائم والإعدادات وواجهة اللعب.', 'المهمات والأهداف والتنبيهات.', 'نافذة كشف الشخصيات (Profiler) بكل بياناتها: العمر والمهنة والدخل.', 'الحوارات والرسائل والإيميلات والراديو.', 'خط عربي مضاف لخطوط اللعبة.'],
    names_note='أسماء الأشخاص والشوارع والأسلحة والسيارات والأغاني تبقى بالإنجليزية كما هي في اللعبة.',
    sample_en='Hack Security Cameras to profile the cops and ID the corrupt ones.', sample_ar='اخترق كاميرات المراقبة لفحص رجال الشرطة وكشف الفاسدين.',
    close_launcher=' والمشغّل', open_note='ستجدها بالعربية مباشرة. التعريب لا يغيّر طريقة اللعب.',
    notes=['إذا كانت عندك نسخة أقدم من التعريب، شغّل البرنامج الجديد واضغط «تعريب اللعبة» فيتحدّث مباشرة.', 'إذا تحدّثت اللعبة أو فحصت ملفاتها من المشغّل، شغّل البرنامج مرة أخرى.', 'التعريب للعب الفردي.', 'ملفات الحفظ لا تتأثر.'],
    tech=[('الملفات التي تُعدَّل', 'data_win64\\patch1.dat\ndata_win64\\patch1.fat'), ('مكان النسخة الاحتياطية', 'C:\\ProgramData\\ArabicGames\\watchdogs\\backup')],
    video='i0KmqEgl_TA', video_img='img/watchdogs-video.jpg',
    mock=False),
  dict(
    id='lanoire', ar_name='لوس أنجلوس نوار', seo_desc='تعريب لعبة L.A. Noire (لوس أنجلوس نوار) كامل بالعربية الفصحى: الحوارات والقوائم ودفتر المحقق. يُركَّب ببرنامج صغير بضغطة واحدة ويُزال بضغطة واحدة.', use_general=True, name='L.A. Noire', subtitle='تعريب كامل بالعربية الفصحى',
    platforms=['Rockstar Games Launcher'], texts='أكثر من 22,000 نص', size='8.4 ميغابايت', exe='Arabic-LANoire.exe', download='https://arabic-pc.github.io/downloads/Arabic-LANoire.exe',
    card='تلعب بدور محقق في شرطة لوس أنجلوس عام 1947. تفحص مسرح الجريمة وتستجوب المشتبه بهم وتقرأ وجوههم لتعرف من يكذب.',
    cover='img/lanoire-cover.jpg', cover_no_logo=True, shot='img/lanoire-shot.jpg', shots=[('img/lanoire-shot2.jpg','الحوارات مع الترجمة أسفل الشاشة'),('img/lanoire-shot.jpg','قائمة الخيارات'),('img/lanoire-shot3.jpg','دفتر المحقق والرتبة')],
    about='تلعب بدور المحقق «كول فيلبس» في شرطة لوس أنجلوس عام 1947. تجمع الأدلة من مسرح الجريمة، وتدوّنها في دفترك، وتستجوب الشهود والمشتبه بهم، وتقرر من يقول الحقيقة.',
    translated=['القوائم والإعدادات.', 'الحوارات والترجمة أسفل الشاشة.', 'دفتر المحقق والقضايا والأدلة.', 'الوثائق والجرائد.', 'خطوط عربية لكل خطوط اللعبة، وعناوين القوائم مرسومة بالعربية.'],
    names_note='أسماء الشخصيات مكتوبة بالحروف العربية.',
    sample_en="Detective Bekowsky's handwriting is just illegible.", sample_ar='خط المحقق بيكوسكي لا يمكن قراءته أبدًا.',
    close_launcher=' والمشغّل', open_note='اترك لغة اللعبة على الإنجليزية، وستجدها بالعربية مباشرة.',
    notes=['لا تستخدم خيار فحص الملفات في منصة روكستار. إذا استخدمته، شغّل البرنامج مرة أخرى.', 'إذا ظهرت كلمة UPDATING في منصة روكستار وعادت اللعبة إلى الإنجليزية، نزّل آخر نسخة من البرنامج وشغّلها مرة أخرى.', 'ملفات التعريب بنفس حجم الملفات الأصلية وتاريخها، لذلك لا تلاحظها المنصة.', 'ملفات الحفظ لا تتأثر.'],
    tech=[('الملفات التي تُعدَّل', 'final\\pc\\out.wad.pc\nfinal\\pc\\cases.big.pc'), ('مكان النسخة الاحتياطية', 'C:\\ProgramData\\ArabicGames\\lanoire\\backup')],
    video='saDjLGIzEVg', video_img='img/lanoire-video.jpg',
    mock=False),
  dict(
    id='rdr2', ar_name='ريد ديد ريدمبشن 2', seo_desc='تعريب لعبة Red Dead Redemption 2 (ريد ديد ريدمبشن 2) بالعربية: القصة والقوائم والحوارات. يُركَّب ببرنامج صغير بضغطة واحدة ويُزال بضغطة واحدة.', use_general=True, name='Red Dead Redemption 2', subtitle='تعريب القصة والقوائم والحوارات',
    platforms=['Rockstar Games Launcher', 'Steam', 'Epic Games'], texts='أكثر من 240,000 نص', size='12 ميغابايت', exe='Arabic-RDR2.exe', download='https://arabic-pc.github.io/downloads/Arabic-RDR2.exe',
    version='1.2',
    video='t4RHB5spRNI', video_img='img/rdr2-video.jpg',
    card='تلعب بدور «آرثر مورغان» في عصابة خارجين عن القانون تهرب عبر الغرب الأمريكي عام 1899، بين المطاردات والسرقات والصيد وحياة المخيّم.',
    cover='img/rdr2-cover.jpg', shot='img/rdr2-shot.jpg', shots=[('img/rdr2-shot.jpg','الحوارات وأزرار التفاعل بالعربية'),('img/rdr2-shot2.jpg','عجلة الأسلحة وإحصائياتها'),('img/rdr2-shot4.jpg','قائمة الإيقاف')],
    about='تلعب بدور «آرثر مورغان» أحد أفراد عصابة «داتش فان دير ليند» عام 1899. بعد سرقة فاشلة تهرب العصابة من القانون عبر الغرب الأمريكي، وتعيش أنت حياة المخيّم والمطاردات والصيد والقرارات الصعبة.',
    translated=['قصة الطور الفردي كاملة: الحوارات والترجمة أسفل الشاشة.', 'القوائم والإعدادات والخريطة.', 'التعليمات والمهمات والأهداف.', 'الأسلحة والملابس والأغراض والمتاجر.', 'خط عربي مضاف للعبة، والجمل الطويلة مقسّمة على أسطر مرتبة.'],
    names_note='أسماء الشخصيات مكتوبة بالحروف العربية، وأسماء المدن والأماكن على الخريطة تبقى بالإنجليزية.',
    sample_en='Talk to the bartender', sample_ar='تحدث إلى النادل',
    close_launcher=' والمشغّل', open_note='اترك لغة اللعبة على الإنجليزية، وستجدها بالعربية مباشرة.',
    alert=('لا تلعب Red Dead Online والتعريب مركّب', 'التعريب للطور الفردي فقط. قبل الدخول إلى الطور الجماعي شغّل البرنامج واضغط «إرجاع الأصل»، لأن روكستار قد تحظر الحسابات التي تدخل الطور الجماعي بملفات تعديل.'),
    restore='شغّل البرنامج نفسه واضغط «إرجاع الأصل». يحذف البرنامج ملفات التعريب التي أضافها فقط، وتعود اللعبة كما كانت.',
    credit='الترجمة مبنية على تعريب <b>KG Studio</b> بإذن منهم، مع تصحيح الترجمة وترتيب النصوص في فريق {{BRAND}}. شكراً لهم.',
    notes=['البرنامج لا يعدّل أي ملف من ملفات اللعبة الأصلية. يضيف ملفات التعريب بجانبها فقط، لذلك لا تلاحظه منصة روكستار ولا يحتاج نسخة احتياطية.', 'إذا كان عندك تعديلات أخرى تعمل بـ Lenny\'s Mod Loader، يضاف التعريب إليها ولا يحذفها.', 'ملفات الحفظ لا تتأثر.'],
    tech=[('طريقة العمل', "Lenny's Mod Loader (LML)\nUltimate ASI Loader — رخصة MIT"), ('الملفات المضافة', 'dinput8.dll، vfs.asi، lml\\arabic-pc\\'), ('سجل الملفات المضافة', 'C:\\ProgramData\\ArabicGames\\rdr2\\installed.txt')],
    mock=False),
  dict(
    id='readyornot', ar_name='ريدي أور نوت', seo_desc='تعريب لعبة Ready or Not (ريدي أور نوت) بالعربية الفصحى: القوائم والإعدادات وأوامر الفريق والإيجاز ومكالمات الطوارئ والأدلة. يُركَّب ببرنامج صغير بضغطة واحدة ويُزال بضغطة واحدة.', use_general=True, name='Ready or Not', subtitle='تعريب القوائم والأوامر والإيجاز',
    platforms=['Steam'], texts='أكثر من 7,500 نص', size='4 ميغابايت', exe='Arabic-ReadyOrNot.exe', download='https://arabic-pc.github.io/downloads/Arabic-ReadyOrNot.exe',
    version='1.0',
    card='تقود فريق تدخّل خاص (SWAT) في مدينة Los Sueños، تقتحم وتطهّر وتعتقل المشتبه بهم وتنقذ الرهائن بأقل قوة ممكنة.',
    cover='img/readyornot-cover.jpg', shot='img/readyornot-shot.jpg', shots=[('img/readyornot-shot.jpg','إيجاز المهمة والأهداف'),('img/readyornot-shot2.jpg','عجلة أوامر الفريق'),('img/readyornot-shot3.jpg','العتاد والملحقات')],
    about='تقود فريق تدخّل خاص (SWAT) في شرطة مدينة Los Sueños. تخطط للمهمة من الإيجاز، وتختار عتادك، ثم تقتحم المباني وتطهّرها، وتعتقل المشتبه بهم وتنقذ المدنيين، مع إصدار الأوامر لفريقك في كل خطوة.',
    translated=['القوائم والإعدادات كاملة.', 'عجلة أوامر الفريق والتعليمات أثناء اللعب.', 'إيجاز المهمات والأهداف ومكالمات الطوارئ 911.', 'الأدلة والأسلحة والعتاد والملابس، وسير الضباط في وضع القائد.', 'خط عربي مدموج في خطوط اللعبة، وحروف متصلة واتجاه من اليمين لليسار.'],
    names_note='أسماء الأشخاص والأماكن والمهمات والأسلحة تبقى بالحروف اللاتينية.',
    sample_en='Breach and Clear', sample_ar='اقتحام وتطهير',
    close_launcher='', open_note='اترك لغة اللعبة على الإنجليزية، وستجدها بالعربية مباشرة.',
    restore='شغّل البرنامج نفسه واضغط «إرجاع الأصل». يحذف البرنامج ملف التعريب الذي أضافه فقط، وتعود اللعبة كما كانت.',
    notes=['البرنامج لا يعدّل أي ملف من ملفات اللعبة الأصلية. يضيف ملف تعديل واحداً في مجلد التعديلات فقط.', 'التعريب يغيّر النصوص فقط، فلا يؤثر على اللعب ولا على ملفات الحفظ.', 'إذا تحدّثت اللعبة وتغيّرت بعض النصوص، قد تظهر النصوص الجديدة بالإنجليزية حتى نحدّث التعريب.'],
    tech=[('طريقة العمل', 'ملف تعديل Unreal Engine في مجلد ~mods'), ('الملف المضاف', 'ReadyOrNot\\Content\\Paks\\~mods\\ArabicPC_P.pak'), ('الخطوط', 'Noto Sans Arabic مدموج في خطوط اللعبة المفتوحة — رخصة SIL OFL')],
    mock=False),
  ANNO,
  MANOR,
  BANNER,
]

# ألعاب قادمة: تظهر في قسم «قريباً» في الرئيسية. عند النشر تنتقل اللعبة من هنا إلى GAMES
COMING = [
]

r = lambda f: open(os.path.join(S, f), encoding='utf-8').read()
# مكان كل لعبة في نافذة البرنامج المتنقّلة في الرئيسية
MOCK_PATHS = {
  'operator': 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Project OPERATOR',
  'watchdogs': 'C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\games\\Watch_Dogs',
  'lanoire': 'C:\\Program Files\\Rockstar Games\\L.A. Noire',
  'rdr2': 'C:\\Program Files\\Rockstar Games\\Red Dead Redemption 2',
  'readyornot': 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Ready Or Not',
  'anno1800': 'D:\\SteamLibrary\\steamapps\\common\\Anno 1800',
  'manorlords': 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Manor Lords',
}
css, mock, js = r('site.css'), r('app_mock.html'), r('mock.js')
import json as _json
_mg = [dict(name=g['name'], path=MOCK_PATHS.get(g['id'], ''), ver=g.get('version', '1.0')) for g in reversed(GAMES) if g['id'] in MOCK_PATHS]
mock_index = mock.replace('{{MOCK_DATA}}', " data-games='%s'" % html.escape(_json.dumps(_mg, ensure_ascii=False), quote=True))
mock = mock.replace('{{MOCK_DATA}}', '')
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Noto+Kufi+Arabic:wght@500;600;700&display=swap">'
LIGHTBOX = """<div class="lb" id="lb" hidden><button type="button" class="lb-x" aria-label="إغلاق">✕</button><img id="lbImg" alt=""><p id="lbCap"></p></div>
<script>(function(){var lb=document.getElementById('lb');if(!lb)return;var im=document.getElementById('lbImg'),cp=document.getElementById('lbCap');
function close(){lb.hidden=true;im.removeAttribute('src');}
document.querySelectorAll('.zoom').forEach(function(b){b.addEventListener('click',function(){im.src=b.dataset.src;var c=b.parentNode.querySelector('figcaption');cp.textContent=c?c.textContent:'';lb.hidden=false;});});
lb.addEventListener('click',close);document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!lb.hidden)close();});})();</script>"""
YTJS = """<script>(function(){document.querySelectorAll('.yt').forEach(function(b){b.addEventListener('click',function(){var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.id+'?autoplay=1&rel=0';f.title=b.getAttribute('aria-label');f.allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';f.allowFullscreen=true;f.className='yt-frame';b.replaceWith(f);});});})();</script>"""
DLJS = """<script>(function(){var b=document.getElementById('dlBtn'),n=document.getElementById('dlNote');if(b&&b.getAttribute('href')==='#download'){b.addEventListener('click',function(e){e.preventDefault();n.hidden=false;});}})();</script>"""

def card(g):
    if g.get('cover') and g.get('cover_no_logo'):
        art = '<div class="art shot"><img src="%s" alt="%s" loading="lazy"><div class="name">%s</div></div>' % (g['cover'], g['name'], g['name'])
    elif g.get('cover'):
        art = '<div class="art shot cover"><img src="%s" alt="%s" loading="lazy"></div>' % (g['cover'], g['name'])
    elif g.get('shot'):
        art = '<div class="art shot"><img src="%s" alt="لقطة من %s بعد التعريب" loading="lazy"><div class="name">%s</div></div>' % (g['shot'], g['name'], g['name'])
    else:
        art = '<div class="art" aria-hidden="true"><div class="term">%s</div><div class="name">%s</div></div>' % (g['term'], g['name'])
    plats = ''.join('<b class="ltr">%s</b>' % p for p in g['platforms'])
    return ('      <a class="game" href="%s.html">\n        %s\n        <div class="game-body">\n          <h3 class="game-name">%s</h3>\n          <p>%s</p>\n'
            '          <div class="chips"><span class="chip on">متاح</span><span class="chip pc">PC</span><span class="chip">%s</span><span class="chip">%s</span></div>\n'
            '          <span class="game-go">صفحة التعريب ←</span>\n        </div>\n      </a>') % (
            g['id'], art, g['name'], g['card'], g['texts'], g['size'])

def soon_card(g):
    if g.get('cover'):
        art = '<div class="art shot cover"><img src="%s" alt="%s" loading="lazy"></div>' % (g['cover'], g['name'])
    else:
        art = '<div class="art" aria-hidden="true"><div class="term">&gt; ROUTE: <span>Rotterdam → Kraków</span><br>&gt; CARGO: <span>Machinery · 18 t</span></div><div class="name">%s</div></div>' % g['name']
    return ('      <div class="game upcoming">\n        %s\n        <div class="game-body">\n          <h3 class="game-name">%s</h3>\n          <p>%s</p>\n'
            '          <div class="chips"><span class="chip upcoming">قريباً</span><span class="chip pc">PC</span><span class="chip">%s</span></div>\n'
            '          <span class="game-when">%s</span>\n        </div>\n      </div>') % (art, g['name'], g['card'], g['texts'], g['when'])

SOON_SECTION = ('''  <section id="soon">
    <div class="sec-head">
      <div>
        <div class="eyebrow">قريباً</div>
        <h2>ألعاب في الطريق</h2>
      </div>
    </div>

    <div class="games">
%s
    </div>
  </section>
''' % '\n'.join(soon_card(g) for g in COMING)) if COMING else ''

def count_ar(n):
    return {1: 'لعبة واحدة', 2: 'لعبتان'}.get(n, '%d ألعاب' % n)

HOW_VIDEO = ('l0V6hPcY2Us', 'img/operator-video.jpg')   # فيديو The Operator (احتياطي)
# فيديو الشرح العام: ضع رابطه هنا بعد نشره في يوتيوب، فيحلّ محل خطوات الصفحة الرئيسية ويظهر في صفحات الألعاب
HOW_GENERAL = ('VjXcg7ehp68', 'img/how-video.jpg')   # فيديو الشرح العام
HOW_STEPS = '''    <ol class="steps">
      <li><h3>نزّل برنامج اللعبة</h3><p>لكل لعبة برنامج صغير خاص بها. اختر لعبتك واضغط زر التنزيل.</p></li>
      <li><h3>شغّله واضغط «نعم»</h3><p>يطلب البرنامج صلاحية تعديل ملفات اللعبة، ثم يعثر على مكانها في جهازك تلقائياً.</p></li>
      <li><h3>اضغط «تعريب اللعبة»</h3><p>خلال ثوانٍ يكتمل التركيب ويتحقق البرنامج من الملفات. افتح اللعبة وستجدها بالعربية.</p></li>
    </ol>'''
def video_html(vid, img, cap):
    return '<div class="yt-wrap"><button type="button" class="yt" data-id="%s" aria-label="تشغيل فيديو طريقة التركيب"><img src="%s" alt="فيديو: طريقة تركيب التعريب" loading="lazy"><span class="yt-play" aria-hidden="true"></span></button><p class="yt-cap">%s</p></div>' % (vid, img, cap)

def game_body(g):
    b = r('game.body.html')
    cover = '<figure class="g-shot g-cover"><img src="%s" alt="%s"></figure>' % (g['cover'], g['name']) if g.get('cover') else ''
    shot = ''
    if g.get('shots'):
        shot = '<div class="gallery">' + ''.join('<figure><button type="button" class="zoom" data-src="%s" aria-label="تكبير: %s"><img src="%s" alt="%s" loading="lazy"></button><figcaption>%s</figcaption></figure>' % (p, c, p, c, c) for p, c in g['shots']) + '</div>'
        shot = '<section><h2>من داخل اللعبة</h2><p>لقطات من اللعبة بعد التعريب.</p>' + shot + '</section>'
    rep = {
      'NAME': g['name'], 'SUBTITLE': g['subtitle'], 'TEXTS': g['texts'], 'ABOUT': g['about'], 'SHOT': shot, 'COVER': cover,
      'PLATFORM_CHIPS': ''.join('<span class="chip ltr">%s</span>' % p for p in g['platforms']),
      'PLATFORMS': '، '.join(g['platforms']),
      'TRANSLATED': ''.join('<li>%s</li>' % t for t in g['translated']),
      'NAMES_NOTE': g['names_note'], 'SAMPLE_EN': html.escape(g['sample_en']), 'SAMPLE_AR': g['sample_ar'],
      'CLOSE_LAUNCHER': g['close_launcher'], 'OPEN_NOTE': g['open_note'],
      'MOCK_SLOT': '<div class="mock-slot">%s</div>' % mock if g['mock'] else '',
      'NOTES': ''.join('<li>%s</li>' % t for t in g['notes']),
      'TECH': ''.join('<tr><td>%s</td><td>%s</td></tr>' % (k, html.escape(v).replace('\n', '<br>')) for k, v in g['tech']),
      'EXE': g['exe'], 'SIZE': g['size'], 'VERSION': g.get('version', '1.0'),
      'ALERT': ('<div class="alert" role="note"><b>%s</b><p>%s</p></div>' % g['alert']) if g.get('alert') else '',
      'RESTORE': g.get('restore', 'شغّل البرنامج نفسه واضغط «إرجاع الأصل». يعيد البرنامج الملفات الأصلية التي حفظها قبل التعريب ويتحقق منها.'),
      'CREDIT': ('<section><h2>شكر</h2><p class="credit">%s</p></section>' % g['credit']) if g.get('credit') else '',
      'VIDEO': (video_html(g['video'], g['video_img'], 'شاهد طريقة التركيب بالفيديو، أو اتبع الخطوات تحت.') if g.get('video') else video_html(HOW_GENERAL[0], HOW_GENERAL[1], 'شاهد طريقة التركيب بالفيديو، أو اتبع الخطوات تحت.') if (HOW_GENERAL and g.get('use_general')) else ''),
    }
    for k, v in rep.items(): b = b.replace('{{%s}}' % k, v)
    if g['download']: b = b.replace('href="#download"', 'href="%s" download data-goatcounter-click="download-%s" data-goatcounter-title="تنزيل %s"' % (g['download'], g['id'], g['name']))
    return b

# عداد الزوار والتنزيلات (GoatCounter: بدون كوكيز). اتركه فارغاً لإيقافه
COUNTER = 'arabic-pc'
MODE = 'github'
# نسخة ثابتة من سكربت العداد مع بصمتها (من https://www.goatcounter.com/help/countjs-versions، ومحسوبة من الملف نفسه)
COUNTER_JS = 'https://gc.zgo.at/count.v5.js'
COUNTER_SRI = 'sha384-atnOLvQb9t+jTSipvd75X2yginT4PjVbqDdlJAmxMm+wYElFmeR6EmLP5bYeoRVQ'
def counter_on(): return bool(COUNTER) and MODE == 'github'
def counter_js():
    if not counter_on(): return ''
    return '<script data-goatcounter="https://%s.goatcounter.com/count" async src="%s" integrity="%s" crossorigin="anonymous"></script>\n' % (COUNTER, COUNTER_JS, COUNTER_SRI)

# سياسة أمان المحتوى (CSP): السكربتات والأنماط الداخلية مسموحة ببصمتها فقط، فأي تعديل فيها يحدّث البصمة تلقائياً
import re, hashlib, base64
def _sha(s): return "'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode('utf-8')).digest()).decode()
def csp(page):
    if re.search(r'\sstyle=|\son[a-z]+=|javascript:', page): raise SystemExit('CSP: نمط أو حدث داخل وسم، انقله لملف الأنماط أو السكربت')
    scripts = [_sha(m) for m in re.findall(r'<script>(.*?)</script>', page, re.S)]
    styles = [_sha(m) for m in re.findall(r'<style>(.*?)</style>', page, re.S)]
    gc = 'https://%s.goatcounter.com' % COUNTER
    p = ["default-src 'none'",
         'script-src ' + ' '.join(scripts + ([COUNTER_JS] if counter_on() else [])),
         'style-src ' + ' '.join(styles + ['https://fonts.googleapis.com']),
         'font-src https://fonts.gstatic.com',
         "img-src 'self'" + (' ' + gc if counter_on() else '')]
    if counter_on(): p.append('connect-src ' + gc)
    if 'class="yt"' in page: p.append('frame-src https://www.youtube-nocookie.com')
    p += ["base-uri 'none'", "form-action 'none'"]
    return '<meta http-equiv="Content-Security-Policy" content="%s">\n' % '; '.join(p)

SITE_LD = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"ألعاب بالعربي","alternateName":["Arabic PC","ألعاب بالعربي - Arabic PC"],"url":"https://arabic-pc.github.io/"}</script>\n'
DESC = 'تعريب ألعاب الكمبيوتر بالعربية الفصحى، يُركَّب ببرنامج صغير بضغطة واحدة ويُزال بضغطة واحدة.'

def doc(title, body, anim, full, desc=None, ldjson=''):
    body = body.replace('{{BRAND}}', BRAND).replace('{{X_URL}}', SOCIAL['x']).replace('{{DISCORD_URL}}', SOCIAL['discord'] or '#discord').replace('{{YT_URL}}', SOCIAL['youtube'])
    head = '<title>%s</title>\n%s\n<style>\n%s\n</style>\n' % (title, FONTS, css)
    tail = ('<script>\n%s\n</script>\n' % js if anim else '') + DLJS + (LIGHTBOX if 'class="zoom"' in body else '') + (YTJS if 'class="yt"' in body else '') + counter_js()
    if full:
        d0 = desc or DESC
        meta = '<meta name="description" content="%s">\n<link rel="icon" type="image/png" href="img/icon.png">\n<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n<meta property="og:image" content="https://arabic-pc.github.io/img/icon.png">\n<meta name="theme-color" content="#0D1119">\n<meta name="google-site-verification" content="0khRUPTyk-3FLgudLrnjnzi9njk2wVIBT3IxozMUFL8">\n<meta property="og:site_name" content="%s">\n' % (d0, title, d0, BRAND) + ldjson
        page = meta + '%s</head>\n<body>\n%s\n%s</body>\n</html>\n' % (head, body, tail)
        return '<!doctype html>\n<html lang="ar" dir="rtl">\n<head>\n<meta charset="utf-8">\n' + csp(page) + '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' + page
    return head + body + '\n' + tail

index_body = r('index.body.html').replace('{{APP_MOCK}}', mock_index).replace('{{GAME_CARDS}}', '\n'.join(card(g) for g in GAMES)).replace('{{GAME_COUNT}}', count_ar(len(GAMES))).replace('{{SOON}}', SOON_SECTION).replace('{{HOW_HEAD}}', '<div class="eyebrow">شاهد الشرح</div>\n        <h2>فيديو طريقة تركيب التعريب وتثبيت البرنامج</h2>' if HOW_GENERAL else '<div class="eyebrow">ثلاث خطوات</div>\n        <h2>طريقة التركيب</h2>').replace('{{HOW_BODY}}', video_html(HOW_GENERAL[0], HOW_GENERAL[1], 'الطريقة نفسها في كل الألعاب.') if HOW_GENERAL else HOW_STEPS)
for mode in ('artifact', 'github'):
    MODE = mode
    d = os.path.join(B, 'out', mode)
    if os.path.isdir(d): shutil.rmtree(d)
    os.makedirs(os.path.join(d, 'img'))
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(doc(BRAND + ' | تعريب ألعاب الكمبيوتر بالعربية', index_body, True, mode == 'github', ldjson=SITE_LD))
    for g in GAMES:
        open(os.path.join(d, g['id'] + '.html'), 'w', encoding='utf-8').write(doc('تعريب ' + g['name'] + ' (' + g['ar_name'] + ') بالعربية | ' + BRAND, game_body(g), g['mock'], True, desc=g['seo_desc']))
    for f in os.listdir(os.path.join(S, 'img')): shutil.copyfile(os.path.join(S, 'img', f), os.path.join(d, 'img', f))
print('built', len(GAMES), 'games')
