# coding=utf-8
import re  

# Driver Code 
string1 = "[{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]{'type': 'uri', 'value': 'http://dbpedia.org/class/yago/TopographicPoint108664443'}"


'''
for m in re.finditer("http://", string1):
    # print(m)
    i = m.start()
    while(string1[i] is not '\''):
        i=i+1
    print(string1[m.start():i])
'''

def getUrlSet(input):
    myset = set()
    for m in re.finditer("http://", str(input)):
    # print(m)
        i = m.start()
        while(string1[i] is not "'"):
            i=i+1
        print(string1[m.start():i])
        myset.add(input[m.start():i])
        return myset


str = "{'http://dbpedia.org/resource/Inside_(Paul_Horn_album)': {'http://dbpedia.org/ontology/recordedIn': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/The_Taj_Mahal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Tadj_Mahal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Mumtaz_Mahal': {'http://dbpedia.org/ontology/restingPlace': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Tāj_Mahal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj_Mahal_(disambiguation)': {'http://dbpedia.org/ontology/wikiPageDisambiguates': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Mahal': {'http://dbpedia.org/ontology/wikiPageDisambiguates': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj_mahal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj_Majal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj+mahal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Tejomahal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj_Mahal,_India': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://en.wikipedia.org/wiki/Taj_Mahal': {'http://xmlns.com/foaf/0.1/primaryTopic': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Tai_Mahal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj_mahel': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Uttar_Pradesh_Heritage_Arc': {'http://dbpedia.org/property/landmark': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj_Mahal_(palace)': {'http://www.w3.org/2002/07/owl#differentFrom': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Shah_Jahan': {'http://dbpedia.org/property/burialPlace': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, "http://dbpedia.org/resource/List_of_Late_Night_with_Conan_O'Brien_episodes_(season_4)": {'http://dbpedia.org/property/guests': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Tajmahal': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/ताज_महल': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Gauharara_Begum': {'http://dbpedia.org/ontology/restingPlace': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Trump_Taj_Mahal': {'http://dbpedia.org/property/theme': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj_Mahal': {'http://www.w3.org/1999/02/22-rdf-syntax-ns#type': [{'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Cemetery108521623'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Plot108674739'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Garden103417345'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatWorldHeritageSitesInIndia'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Area102735688'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Site108651247'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Tract108673395'}, {'type': 'uri', 'value': 'http://www.w3.org/2002/07/owl#Thing'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/TopographicPoint108664443'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/GeographicPoint108578706'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Point108620061'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Grave103455033'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/GeographicalArea108574314'}, {'type': 'uri', 'value': 'http://dbpedia.org/ontology/HistoricPlace'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Facility103315023'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatPersianGardens'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Garrison103420559'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/MilitaryInstallation103763133'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/MilitaryPost103763403'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Chamber103003730'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Residence108558963'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Address108491027'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatRoyalResidencesInIndia'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatMausoleumsInUttarPradesh'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatFortsInDelhi'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatPersianGardensInIndia'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatMonumentsAndMemorialsInUttarPradesh'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatMughalFuneraryGardensInIndia'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Location100027167'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Memorial103743902'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Region108630985'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Artifact100021939'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/YagoGeoEntity'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/YagoPermanentlyLocatedEntity'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Structure104341686'}, {'type': 'uri', 'value': 'http://dbpedia.org/ontology/Location'}, {'type': 'uri', 'value': 'http://dbpedia.org/ontology/Place'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/BurialChamber102921884'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/PhysicalEntity100001930'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Mausoleum103732114'}, {'type': 'uri', 'value': 'http://schema.org/Place'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatMausoleumsInIndia'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Object100002684'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/YagoLegalActorGeo'}, {'type': 'uri', 'value': 'http://schema.org/LandmarksOrHistoricalBuildings'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatMausoleums'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatBurialSitesOfEuropeanRoyalFamilies'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatGardensInIndia'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/WikicatMonumentsAndMemorialsInIndia'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Whole100003553'}, {'type': 'uri', 'value': 'http://dbpedia.org/class/yago/Enclosure103285912'}], 'http://www.w3.org/2000/01/rdf-schema#label': [{'type': 'literal', 'value': 'تاج محل', 'lang': 'ar'}, {'type': 'literal', 'value': 'Taj Mahal', 'lang': 'fr'}, {'type': 'literal', 'value': 'Тадж-Махал', 'lang': 'ru'}, {'type': 'literal', 'value': 'Taj Mahal', 'lang': 'it'}, {'type': 'literal', 'value': 'Taj Mahal', 'lang': 'nl'}, {'type': 'literal', 'value': 'Taj Mahal', 'lang': 'de'}, {'type': 'literal', 'value': 'Tadź Mahal', 'lang': 'pl'}, {'type': 'literal', 'value': 'Taj Mahal', 'lang': 'pt'}, {'type': 'literal', 'value': 'タージ・マハル', 'lang': 'ja'}, {'type': 'literal', 'value': 'Taj Mahal', 'lang': 'es'}, {'type': 'literal', 'value': 'Taj Mahal', 'lang': 'en'}, {'type': 'literal', 'value': '泰姬陵', 'lang': 'zh'}], 'http://www.w3.org/2000/01/rdf-schema#comment': [{'type': 'literal', 'value': "Le Tāj Mahal (en devanagari : ताजमहल ; en persan : تاج محل) qui signifie « le palais de la couronne » en persan, est situé à Āgrā, au bord de la rivière Yamunâ, dans l'État de l'Uttar Pradesh, en Inde. Le Taj Mahal est considéré comme un joyau de l'architecture moghole, un style qui combine des éléments architecturaux des architectures islamique, iranienne, ottomane et indienne. La construction commence en 1632 et en grande partie achevée en 1643. Il est considéré que l'architecte principal fut Ustad Ahmad Lahauri de Lahore.", 'lang': 'fr'}, {'type': 'literal', 'value': "泰姬陵（印地语：ताज महल，烏爾都語：تاج محل\u200e），是位于印度北方邦阿格拉的一座用白色大理石建造的陵墓，是印度知名度最高的古迹之一。它是莫卧儿王朝第5代皇帝沙贾汗为了纪念他的第三任妻子已故皇后姬蔓·芭奴而興建的陵墓，竣工于1654年。泰姬陵被广泛认为是“印度穆斯林艺术的珍宝和世界遗产中被广泛赞美的杰作之一”。 泰姬陵被认为是莫卧儿建筑的最精美的例子，结合了印度建筑和波斯建筑的风格。 1983年，泰姬陵被列为联合国教科文组织世界遗产。虽然白色大理石圆顶陵墓是泰姬陵最让人熟悉的部分，但整个泰姬陵是一个拥有多处建筑的复杂建筑群。泰姬陵大约在1632年开始建造，在1653年左右完工，使用了成千上万的工匠。泰姬陵的建造被委托给一个建筑师团队，并由皇帝总监，团队中包括有Abd ul-Karim Ma'mur Khan，Makramat Khan和乌斯塔德.艾哈迈德.拉合里。波斯建筑师拉合里一般被认为是首席设计师。", 'lang': 'zh'}, {'type': 'literal', 'value': 'O Taj Mahal (em hindi ताज महल, persa تاج محل) é um mausoléu situado em Agra, na Índia, sendo o mais conhecido dos monumentos do país. Encontra-se classificado pela UNESCO como Patrimônio da Humanidade. Foi recentemente anunciado como uma das Novas Sete Maravilhas do Mundo em uma celebração em Lisboa no dia 7 de Julho de 2007. Supõe-se que o imperador pretendesse fazer uma réplica do Taj Mahal original na outra margem do rio, em mármore preto, mas acabou morto antes do início das obras por um de seus filhos.', 'lang': 'pt'}, {'type': 'literal', 'value': "De Taj Mahal (Perzisch: تاخ محل ('paleis van de kroon'), Urdu: تاج محل, Hindi: ताज महल; uitgesproken als tadzj mèhèl) is een imposant, wit marmeren mausoleum in Agra (Uttar Pradesh). Shah Jahan, de vijfde heerser van het Mogolrijk, liet het grafmonument tussen 1632 en 1648 bouwen als laatste rustplaats voor zijn geliefde echtgenote Mumtaz Mahal, die in 1631 in het kraambed was overleden. Na de dood van Shah Jahan werden ook diens resten bijgezet in de tombe.", 'lang': 'nl'}, {'type': 'literal', 'value': 'Der Taj Mahal (deutsch: Tadsch Mahal, Perso-Arabisch: تاج محل, DMG tāǧ maḥall / Devanagari: ताजमहल tāj mahal, „Krone des Ortes“ bzw. „Kronen-Palast“) ist ein 58 Meter hohes und 56 Meter breites Mausoleum (Grabgebäude), das in Agra im indischen Bundesstaat Uttar Pradesh auf einer 100 × 100 Meter großen Marmorplattform in der Form einer Moschee errichtet wurde. Der Großmogul Shah Jahan ließ ihn zum Gedenken an seine im Jahre 1631 verstorbene große Liebe Mumtaz Mahal (Arjumand Bano Begum) erbauen.', 'lang': 'de'}, {'type': 'literal', 'value': 'The Taj Mahal (/ˌtɑːdʒ məˈhɑːl/, more often /ˈtɑːʒ/; (Persian and Urdu: تاج محل meaning Crown of Palaces) is an ivory-white marble mausoleum on the south bank of the Yamuna river in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor, Shah Jahan (reigned 1628–1658), to house the tomb of his favourite wife, Mumtaz Mahal. The tomb is the centrepiece of a 17-hectare (42-acre) complex, which includes a mosque and a guest house, and is set in formal gardens bounded on three sides by a crenellated wall.', 'lang': 'en'}, {'type': 'literal', 'value': 'تاج محل وبالهندي : ताज महल "تاج القصور هندية: ताज महल, من الفارسية/أردوية تاج محل "" وهو ضريح رائع الصنع، أنيق العمارة من الرخام الأبيض يوجد بأكرة بأوتار برادش بالهند. شيده الملك شاه جهان الإمبراطور المغولي (1630 – 1648) ليضم رفات زوجه أرجمند بانوبيگم " الزوجة الثالثة وتعرف بممتاز محل والتي تدله في عشقها تخليدا لذكراها. وكلمة تاج محل محرفة عن الاسم الذي كانت تحمله الأميرة، وهو ممتاز محل. وضع تصميمه المهندس المعروف بالأستاذ عيسى شیرازی وامان الله خان شیرازی. شيد بالمرمر الأبيض المجلوب من جدهابور على مصطبة يغطى سطحها بالمرمر الأبيض، وأقيمت عند كل زاوية من زوايا المصطبة مئذنة متناسقة الأجزاء ارتفاعها 37 م. يحيط بدائر كل منها ثلاث شرفات، وفي وسط المصطبة يرتفع الضريح في شكل رباعي، وتشغل الجزء الأوسط من البناية القبة الرئيسية، وقطرها 17 م. وارتفاعها 22.5 م. ولكل من واجهات البناية الأربع مدخل عال', 'lang': 'ar'}, {'type': 'literal', 'value': 'Тадж-Маха́л (хинди ताज महल, урду تاج محل, англ. Taj Mahal) — мавзолей-мечеть, находящийся в Агре, Индия, на берегу реки Джамна (архитекторы, вероятно, Устад-Иса и др.). Построен по приказу потомка Тамерлана — падишаха Империи Великих Моголов Шах-Джахана в память о жене Мумтаз-Махал, умершей при родах четырнадцатого ребёнка (позже здесь был похоронен и сам Шах-Джахан).', 'lang': 'ru'}, {'type': 'literal', 'value': 'Tadź Mahal (hindi: ताज महल urdu: تاج محل) – indyjskie mauzoleum wzniesione przez Szahdżahana z dynastii Wielkich Mogołów, na pamiątkę przedwcześnie zmarłej, ukochanej żony Mumtaz Mahal. Obiekt bywa nazywany świątynią miłości.', 'lang': 'pl'}, {'type': 'literal', 'value': "Il template {{Coord}} ha riscontrato degli errori (istruzioni):Modulo:Wikidata:398: attempt to index field 'wikibase' (a nil value) Il Taj Mahal (in urdu: تاج محل; in hindi: ताज महल; IPA: ˈtɑːdʒ_məˈhɑːl), situato ad Agra, nell'India settentrionale (stato di Uttar Pradesh), è un mausoleo fatto costruire nel 1632 dall'imperatore moghul Shah Jahan in memoria della moglie preferita Arjumand Banu Begum, meglio conosciuta come Mumtaz Mahal. Nonostante vi siano molti dubbi riguardo al nome dell'architetto che lo progettò, generalmente si tende a considerare Ustad Ahmad Lahauri il padre dell'opera.", 'lang': 'it'}, {'type': 'literal', 'value': 'タージ・マハル（ヒンディー語: ताज महल, ウルドゥー語: تاج محل\u200e, 英語: Taj Mahal）は、インド北部アーグラにある、ムガル帝国第5代皇帝シャー・ジャハーンが、1631年に死去した愛妃ムムターズ・マハルのため建設した総大理石の墓廟。インド・イスラーム文化の代表的建築である。', 'lang': 'ja'}, {'type': 'literal', 'value': "El Taj Mahal (hindi: ताज महल Tāj Mahal, urdu: تاج محل Tāŷ Mahal 'Corona de los Palacios'; /tɑːʒ mə'hɑl/) es un complejo de edificios construido entre 1631 y 1648 en la ciudad de Agra, estado de Uttar Pradesh (India), a orillas del río Yamuna, por el emperador musulmán Shah Jahan de la dinastía mogola. El imponente conjunto se erigió en honor de su esposa favorita, Arjumand Bano Begum —más conocida como Mumtaz Mahal— que murió en el parto de su decimocuarta hija. Se estima que su construcción necesitó el esfuerzo de unos 20 000 obreros.", 'lang': 'es'}], 'http://www.w3.org/2002/07/owl#sameAs': [{'type': 'uri', 'value': 'http://es.dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://pl.dbpedia.org/resource/Tadź_Mahal'}, {'type': 'uri', 'value': 'http://ko.dbpedia.org/resource/타지마할'}, {'type': 'uri', 'value': 'http://sw.cyc.com/concept/Mx4rlJT8aJaUSP-bgmqljaE6Pg'}, {'type': 'uri', 'value': 'http://pt.dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://ja.dbpedia.org/resource/タージ・マハル'}, {'type': 'uri', 'value': 'http://d-nb.info/gnd/4086583-6'}, {'type': 'uri', 'value': 'http://it.dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://fr.dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q9141'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://nl.dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://eu.dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://cs.dbpedia.org/resource/Tádž_Mahal'}, {'type': 'uri', 'value': 'http://rdf.freebase.com/ns/m.0l8cb'}, {'type': 'uri', 'value': 'http://wikidata.dbpedia.org/resource/Q9141'}, {'type': 'uri', 'value': 'http://yago-knowledge.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://sws.geonames.org/1255231/'}, {'type': 'uri', 'value': 'http://de.dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://id.dbpedia.org/resource/Taj_Mahal'}, {'type': 'uri', 'value': 'http://el.dbpedia.org/resource/Τατζ_Μαχάλ'}], 'http://purl.org/dc/terms/subject': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Iranian_architecture'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:World_Heritage_Sites_in_India'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Domes'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Mughal_architecture'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Islamic_architecture'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Marble_buildings'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Buildings_and_structures_completed_in_1654'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Buildings_and_structures_in_Agra'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Taj_Mahal'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:1654_establishments_in_the_Mughal_Empire'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Tourist_attractions_in_Agra'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Mughal_funerary_gardens_in_India'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Tourism_in_India'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Persian_gardens_in_India'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Category:Mausoleums_in_Uttar_Pradesh'}], 'http://xmlns.com/foaf/0.1/name': [{'type': 'literal', 'value': 'Taj Mahal', 'lang': 'en'}, {'type': 'literal', 'value': 'تاج محل', 'lang': 'en'}], 'http://xmlns.com/foaf/0.1/homepage': [{'type': 'uri', 'value': 'http://www.tajmahal.gov.in/'}], 'http://xmlns.com/foaf/0.1/depiction': [{'type': 'uri', 'value': 'http://commons.wikimedia.org/wiki/Special:FilePath/Taj_Mahal_N-UP-A28-a.jpg'}], 'http://xmlns.com/foaf/0.1/isPrimaryTopicOf': [{'type': 'uri', 'value': 'http://en.wikipedia.org/wiki/Taj_Mahal'}], 'http://dbpedia.org/property/coordDisplay': [{'type': 'literal', 'value': 'inline, title', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/latDegrees': [{'type': 'literal', 'value': 27, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/latDirection': [{'type': 'literal', 'value': 'N', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/latMinutes': [{'type': 'literal', 'value': 10, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/latSeconds': [{'type': 'literal', 'value': 30, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/locmapin': [{'type': 'literal', 'value': 'India', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/longDegrees': [{'type': 'literal', 'value': 78, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/longDirection': [{'type': 'literal', 'value': 'E', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/longMinutes': [{'type': 'literal', 'value': 2, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/longSeconds': [{'type': 'literal', 'value': 31, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/built': [{'type': 'literal', 'value': 1632, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/nativeLanguage': [{'type': 'literal', 'value': 'ur', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/designation1Number': [{'type': 'literal', 'value': 252, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/designation1Free1name': [{'type': 'literal', 'value': 'State Party', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/designation1Free2value': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/List_of_World_Heritage_Sites_in_Asia'}], 'http://dbpedia.org/property/designation1Type': [{'type': 'literal', 'value': 'Cultural', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/designation1Date': [{'type': 'literal', 'value': 1983, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/designation1Free2name': [{'type': 'literal', 'value': 'Region', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/visitationNum': [{'type': 'literal', 'value': 7, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://www.w3.org/ns/prov#wasDerivedFrom': [{'type': 'uri', 'value': 'http://en.wikipedia.org/wiki/Taj_Mahal?oldid=744758466'}], 'http://dbpedia.org/ontology/wikiPageExternalLink': [{'type': 'uri', 'value': 'http://www.tajmahal.gov.in/'}, {'type': 'uri', 'value': 'http://asi.nic.in/asi_monu_whs_agratajmahal.asp'}, {'type': 'uri', 'value': 'http://whc.unesco.org/en/list/252'}], 'http://dbpedia.org/property/caption': [{'type': 'literal', 'value': 'Artistic depiction of Mumtaz Mahal', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}, {'type': 'literal', 'value': '"Shah jahan on a globe" from the Smithsonian Institution', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/alt': [{'type': 'literal', 'value': 'Shah Jahan', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}, {'type': 'literal', 'value': 'Mumtaz Mahal', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/image': [{'type': 'literal', 'value': 'Mumtaz Mahal.jpg', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}, {'type': 'literal', 'value': 'Shahjahan on globe, mid 17th century.jpg', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/designation1Free1value': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/India'}], 'http://dbpedia.org/ontology/location': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/India'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Uttar_Pradesh'}, {'type': 'uri', 'value': 'http://dbpedia.org/resource/Agra'}], 'http://dbpedia.org/property/header': [{'type': 'literal', 'value': 'Shah Jahan and Mumtaz Mahal', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/ontology/abstract': [{'type': 'literal', 'value': 'تاج محل وبالهندي : ताज महल "تاج القصور هندية: ताज महल, من الفارسية/أردوية تاج محل "" وهو ضريح رائع الصنع، أنيق العمارة من الرخام الأبيض يوجد بأكرة بأوتار برادش بالهند. شيده الملك شاه جهان الإمبراطور المغولي (1630 – 1648) ليضم رفات زوجه أرجمند بانوبيگم " الزوجة الثالثة وتعرف بممتاز محل والتي تدله في عشقها تخليدا لذكراها. وكلمة تاج محل محرفة عن الاسم الذي كانت تحمله الأميرة، وهو ممتاز محل. وضع تصميمه المهندس المعروف بالأستاذ عيسى شیرازی وامان الله خان شیرازی. شيد بالمرمر الأبيض المجلوب من جدهابور على مصطبة يغطى سطحها بالمرمر الأبيض، وأقيمت عند كل زاوية من زوايا المصطبة مئذنة متناسقة الأجزاء ارتفاعها 37 م. يحيط بدائر كل منها ثلاث شرفات، وفي وسط المصطبة يرتفع الضريح في شكل رباعي، وتشغل الجزء الأوسط من البناية القبة الرئيسية، وقطرها 17 م. وارتفاعها 22.5 م. ولكل من واجهات البناية الأربع مدخل عال مغطى بعقد، وتحت القبة الكبرى التي تعلو وسط البناية ضريح الأميرة، وإلى جانبه ضريح زوجها، وكلاهما مزخرف بالنقوش الكتابية. ويعتبر من أجمل نماذج طراز العمارة الإسلامي حيث يعرف على نطاق واسع بأنه "جوهرة الفن الإسلامي في الهند وإحدى الروائع الخالدة في العالم". ويعتبر تاج محل من قبل العديد من أرقى الأمثلة على العمارة المغولية، وهو أسلوب يجمع بين الطراز المعماري الفارسي والتركي والعثماني والهندي . في عام 1983 م، أصبح تاج محل من مواقع التراث العالمي لليونسكو. في حين أن قبة الرخام البيضاء هي الجزء الأكثر شهرة في تاج محل، وهو في الواقع مجمع متكامل من الهياكل، بدأ بناءه حوالي عام 1632 م وتم الانتهاء منه في حوالي عام 1653، وعمل فيه آلاف الحرفيين. وكان بناء تاج محل موكل إلى نخبة من المهندسين المعماريين تحت إشراف إمبراطوري، بما فيهم عبد الكريم معمور خان، مكرمات خان وأستاذ أحمد لاهوري  وهو يعتبر المصمم الرئيسي.', 'lang': 'ar'}, {'type': 'literal', 'value': 'O Taj Mahal (em hindi ताज महल, persa تاج محل) é um mausoléu situado em Agra, na Índia, sendo o mais conhecido dos monumentos do país. Encontra-se classificado pela UNESCO como Patrimônio da Humanidade. Foi recentemente anunciado como uma das Novas Sete Maravilhas do Mundo em uma celebração em Lisboa no dia 7 de Julho de 2007. A obra foi feita entre 1632 e 1653 com a força de cerca de 20 mil homens, trazidos de várias cidades do Oriente, para trabalhar no suntuoso monumento de mármore branco que o imperador Shah Jahan mandou construir em memória de sua esposa favorita, Aryumand Banu Begam, a quem chamava de Mumtaz Mahal ("A joia do palácio"). Ela morreu após dar à luz o 14º filho, tendo o Taj Mahal sido construído sobre seu túmulo, junto ao rio Yamuna. Assim, o Taj Mahal é também conhecido como a maior prova de amor do mundo, contendo inscrições retiradas do Corão. É incrustado com pedras semipreciosas, tais como o lápis-lazúli entre outras. A sua cúpula é costurada com fios de ouro. O edifício é flanqueado por duas mesquitas e cercado por quatro minaretes. Supõe-se que o imperador pretendesse fazer uma réplica do Taj Mahal original na outra margem do rio, em mármore preto, mas acabou morto antes do início das obras por um de seus filhos.', 'lang': 'pt'}, {'type': 'literal', 'value': 'タージ・マハル（ヒンディー語: ताज महल, ウルドゥー語: تاج محل\u200e, 英語: Taj Mahal）は、インド北部アーグラにある、ムガル帝国第5代皇帝シャー・ジャハーンが、1631年に死去した愛妃ムムターズ・マハルのため建設した総大理石の墓廟。インド・イスラーム文化の代表的建築である。', 'lang': 'ja'}, {'type': 'literal', 'value': 'Тадж-Маха́л (хинди ताज महल, урду تاج محل, англ. Taj Mahal) — мавзолей-мечеть, находящийся в Агре, Индия, на берегу реки Джамна (архитекторы, вероятно, Устад-Иса и др.). Построен по приказу потомка Тамерлана — падишаха Империи Великих Моголов Шах-Джахана в память о жене Мумтаз-Махал, умершей при родах четырнадцатого ребёнка (позже здесь был похоронен и сам Шах-Джахан). Тадж-Махал (также «Тадж») считается лучшим примером архитектуры стиля моголов, который сочетает в себе элементы индийского, персидского и арабского архитектурных стилей. В 1983 году Тадж-Махал был назван объектом Всемирного наследия ЮНЕСКО: «жемчужиной мусульманского искусства в Индии, одним из общепризнанных шедевров наследия, которым восхищаются во всём мире». Несмотря на то, что белый мраморный купол мавзолея является наиболее известным компонентом, Тадж-Махал — это структурно интегрированный комплекс. Здание начали строить примерно в 1632 году и завершили в 1653 году, работали 20 тысяч ремесленников и мастеров. Руководство строительством Тадж-Махала было возложено на Совет архитекторов под имперским контролем, включая Дешенов-Ану, Макрамат Хана и Устад Ахмад Лахаури. Главным автором проекта обычно считают Лахаури. По другой версии, наиболее популярной среди гидов Тадж Махала, одним из главных архитекторов был турок Иса Мухаммед Эфенди. Внутри мавзолея расположены две гробницы — шаха и его жены. На самом деле, место их захоронения находится ниже — строго под гробницами, под землей. Время строительства относится примерно к 1630—1652 годам. Тадж-Махал представляет собой пятикупольное сооружение высотой 74 м на платформе, с 4 минаретами по углам (они слегка наклонены в сторону от усыпальницы для того, чтобы в случае разрушения не повредить её), к которому примыкает сад с фонтанами и бассейном. Стены выложены из полированного полупрозрачного мрамора (привозившегося на строительство за 300 км) с инкрустацией из самоцветов. Были использованы бирюза, агат, малахит, сердолик и др. Мрамор имеет такую особенность, что при ярком дневном свете он выглядит белым, на заре розовым, а в лунную ночь — серебристым.', 'lang': 'ru'}, {'type': 'literal', 'value': "Il template {{Coord}} ha riscontrato degli errori (istruzioni):Modulo:Wikidata:398: attempt to index field 'wikibase' (a nil value) Il Taj Mahal (in urdu: تاج محل; in hindi: ताज महल; IPA: ˈtɑːdʒ_məˈhɑːl), situato ad Agra, nell'India settentrionale (stato di Uttar Pradesh), è un mausoleo fatto costruire nel 1632 dall'imperatore moghul Shah Jahan in memoria della moglie preferita Arjumand Banu Begum, meglio conosciuta come Mumtaz Mahal. Nonostante vi siano molti dubbi riguardo al nome dell'architetto che lo progettò, generalmente si tende a considerare Ustad Ahmad Lahauri il padre dell'opera. È da sempre considerata una delle più notevoli bellezze dell'architettura musulmana in India ed è tra i patrimoni dell'umanità dell'UNESCO dal 9 dicembre 1983. È stato inserito nel 2007 fra le nuove sette meraviglie del mondo.", 'lang': 'it'}, {'type': 'literal', 'value': "Le Tāj Mahal (en devanagari : ताजमहल ; en persan : تاج محل) qui signifie « le palais de la couronne » en persan, est situé à Āgrā, au bord de la rivière Yamunâ, dans l'État de l'Uttar Pradesh, en Inde. C'est un mausolée de marbre blanc construit par l'empereur moghol musulman Shâh Jahân en mémoire de son épouse Arjumand Bânu Begam, aussi connue sous le nom de Mumtaz Mahal, qui signifie en persan « la lumière du palais ». Elle meurt le 17 juin 1631 en donnant naissance à leur quatorzième enfant alors qu'elle allait à la campagne. Elle trouve une première sépulture sur place dans le jardin Zainabad à Burhanpur. La construction du mausolée commence en 1631 et est achevée dans sa plus grande partie en 1648. Son époux, mort le 31 janvier 1666, est inhumé auprès d'elle. Le Taj Mahal est considéré comme un joyau de l'architecture moghole, un style qui combine des éléments architecturaux des architectures islamique, iranienne, ottomane et indienne. La construction commence en 1632 et en grande partie achevée en 1643. Il est considéré que l'architecte principal fut Ustad Ahmad Lahauri de Lahore.", 'lang': 'fr'}, {'type': 'literal', 'value': "El Taj Mahal (hindi: ताज महल Tāj Mahal, urdu: تاج محل Tāŷ Mahal 'Corona de los Palacios'; /tɑːʒ mə'hɑl/) es un complejo de edificios construido entre 1631 y 1648 en la ciudad de Agra, estado de Uttar Pradesh (India), a orillas del río Yamuna, por el emperador musulmán Shah Jahan de la dinastía mogola. El imponente conjunto se erigió en honor de su esposa favorita, Arjumand Bano Begum —más conocida como Mumtaz Mahal— que murió en el parto de su decimocuarta hija. Se estima que su construcción necesitó el esfuerzo de unos 20 000 obreros. El Taj Mahal es considerado el más bello ejemplo de arquitectura mogola, estilo que combina elementos de las arquitecturas islámica, persa, india e incluso turca. Este monumento ha logrado especial notoriedad por el carácter romántico de su inspiración. Aunque el mausoleo cubierto por la cúpula de mármol blanco es la parte más conocida, el Taj Mahal es un conjunto de edificios integrados. El monumento es un importante destino turístico de la India. En 1983, fue reconocido por la Unesco como Patrimonio de la Humanidad, y nombrado una de Las Nuevas Siete Maravillas del Mundo Moderno.", 'lang': 'es'}, {'type': 'literal', 'value': 'The Taj Mahal (/ˌtɑːdʒ məˈhɑːl/, more often /ˈtɑːʒ/; (Persian and Urdu: تاج محل meaning Crown of Palaces) is an ivory-white marble mausoleum on the south bank of the Yamuna river in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor, Shah Jahan (reigned 1628–1658), to house the tomb of his favourite wife, Mumtaz Mahal. The tomb is the centrepiece of a 17-hectare (42-acre) complex, which includes a mosque and a guest house, and is set in formal gardens bounded on three sides by a crenellated wall. Construction of the mausoleum was essentially completed in 1643 but work continued on other phases of the project for another 10 years. The Taj Mahal complex is believed to have been completed in its entirety in 1653 at a cost estimated at the time to be around 32 million rupees, which in 2015 would be approximately 52.8 billion rupees (US$827 million). The construction project employed some 20,000 artisans under the guidance of a board of architects led by the court architect to the emperor, Ustad Ahmad Lahauri. The Taj Mahal was designated as a UNESCO World Heritage Site in 1983 for being "the jewel of Muslim art in India and one of the universally admired masterpieces of the world\'s heritage". Described by Nobel laureate Rabindranath Tagore as "the tear-drop on the cheek of time", it is regarded by many as the best example of Mughal architecture and a symbol of India\'s rich history. The Taj Mahal attracts 7–8 million visitors a year. In 2007, it was declared a winner of the New7Wonders of the World (2000–2007) initiative.', 'lang': 'en'}, {'type': 'literal', 'value': 'Der Taj Mahal (deutsch: Tadsch Mahal, Perso-Arabisch: تاج محل, DMG tāǧ maḥall / Devanagari: ताजमहल tāj mahal, „Krone des Ortes“ bzw. „Kronen-Palast“) ist ein 58 Meter hohes und 56 Meter breites Mausoleum (Grabgebäude), das in Agra im indischen Bundesstaat Uttar Pradesh auf einer 100 × 100 Meter großen Marmorplattform in der Form einer Moschee errichtet wurde. Der Großmogul Shah Jahan ließ ihn zum Gedenken an seine im Jahre 1631 verstorbene große Liebe Mumtaz Mahal (Arjumand Bano Begum) erbauen.', 'lang': 'de'}, {'type': 'literal', 'value': 'Tadź Mahal (hindi: ताज महल urdu: تاج محل) – indyjskie mauzoleum wzniesione przez Szahdżahana z dynastii Wielkich Mogołów, na pamiątkę przedwcześnie zmarłej, ukochanej żony Mumtaz Mahal. Obiekt bywa nazywany świątynią miłości.', 'lang': 'pl'}, {'type': 'literal', 'value': "De Taj Mahal (Perzisch: تاخ محل ('paleis van de kroon'), Urdu: تاج محل, Hindi: ताज महल; uitgesproken als tadzj mèhèl) is een imposant, wit marmeren mausoleum in Agra (Uttar Pradesh). Shah Jahan, de vijfde heerser van het Mogolrijk, liet het grafmonument tussen 1632 en 1648 bouwen als laatste rustplaats voor zijn geliefde echtgenote Mumtaz Mahal, die in 1631 in het kraambed was overleden. Na de dood van Shah Jahan werden ook diens resten bijgezet in de tombe. De Mogoldynastie had de gewoonte om voor haar leden grafmonumenten in symmetrisch aangelegde tuinen te bouwen. Tuinen staan in de islamitische traditie symbool voor het paradijs en de Mogols poogden voor hun overledenen een hemelse woonplaats op aarde te scheppen. De grootschaligheid en esthetische verfijning van deze bouwwerken diende tevens de luister van hun heerschappij te onderstrepen. Een eerste hoogtepunt in deze traditie was Humayuns tombe in Delhi, in de jaren 1560 gebouwd door Akbar. De Taj Mahal staat niet zoals gebruikelijk in het midden van de tuin, maar op een verhoogd platform aan de oever van de Yamuna-rivier in Agra en domineert zo de wijde omgeving. Vier vrijstaande minaretten bezetten de hoeken van het platform en geven het bouwwerk een driedimensionale referentie. De Taj Mahal wordt geflankeerd door twee identieke - in contrasterend rood zandsteen opgetrokken - gebouwen, de moskee en het gastenverblijf. Tussen het mausoleum en de hoofdpoort van het complex ligt de tuin, die door kanalen in vier gelijke perken verdeeld is volgens het Perzische chahar bagh-patroon. Het mausoleum wordt geroemd om de volmaakt uitgevoerde symmetrie, de verfijnde decoraties in de vorm van kalligrafieën uit de Koran, de marmeren reliëfs en het ingelegde steenwerk en niet op de laatste plaats vanwege het subtiele lichtspel, dat het gebouw steeds een ander aanzien geeft. Shah Jahan slaagde in zijn ambitie om een monument voor eeuwen neer te zetten. De Taj Mahal is een van de meest herkenbare gebouwen ter wereld en een symbool van India. In 2007 werd de Taj Mahal verkozen tot een van de zeven nieuwe wereldwonderen. Het gebouw wordt jaarlijks door miljoenen bezoekers bezocht. Voor velen van hen is het mausoleum vooral een romantische ode aan de liefde.", 'lang': 'nl'}, {'type': 'literal', 'value': "泰姬陵（印地语：ताज महल，烏爾都語：تاج محل\u200e），是位于印度北方邦阿格拉的一座用白色大理石建造的陵墓，是印度知名度最高的古迹之一。它是莫卧儿王朝第5代皇帝沙贾汗为了纪念他的第三任妻子已故皇后姬蔓·芭奴而興建的陵墓，竣工于1654年。泰姬陵被广泛认为是“印度穆斯林艺术的珍宝和世界遗产中被广泛赞美的杰作之一”。 泰姬陵被认为是莫卧儿建筑的最精美的例子，结合了印度建筑和波斯建筑的风格。 1983年，泰姬陵被列为联合国教科文组织世界遗产。虽然白色大理石圆顶陵墓是泰姬陵最让人熟悉的部分，但整个泰姬陵是一个拥有多处建筑的复杂建筑群。泰姬陵大约在1632年开始建造，在1653年左右完工，使用了成千上万的工匠。泰姬陵的建造被委托给一个建筑师团队，并由皇帝总监，团队中包括有Abd ul-Karim Ma'mur Khan，Makramat Khan和乌斯塔德.艾哈迈德.拉合里。波斯建筑师拉合里一般被认为是首席设计师。", 'lang': 'zh'}], 'http://dbpedia.org/ontology/thumbnail': [{'type': 'uri', 'value': 'http://commons.wikimedia.org/wiki/Special:FilePath/Taj_Mahal_N-UP-A28-a.jpg?width=300'}], 'http://dbpedia.org/ontology/wikiPageRevisionID': [{'type': 'literal', 'value': 744758466, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/ontology/wikiPageID': [{'type': 'literal', 'value': 82976, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/wordnet_type': [{'type': 'uri', 'value': 'http://www.w3.org/2006/03/wn/wn20/instances/synset-monument-noun-2'}], 'http://dbpedia.org/property/architecture': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Mughal_architecture'}], 'http://dbpedia.org/property/visitationYear': [{'type': 'literal', 'value': 2014, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://purl.org/linguistics/gold/hypernym': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Mausoleum'}], 'http://dbpedia.org/property/mapCaption': [{'type': 'literal', 'value': 'Location of Agra within India', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/width': [{'type': 'literal', 'value': 200, 'datatype': 'http://www.w3.org/2001/XMLSchema#integer'}], 'http://dbpedia.org/property/direction': [{'type': 'literal', 'value': 'vertical', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}], 'http://dbpedia.org/property/architect': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Ustad_Ahmad_Lahauri'}], 'http://dbpedia.org/property/designation': [{'type': 'literal', 'value': 'WHS', 'datatype': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#langString'}]}, 'http://dbpedia.org/resource/Taj_Mahal,_Agra': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}, 'http://dbpedia.org/resource/Taj_Mahaj': {'http://dbpedia.org/ontology/wikiPageRedirects': [{'type': 'uri', 'value': 'http://dbpedia.org/resource/Taj_Mahal'}]}}"


l = getUrlSet(string1)
for i in l:
    print(i)