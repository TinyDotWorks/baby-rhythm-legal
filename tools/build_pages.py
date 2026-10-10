#!/usr/bin/env python3
"""Builds every page of the legal site from the texts below: index, privacy and support, per language.

    python3 tools/build_pages.py        # rewrites all index.html files in place

All languages share one layout, link to each other and list each other as hreflang alternates.
Never edit the HTML by hand; change the texts here and rebuild.

To add a language:
1. Add (hreflang, folder, native name) to LANGS. The folder is the App's localization code in
   lowercase (`AppLinks.policyLocalizations` in the app builds the same path).
2. Add a T["<code>"] entry translated from T["en"] section by section; keep the effective date.
3. Rebuild, check `git diff` only adds the new folder plus one link per existing page, then have the
   translation reviewed before pushing. After the push, add the code to `AppLinks.policyLocalizations`.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = '<a href="mailto:support@tinydotworks.com">support@tinydotworks.com</a>'
STYLE = '<style>body{font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:720px;margin:2rem auto;padding:0 1rem;color:#3b2a20}h1{font-size:1.6rem}h2{font-size:1.15rem;margin-top:1.6rem}a{color:#b5623f}hr{margin:2.5rem 0;border:0;border-top:1px solid #e6d8cc}small{color:#7a6a5f}</style>'
# (hreflang, folder, native name), in the order the language links are shown.
LANGS = [("en", "", "English"), ("zh-Hans", "zh-hans/", "简体中文"), ("zh-Hant", "zh-hant/", "繁體中文"),
         ("fr", "fr/", "Français"), ("de", "de/", "Deutsch"), ("es", "es/", "Español"), ("it", "it/", "Italiano"),
         ("pt-BR", "pt-br/", "Português (Brasil)"), ("ja", "ja/", "日本語"), ("ko", "ko/", "한국어")]
T = {}
T["en"] = dict(home="Baby Rhythm", tagline="A local-first feeding rhythm tracker for caregivers.", privacy="Privacy Policy", support="Support",
 p_title="Baby Rhythm Privacy Policy", effective="Effective",
 intro="Baby Rhythm is a local-first app. <strong>It does not collect, transmit, sell or share any personal data.</strong> The app has no account, no server, no analytics, no advertising and no third-party SDKs, and it does not track you.",
 sections=[("What the app stores, and where", "Baby names, birth dates, feeding records (time, type, amount, nursing duration) and your settings are stored only on your device, inside the app's private storage. They never leave your device through Baby Rhythm."),
  ("Notifications and Live Activity", "Reminders are local notifications scheduled on your device, and the Live Activity is shown by the system on your Lock Screen, Dynamic Island and paired Apple Watch. Both are generated on the device without any server. Live Activity content does not include baby names."),
  ("Widgets", "Home Screen and Lock Screen widgets show a summary of today's feedings and the next estimated feeding, and may include your baby's name. The app keeps that summary in a storage area on your device that is shared only between Baby Rhythm and its widgets. It is never sent anywhere. Widgets are drawn by the system, so anyone who can see your Home Screen or Lock Screen can see what they show."),
  ("Backups", "Your device's own backup (for example iCloud Backup or a computer backup) may include the app's data, as it does for other apps. That is controlled by your Apple settings, not by Baby Rhythm."),
  ("Deleting your data", "Delete individual records or a baby profile inside the app, or delete the app to remove all of its data from your device. We hold no copy, so there is nothing to request from us."),
  ("Not medical advice", "Feeding predictions are calculated only from your own records and are not medical advice."),
  ("Children's privacy", "The app is intended for parents and caregivers, not for children. Because no data is collected, we hold no information about children."),
  ("Changes and contact", "If this policy changes, the updated version will be posted here with a new effective date. Questions: email {email}.")],
 s_title="Baby Rhythm Support", s_contact="Questions, bug reports or feedback: email {email}.", faq="Common questions",
 q=[("Where is my data?", "Only on your iPhone. Deleting the app deletes it."), ("No reminder or Live Activity?", "Check Settings → Notifications and Live Activities for Baby Rhythm.")])
T["zh-Hans"] = dict(home="Baby Rhythm 宝宝节律", tagline="面向照护者的本地优先喂养节律记录工具。", privacy="隐私政策", support="支持",
 p_title="Baby Rhythm 隐私政策", effective="生效日期",
 intro="Baby Rhythm 是一款本地优先的 App。<strong>它不会收集、传输、出售或共享任何个人数据。</strong>本 App 没有账号、没有服务器、没有数据分析、没有广告，也不使用任何第三方 SDK，并且不会追踪你。",
 sections=[("App 存储的内容及位置", "宝宝的名字、出生日期、喂养记录（时间、类型、奶量、亲喂时长）以及你的设置，仅存储在你的设备上，位于 App 的私有存储空间内。通过 Baby Rhythm，这些数据不会离开你的设备。"),
  ("通知与实时活动", "提醒是在你的设备上安排的本地通知；实时活动由系统显示在你的锁定屏幕、灵动岛和已配对的 Apple Watch 上。两者都在设备本地生成，不经过任何服务器。实时活动的内容不包含宝宝的名字。"),
  ("小组件", "主屏幕和锁定屏幕小组件会显示今天的喂养概况和预计的下次喂养时间，并可能包含宝宝的名字。App 把这份概况保存在你设备上一个仅供 Baby Rhythm 与其小组件共用的存储区域，不会发送到任何地方。小组件由系统绘制，因此任何能看到你主屏幕或锁定屏幕的人，都能看到它们显示的内容。"),
  ("备份", "与其他 App 一样，你设备自身的备份（例如 iCloud 云备份或电脑备份）可能包含本 App 的数据。这由你的 Apple 设置控制，而不是由 Baby Rhythm 控制。"),
  ("删除你的数据", "你可以在 App 内删除单条记录或某个宝宝档案，也可以删除 App 以从设备上移除它的全部数据。我们不保留任何副本，因此无需向我们提出删除请求。"),
  ("非医疗建议", "喂养预测仅根据你自己的记录计算，不构成医疗建议。"),
  ("儿童隐私", "本 App 面向家长和照护者，而非儿童。由于不收集任何数据，我们不持有任何有关儿童的信息。"),
  ("变更与联系方式", "如果本政策有变更，更新后的版本将连同新的生效日期发布在此页面。如有疑问，请发送邮件至 {email}。")],
 s_title="Baby Rhythm 支持", s_contact="疑问、问题反馈或建议：请发送邮件至 {email}。", faq="常见问题",
 q=[("我的数据在哪里？", "只在你的 iPhone 上。删除 App 即会删除数据。"), ("没有收到提醒或实时活动？", "请检查“设置”→“通知”以及 Baby Rhythm 的“实时活动”选项。")])
T["zh-Hant"] = dict(home="Baby Rhythm 寶寶節律", tagline="為照顧者設計的本機優先餵奶節律記錄工具。", privacy="隱私權政策", support="支援",
 p_title="Baby Rhythm 隱私權政策", effective="生效日期",
 intro="Baby Rhythm 是一款本機優先的 App。<strong>它不會蒐集、傳輸、出售或分享任何個人資料。</strong>本 App 沒有帳號、沒有伺服器、沒有數據分析、沒有廣告，也不使用任何第三方 SDK，並且不會追蹤你。",
 sections=[("App 儲存的內容及位置", "寶寶的名字、出生日期、餵奶記錄（時間、類型、奶量、親餵時長）以及你的設定，僅儲存在你的裝置上，位於 App 的私有儲存空間內。透過 Baby Rhythm，這些資料不會離開你的裝置。"),
  ("通知與即時動態", "提醒是在你的裝置上排定的本機通知；即時動態由系統顯示在你的鎖定畫面、動態島和已配對的 Apple Watch 上。兩者都在裝置本機產生，不經過任何伺服器。即時動態的內容不包含寶寶的名字。"),
  ("小工具", "主畫面和鎖定畫面小工具會顯示今天的餵奶概況和預估的下次餵奶時間，並可能包含寶寶的名字。App 把這份概況儲存在你裝置上一個僅供 Baby Rhythm 與其小工具共用的儲存區域，不會傳送到任何地方。小工具由系統繪製，因此任何能看到你主畫面或鎖定畫面的人，都能看到它們顯示的內容。"),
  ("備份", "與其他 App 一樣，你裝置本身的備份（例如 iCloud 備份或電腦備份）可能包含本 App 的資料。這由你的 Apple 設定控制，而不是由 Baby Rhythm 控制。"),
  ("刪除你的資料", "你可以在 App 內刪除單筆記錄或某個寶寶檔案，也可以刪除 App 以從裝置上移除它的全部資料。我們不保留任何副本，因此無需向我們提出刪除請求。"),
  ("非醫療建議", "餵奶預測僅根據你自己的記錄計算，不構成醫療建議。"),
  ("兒童隱私", "本 App 以家長和照顧者為對象，而非兒童。由於不蒐集任何資料，我們不持有任何有關兒童的資訊。"),
  ("變更與聯絡方式", "如果本政策有變更，更新後的版本將連同新的生效日期發布在此頁面。如有疑問，請寄送電子郵件至 {email}。")],
 s_title="Baby Rhythm 支援", s_contact="疑問、問題回報或建議：請寄送電子郵件至 {email}。", faq="常見問題",
 q=[("我的資料在哪裡？", "只在你的 iPhone 上。刪除 App 即會刪除資料。"), ("沒有收到提醒或即時動態？", "請檢查「設定」→「通知」以及 Baby Rhythm 的「即時動態」選項。")])
T["fr"] = dict(home="Baby Rhythm", tagline="Le suivi du rythme des repas, en local, pour celles et ceux qui s'occupent de bébé.", privacy="Politique de confidentialité", support="Assistance",
 p_title="Politique de confidentialité de Baby Rhythm", effective="En vigueur le",
 intro="Baby Rhythm est une app qui fonctionne en local. <strong>Elle ne collecte, ne transmet, ne vend ni ne partage aucune donnée personnelle.</strong> L'app n'a ni compte, ni serveur, ni outil d'analyse, ni publicité, ni SDK tiers, et elle ne vous piste pas.",
 sections=[("Ce que l'app enregistre, et où", "Les prénoms et dates de naissance des bébés, les repas enregistrés (heure, type, quantité, durée de la tétée) et vos réglages sont stockés uniquement sur votre appareil, dans l'espace privé de l'app. Ils ne quittent jamais votre appareil par l'intermédiaire de Baby Rhythm."),
  ("Notifications et Activité en direct", "Les rappels sont des notifications locales programmées sur votre appareil, et l'Activité en direct est affichée par le système sur votre écran verrouillé, dans la Dynamic Island et sur l'Apple Watch jumelée. Les deux sont générées sur l'appareil, sans aucun serveur. Le contenu de l'Activité en direct n'inclut pas le prénom des bébés."),
  ("Widgets", "Les widgets de l'écran d'accueil et de l'écran verrouillé affichent un résumé des repas du jour et l'heure estimée du prochain repas, et peuvent inclure le prénom de votre bébé. L'app conserve ce résumé dans un espace de stockage de votre appareil partagé uniquement entre Baby Rhythm et ses widgets. Il n'est jamais envoyé nulle part. Les widgets sont affichés par le système, donc toute personne qui voit votre écran d'accueil ou votre écran verrouillé peut voir ce qu'ils indiquent."),
  ("Sauvegardes", "La sauvegarde de votre appareil (par exemple la sauvegarde iCloud ou une sauvegarde sur ordinateur) peut inclure les données de l'app, comme pour les autres apps. Cela dépend de vos réglages Apple, et non de Baby Rhythm."),
  ("Supprimer vos données", "Supprimez des saisies ou le profil d'un bébé dans l'app, ou supprimez l'app pour effacer toutes ses données de votre appareil. Nous n'en détenons aucune copie, il n'y a donc rien à nous demander."),
  ("Pas un avis médical", "Les estimations des repas sont calculées uniquement à partir de vos propres saisies et ne constituent pas un avis médical."),
  ("Confidentialité des enfants", "L'app s'adresse aux parents et aux personnes qui s'occupent des enfants, pas aux enfants eux-mêmes. Comme aucune donnée n'est collectée, nous ne détenons aucune information sur des enfants."),
  ("Modifications et contact", "Si cette politique change, la nouvelle version sera publiée ici avec une nouvelle date d'entrée en vigueur. Pour toute question, écrivez à {email}.")],
 s_title="Assistance Baby Rhythm", s_contact="Pour toute question, tout bug ou toute suggestion, écrivez à {email}.", faq="Questions fréquentes",
 q=[("Où sont mes données ?", "Uniquement sur votre iPhone. Supprimer l'app les supprime."), ("Pas de rappel ni d'Activité en direct ?", "Dans Réglages, vérifiez les notifications et les Activités en direct de Baby Rhythm.")])
T["de"] = dict(home="Baby Rhythm", tagline="Ein lokaler Tracker für den Mahlzeiten-Rhythmus deines Babys – für Eltern und alle, die es betreuen.", privacy="Datenschutzerklärung", support="Support",
 p_title="Datenschutzerklärung von Baby Rhythm", effective="Gültig ab",
 intro="Baby Rhythm arbeitet lokal. <strong>Die App erfasst, überträgt, verkauft oder teilt keinerlei personenbezogene Daten.</strong> Sie hat kein Konto, keinen Server, keine Analyse, keine Werbung und keine Drittanbieter-SDKs, und sie trackt dich nicht.",
 sections=[("Was die App speichert und wo", "Namen und Geburtsdaten der Babys, Einträge zu Mahlzeiten (Uhrzeit, Art, Menge, Stilldauer) und deine Einstellungen werden ausschließlich auf deinem Gerät im privaten Speicher der App abgelegt. Über Baby Rhythm verlassen sie dein Gerät nie."),
  ("Mitteilungen und Live-Aktivität", "Erinnerungen sind lokale Mitteilungen, die auf deinem Gerät geplant werden, und die Live-Aktivität zeigt das System auf deinem Sperrbildschirm, in der Dynamic Island und auf der gekoppelten Apple Watch an. Beides entsteht auf dem Gerät, ohne Server. Die Live-Aktivität enthält keine Namen von Babys."),
  ("Widgets", "Widgets auf dem Home-Bildschirm und dem Sperrbildschirm zeigen eine Übersicht der heutigen Mahlzeiten und die geschätzte nächste Mahlzeit und können den Namen deines Babys enthalten. Die App legt diese Übersicht in einem Speicherbereich auf deinem Gerät ab, den nur Baby Rhythm und seine Widgets gemeinsam nutzen. Sie wird nirgendwohin gesendet. Widgets werden vom System dargestellt, daher kann jede Person, die deinen Home-Bildschirm oder Sperrbildschirm sieht, auch ihren Inhalt sehen."),
  ("Backups", "Das Backup deines Geräts (zum Beispiel ein iCloud-Backup oder ein Backup auf einem Computer) kann wie bei anderen Apps auch die Daten dieser App enthalten. Das steuern deine Apple-Einstellungen, nicht Baby Rhythm."),
  ("Deine Daten löschen", "Lösche einzelne Einträge oder ein Babyprofil in der App, oder lösche die App, um alle ihre Daten von deinem Gerät zu entfernen. Wir haben keine Kopie, daher musst du bei uns nichts anfordern."),
  ("Keine medizinische Beratung", "Die Vorhersagen werden nur aus deinen eigenen Einträgen berechnet und sind keine medizinische Beratung."),
  ("Datenschutz bei Kindern", "Die App richtet sich an Eltern und Betreuungspersonen, nicht an Kinder. Da keine Daten erfasst werden, haben wir keine Informationen über Kinder."),
  ("Änderungen und Kontakt", "Wenn sich diese Erklärung ändert, wird die aktualisierte Fassung hier mit neuem Gültigkeitsdatum veröffentlicht. Fragen? Schreib an {email}.")],
 s_title="Baby Rhythm Support", s_contact="Fragen, Fehlermeldungen oder Feedback? Schreib an {email}.", faq="Häufige Fragen",
 q=[("Wo sind meine Daten?", "Nur auf deinem iPhone. Wenn du die App löschst, werden sie gelöscht."), ("Keine Erinnerung oder Live-Aktivität?", "Prüfe in den Einstellungen die Mitteilungen und Live-Aktivitäten für Baby Rhythm.")])
T["es"] = dict(home="Baby Rhythm", tagline="Un registro del ritmo de tomas que funciona en local, para quienes cuidan de un bebé.", privacy="Política de privacidad", support="Ayuda",
 p_title="Política de privacidad de Baby Rhythm", effective="En vigor desde el",
 intro="Baby Rhythm es una app que funciona en local. <strong>No recopila, transmite, vende ni comparte ningún dato personal.</strong> La app no tiene cuenta, servidor, analítica, publicidad ni SDK de terceros, y no te rastrea.",
 sections=[("Qué guarda la app y dónde", "Los nombres y fechas de nacimiento de los bebés, los registros de tomas (hora, tipo, cantidad, duración de la toma al pecho) y tus ajustes se guardan solo en tu dispositivo, dentro del almacenamiento privado de la app. Nunca salen de tu dispositivo a través de Baby Rhythm."),
  ("Notificaciones y Actividad en directo", "Los recordatorios son notificaciones locales programadas en tu dispositivo, y el sistema muestra la Actividad en directo en tu pantalla de bloqueo, en la Dynamic Island y en el Apple Watch enlazado. Ambos se generan en el dispositivo, sin ningún servidor. El contenido de la Actividad en directo no incluye el nombre de los bebés."),
  ("Widgets", "Los widgets de la pantalla de inicio y de la pantalla de bloqueo muestran un resumen de las tomas de hoy y la próxima toma estimada, y pueden incluir el nombre de tu bebé. La app guarda ese resumen en un espacio de tu dispositivo que solo comparten Baby Rhythm y sus widgets. Nunca se envía a ningún sitio. El sistema dibuja los widgets, así que cualquiera que vea tu pantalla de inicio o de bloqueo puede ver lo que muestran."),
  ("Copias de seguridad", "La copia de seguridad de tu dispositivo (por ejemplo, la copia de seguridad de iCloud o en un ordenador) puede incluir los datos de la app, como ocurre con otras apps. Eso lo controlan tus ajustes de Apple, no Baby Rhythm."),
  ("Eliminar tus datos", "Elimina registros sueltos o el perfil de un bebé dentro de la app, o elimina la app para borrar todos sus datos de tu dispositivo. No guardamos ninguna copia, así que no hay nada que solicitarnos."),
  ("No es consejo médico", "Las predicciones de tomas se calculan solo a partir de tus propios registros y no son consejo médico."),
  ("Privacidad de los niños", "La app está pensada para madres, padres y cuidadores, no para niños. Como no se recopila ningún dato, no tenemos información sobre niños."),
  ("Cambios y contacto", "Si esta política cambia, la versión actualizada se publicará aquí con una nueva fecha de entrada en vigor. Si tienes dudas, escribe a {email}.")],
 s_title="Ayuda de Baby Rhythm", s_contact="Para dudas, errores o sugerencias, escribe a {email}.", faq="Preguntas frecuentes",
 q=[("¿Dónde están mis datos?", "Solo en tu iPhone. Si eliminas la app, se eliminan."), ("¿No ves recordatorios ni la Actividad en directo?", "En Ajustes, revisa las notificaciones y las Actividades en directo de Baby Rhythm.")])
T["it"] = dict(home="Baby Rhythm", tagline="Un diario del ritmo delle poppate che funziona in locale, per chi si prende cura di un bambino.", privacy="Informativa sulla privacy", support="Assistenza",
 p_title="Informativa sulla privacy di Baby Rhythm", effective="In vigore dal",
 intro="Baby Rhythm è un'app che funziona in locale. <strong>Non raccoglie, trasmette, vende né condivide alcun dato personale.</strong> L'app non ha account, server, strumenti di analisi, pubblicità né SDK di terze parti, e non ti traccia.",
 sections=[("Cosa salva l'app e dove", "I nomi e le date di nascita dei bambini, le poppate registrate (ora, tipo, quantità, durata dell'allattamento al seno) e le tue impostazioni sono salvati solo sul tuo dispositivo, nello spazio privato dell'app. Tramite Baby Rhythm non lasciano mai il tuo dispositivo."),
  ("Notifiche e Attività in tempo reale", "I promemoria sono notifiche locali programmate sul tuo dispositivo, e l'Attività in tempo reale viene mostrata dal sistema sulla schermata di blocco, nella Dynamic Island e sull'Apple Watch abbinato. Entrambi sono generati sul dispositivo, senza alcun server. Il contenuto dell'Attività in tempo reale non include i nomi dei bambini."),
  ("Widget", "I widget della schermata Home e della schermata di blocco mostrano un riepilogo delle poppate di oggi e la prossima poppata stimata, e possono includere il nome del tuo bambino. L'app conserva questo riepilogo in uno spazio del tuo dispositivo condiviso solo tra Baby Rhythm e i suoi widget. Non viene mai inviato altrove. I widget sono disegnati dal sistema, quindi chiunque veda la tua schermata Home o di blocco può vedere ciò che mostrano."),
  ("Backup", "Il backup del tuo dispositivo (ad esempio il backup di iCloud o su computer) può includere i dati dell'app, come avviene per le altre app. Questo dipende dalle tue impostazioni Apple, non da Baby Rhythm."),
  ("Eliminare i tuoi dati", "Elimina singole registrazioni o il profilo di un bambino nell'app, oppure elimina l'app per rimuovere tutti i suoi dati dal dispositivo. Non conserviamo alcuna copia, quindi non c'è nulla da richiederci."),
  ("Non è un consiglio medico", "Le previsioni delle poppate sono calcolate solo dalle tue registrazioni e non costituiscono un consiglio medico."),
  ("Privacy dei minori", "L'app è pensata per i genitori e per chi si prende cura dei bambini, non per i bambini. Poiché non viene raccolto alcun dato, non disponiamo di informazioni sui minori."),
  ("Modifiche e contatti", "Se questa informativa cambia, la versione aggiornata sarà pubblicata qui con una nuova data di entrata in vigore. Per domande, scrivi a {email}.")],
 s_title="Assistenza Baby Rhythm", s_contact="Per domande, segnalazioni di bug o suggerimenti, scrivi a {email}.", faq="Domande frequenti",
 q=[("Dove sono i miei dati?", "Solo sul tuo iPhone. Se elimini l'app, vengono eliminati."), ("Nessun promemoria o Attività in tempo reale?", "In Impostazioni, controlla le notifiche e le Attività in tempo reale di Baby Rhythm.")])
T["pt-BR"] = dict(home="Baby Rhythm", tagline="Um registro do ritmo das mamadas que funciona no aparelho, para quem cuida de um bebê.", privacy="Política de Privacidade", support="Suporte",
 p_title="Política de Privacidade do Baby Rhythm", effective="Em vigor desde",
 intro="O Baby Rhythm é um app que funciona localmente. <strong>Ele não coleta, transmite, vende nem compartilha nenhum dado pessoal.</strong> O app não tem conta, servidor, análise de uso, anúncios nem SDKs de terceiros, e não rastreia você.",
 sections=[("O que o app guarda e onde", "Os nomes e datas de nascimento dos bebês, os registros de mamadas (horário, tipo, quantidade, duração no peito) e seus ajustes ficam armazenados apenas no seu aparelho, no armazenamento privado do app. Eles nunca saem do seu aparelho pelo Baby Rhythm."),
  ("Notificações e Atividade ao Vivo", "Os lembretes são notificações locais agendadas no seu aparelho, e a Atividade ao Vivo é exibida pelo sistema na Tela Bloqueada, na Dynamic Island e no Apple Watch emparelhado. Ambos são gerados no aparelho, sem nenhum servidor. O conteúdo da Atividade ao Vivo não inclui o nome dos bebês."),
  ("Widgets", "Os widgets da Tela de Início e da Tela Bloqueada mostram um resumo das mamadas de hoje e a próxima mamada estimada, e podem incluir o nome do seu bebê. O app guarda esse resumo em uma área do seu aparelho compartilhada apenas entre o Baby Rhythm e seus widgets. Ele nunca é enviado para lugar nenhum. Os widgets são desenhados pelo sistema, então qualquer pessoa que veja sua Tela de Início ou Tela Bloqueada pode ver o que eles mostram."),
  ("Backups", "O backup do seu aparelho (por exemplo, o Backup do iCloud ou um backup no computador) pode incluir os dados do app, como acontece com outros apps. Isso é controlado pelos seus ajustes da Apple, não pelo Baby Rhythm."),
  ("Apagar seus dados", "Apague registros individuais ou o perfil de um bebê no app, ou apague o app para remover todos os dados dele do seu aparelho. Não guardamos nenhuma cópia, então não há nada a nos solicitar."),
  ("Não é orientação médica", "As previsões de mamadas são calculadas apenas com base nos seus próprios registros e não são orientação médica."),
  ("Privacidade de crianças", "O app é destinado a mães, pais e cuidadores, não a crianças. Como nenhum dado é coletado, não temos informações sobre crianças."),
  ("Alterações e contato", "Se esta política mudar, a versão atualizada será publicada aqui com uma nova data de vigência. Dúvidas? Envie um e-mail para {email}.")],
 s_title="Suporte do Baby Rhythm", s_contact="Dúvidas, relatos de erros ou sugestões? Envie um e-mail para {email}.", faq="Perguntas frequentes",
 q=[("Onde ficam meus dados?", "Só no seu iPhone. Apagar o app apaga os dados."), ("Não aparece lembrete nem Atividade ao Vivo?", "Em Ajustes, verifique as notificações e as Atividades ao Vivo do Baby Rhythm.")])
T["ja"] = dict(home="Baby Rhythm", tagline="保護者や育児をする方のための、端末内で完結する授乳リズム記録アプリです。", privacy="プライバシーポリシー", support="サポート",
 p_title="Baby Rhythm プライバシーポリシー", effective="施行日",
 intro="Baby Rhythm は端末内で完結するアプリです。<strong>個人データを収集、送信、販売、共有することは一切ありません。</strong>アカウント、サーバ、解析、広告、サードパーティ製 SDK はなく、ユーザーをトラッキングすることもありません。",
 sections=[("アプリが保存する情報と保存場所", "赤ちゃんの名前と生年月日、授乳の記録（時刻、種類、量、直接授乳の時間）、および設定は、お使いのデバイス上のアプリ専用の保存領域にのみ保存されます。Baby Rhythm を通じてデバイスの外に送られることはありません。"),
  ("通知とライブアクティビティ", "リマインダーはデバイス上でスケジュールされるローカル通知です。ライブアクティビティは、ロック画面、Dynamic Island、ペアリングされた Apple Watch にシステムが表示します。いずれもサーバを使わずデバイス上で生成されます。ライブアクティビティの内容に赤ちゃんの名前は含まれません。"),
  ("ウィジェット", "ホーム画面とロック画面のウィジェットには、今日の授乳の概要と次の授乳の予測時刻が表示され、赤ちゃんの名前が含まれる場合があります。アプリはこの概要を、Baby Rhythm とそのウィジェットだけが共有するデバイス上の保存領域に保存し、どこにも送信しません。ウィジェットはシステムが描画するため、ホーム画面やロック画面を見られる人は誰でもその内容を見ることができます。"),
  ("バックアップ", "ほかのアプリと同様に、デバイス自体のバックアップ（iCloud バックアップやコンピュータへのバックアップなど）にはアプリのデータが含まれる場合があります。これは Baby Rhythm ではなく、Apple の設定によって管理されます。"),
  ("データの削除", "アプリ内で個別の記録や赤ちゃんのプロフィールを削除できます。アプリを削除すると、そのデータはすべてデバイスから消去されます。当方はコピーを保持していないため、削除をご依頼いただく必要はありません。"),
  ("医療上のアドバイスではありません", "授乳の予測はご自身の記録のみにもとづいて計算されるもので、医療上のアドバイスではありません。"),
  ("子どものプライバシー", "本アプリは保護者や育児をする方を対象としており、子ども向けではありません。データを収集しないため、子どもに関する情報を保有することはありません。"),
  ("変更とお問い合わせ", "本ポリシーを変更する場合は、新しい施行日とともに更新版をこのページに掲載します。ご質問は {email} までメールでお寄せください。")],
 s_title="Baby Rhythm サポート", s_contact="ご質問、不具合のご報告、ご意見は {email} までメールでお寄せください。", faq="よくある質問",
 q=[("データはどこにありますか？", "お使いの iPhone の中だけです。アプリを削除するとデータも削除されます。"), ("リマインダーやライブアクティビティが表示されない場合は？", "「設定」で Baby Rhythm の通知とライブアクティビティを確認してください。")])
T["ko"] = dict(home="Baby Rhythm", tagline="보호자를 위한, 기기 안에서 작동하는 수유 리듬 기록 앱입니다.", privacy="개인정보 처리방침", support="지원",
 p_title="Baby Rhythm 개인정보 처리방침", effective="시행일",
 intro="Baby Rhythm은 기기 안에서 작동하는 앱입니다. <strong>어떤 개인 데이터도 수집, 전송, 판매 또는 공유하지 않습니다.</strong> 계정, 서버, 분석 도구, 광고, 서드파티 SDK가 없으며 사용자를 추적하지 않습니다.",
 sections=[("앱이 저장하는 정보와 저장 위치", "아기의 이름과 생년월일, 수유 기록(시간, 종류, 양, 모유 수유 시간), 설정은 사용자의 기기 안, 앱 전용 저장 공간에만 저장됩니다. Baby Rhythm을 통해 기기 밖으로 나가는 일은 없습니다."),
  ("알림과 실시간 현황", "리마인더는 기기에서 예약되는 로컬 알림이며, 실시간 현황은 시스템이 잠금 화면, Dynamic Island, 페어링된 Apple Watch에 표시합니다. 둘 다 서버 없이 기기에서 생성됩니다. 실시간 현황에는 아기 이름이 포함되지 않습니다."),
  ("위젯", "홈 화면과 잠금 화면 위젯은 오늘의 수유 요약과 다음 수유 예상 시간을 보여 주며, 아기 이름이 포함될 수 있습니다. 앱은 이 요약을 Baby Rhythm과 그 위젯만 함께 쓰는 기기 내 저장 공간에 보관하며, 어디로도 전송하지 않습니다. 위젯은 시스템이 그리므로 홈 화면이나 잠금 화면을 볼 수 있는 사람은 누구나 위젯 내용을 볼 수 있습니다."),
  ("백업", "다른 앱과 마찬가지로 기기 자체의 백업(예: iCloud 백업 또는 컴퓨터 백업)에 앱 데이터가 포함될 수 있습니다. 이는 Baby Rhythm이 아닌 사용자의 Apple 설정에 따라 결정됩니다."),
  ("데이터 삭제", "앱에서 개별 기록이나 아기 프로필을 삭제할 수 있으며, 앱을 삭제하면 기기에서 모든 데이터가 제거됩니다. 저희는 사본을 보관하지 않으므로 별도로 요청하실 것이 없습니다."),
  ("의학적 조언이 아닙니다", "수유 예측은 사용자가 직접 입력한 기록만으로 계산되며 의학적 조언이 아닙니다."),
  ("아동 개인정보", "이 앱은 아동이 아닌 부모와 보호자를 위한 앱입니다. 데이터를 수집하지 않으므로 아동에 관한 정보를 보유하지 않습니다."),
  ("변경 사항 및 문의", "이 방침이 변경되면 새 시행일과 함께 업데이트된 내용을 이 페이지에 게시합니다. 문의 사항은 {email}로 이메일을 보내 주세요.")],
 s_title="Baby Rhythm 지원", s_contact="질문, 버그 신고 또는 의견은 {email}로 이메일을 보내 주세요.", faq="자주 묻는 질문",
 q=[("제 데이터는 어디에 있나요?", "사용자의 iPhone에만 있습니다. 앱을 삭제하면 데이터도 삭제됩니다."), ("리마인더나 실시간 현황이 보이지 않나요?", "설정에서 Baby Rhythm의 알림과 실시간 현황을 확인해 주세요.")])

def text(s, lang):
    if lang in ("fr", "it"):
        s = s.replace("'", "’")  # typographic apostrophe, as in the app
    return s.replace("{email}", EMAIL)

def render(lang, folder, page):
    t = T[lang]
    depth = folder.count("/") + (1 if page else 0)
    up = "../" * depth
    href = lambda f: (up + f + (page + "/" if page else "")) or "./"
    alts = "".join(f'<link rel="alternate" hreflang="{c}" href="{href(f)}">' for c, f, _ in LANGS)
    switch = " · ".join(f'<a href="{href(f)}" hreflang="{c}" lang="{c}">{n}</a>' for c, f, n in LANGS if c != lang)
    title = {"": t["home"], "privacy": t["p_title"], "support": t["s_title"]}[page]
    head = f'<!doctype html><html lang="{lang}"><head><title>{title}</title><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">{alts}{STYLE}</head><body>\n'
    if page == "":
        body = (f'<h1>Baby Rhythm</h1>\n<p>{text(t["tagline"], lang)}</p>\n<ul><li><a href="privacy/">{t["privacy"]}</a></li><li><a href="support/">{t["support"]}</a></li></ul>\n'
                f'<p><small>{switch}</small></p>\n<p><small>© 2026 TinyDotWorks</small></p></body></html>\n')
    elif page == "privacy":
        body = f'<h1>{title}</h1>\n<p><small>{t["effective"]} 2026-10-08 · {switch}</small></p>\n<p>{text(t["intro"], lang)}</p>\n'
        body += "".join(f'<h2>{text(h, lang)}</h2>\n<p>{text(p, lang)}</p>\n' for h, p in t["sections"]) + "</body></html>\n"
    else:
        body = f'<h1>{title}</h1>\n<p><small>{switch}</small></p>\n<p>{text(t["s_contact"], lang)}</p>\n<h2>{t["faq"]}</h2>\n'
        body += "".join(f'<p><strong>{text(q, lang)}</strong><br>{text(a, lang)}</p>\n' for q, a in t["q"])
        body += f'<p><a href="../privacy/">{t["privacy"]}</a></p>\n</body></html>\n'
    return head + body

for lang, folder, _ in LANGS:
    for page in ("", "privacy", "support"):
        path = ROOT / folder / page / "index.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(lang, folder, page), encoding="utf-8")
print("written", len(LANGS) * 3)
