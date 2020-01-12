from bigDictionariesLexicons import * 
from bigDictionariesAdjectives import *
from bigDictionariesOther import *
from bigDictionariesInquirer import *
from collections import OrderedDict


deathConstruct = ['death','dying','decease']
lifeConstruct = ['alive','life','living']

poorCountryConstruct = ['poor','poverty','underdeveloped']
richCountryConstruct = ['wealth','rich','wealthy','prosperous','developed']

cheapCarsConstruct = ['affordable','budget','cheap','low_cost','poor','bargain','economical','inexpensive']
expensiveCarsConstruct =  ['expensive','rich','prosperous','wealthy','affluent','luxurious','wealth','lavish','upscale','pricey']

diseaseConstruct = ['disease','sick','sickness','illness']
healthConstruct = ['health','healthy','well_being']

dangerousAnimalsConstruct = ['snake','snakes','crocodile','crocodiles','spider','spiders','shark','sharks','scorpion','scorpions']
cuteAnimalsConstruct = ['puppy','puppies','kitten','kittens','bird','birds','dog','dogs','cat','cats','hamster','hamsters','duckling','ducklings','panda_bear','panda_bears','koala','koalas']

dictatorshipConstruct = ['dictatorship','dictator','dictators']
democracyConstruct = ['democracy','democratic_leader','democratic_leaders','representative_government']

#https://www.thetoptens.com/most-evil-people-in-history/
evilPeopleConstruct = ['Hitler','Stalin','Bin_Laden','Pol_Pot','Heinrich_Himmler','Saddam_Hussein','Joseph_Goebbels'] #
goodPeopleConstruct = ['Gandhi','MLK','Nelson_Mandela','Mother_Teresa','Abraham_Lincoln']


maleConstruct = ['man','men','male','males']
femaleConstruct = ['woman','women','female','females']

maleFamilyConstruct = ['father','fathers','dad','dads','son','sons','brother','brothers','husband','husbands','uncle','uncles','grandfather','grandfathers','grandson','grandsons','nephew','nephews']
femaleFamilyConstruct = ['mother','mothers','mom','moms','daughter','daughters','sister','sisters','wife','wives','aunt','aunts','grandmother','grandmothers','granddaughter','granddaughters','niece','nieces']

masculinityConstruct = ['masculine','masculinity']
femininityConstruct = ['feminine','femininity']

boysConstruct = ['boy','boys']
girlsConstruct = ['girl','girls']

#most popular names US Census http://www.galbithink.org/names/us200.htm 
male200NamesConstruct = ['Michael', 'John', 'James', 'Robert', 'David', 'William', 'Mark', 'Richard', 'Jeffrey', 'Stephen', 'Joseph', 'Thomas', 'Daniel', 'Timothy', 'Brian', 'Christop', 'Scott', 'Charles', 'Paul', 'Kenneth', 'Ronald', 'Anthony', 'Donald', 'Gregory', 'Edward', 'Gary', 'Laurence', 'Eric', 'Douglas', 'Patrick', 'Terence', 'Todd', 'Matthew', 'George', 'Keith', 'Andrew', 'Allan', 'Frank', 'Raymond', 'Shawn', 'Dennis', 'Daryl', 'Philip', 'Jerry', 'Peter', 'Lewis', 'Carl', 'Craig', 'Roger', 'Bruce', 'Tony', 'Glen', 'Rodney', 'Daren', 'Steve', 'Russell', 'Troy', 'Samuel', 'Harry', 'Gerald', 'Wayne', 'Leonard', 'Dale', 'Randall', 'Duane', 'Martin', 'Vincent', 'Bradley', 'Curtis', 'Walter', 'Barry', 'Jason', 'Dean', 'Victor', 'Jay', 'Juan', 'Derek', 'Carlos', 'Theodore', 'Roy', 'Henry', 'Arthur', 'Benjamin', 'Jack', 'Greg', 'Albert', 'Francis', 'Joel', 'Ralph', 'Ernest', 'Eugene', 'Stanley', 'Marvin', 'Howard', 'Edwin', 'Alexande', 'Brent', 'Kurt', 'Aaron', 'Nathan', 'Anton', 'Nicholas', 'Melvin', 'Reginald', 'Brett', 'Rick', 'Mitchell', 'Norman', 'Neil', 'Adam', 'Calvin', 'Jerome', 'Kirk', 'Brad', 'Clifford', 'Manuel', 'Hector', 'Earl', 'Alfred', 'Gilbert', 'Stewart', 'Lance', 'Wesley', 'Miguel', 'Kent', 'Warren', 'Andre', 'Clarence', 'Tyrone', 'Reuben', 'Bernard', 'Kyle', 'Kerry', 'Chad', 'Jorge', 'Alvin', 'Leroy', 'Gordon', 'Shane', 'Erik', 'Pedro', 'Jesus', 'Gene', 'Dave', 'Guy', 'Maurice', 'Mario', 'Lonnie', 'Leslie', 'Herbert', 'Lloyd', 'Vernon', 'Perry', 'Rafael', 'Ramon', 'Rickey', 'Wade', 'Dwight', 'Gregg', 'Ron', 'Marty', 'Travis', 'Loren', 'Joey', 'Ken', 'Timmy', 'Nelson', 'Kelvin', 'Byron', 'Doug', 'Randal', 'Oscar', 'Donnie', 'Ryan', 'Hugh', 'Raul', 'Floyd', 'Damien', 'Milton', 'Lester', 'Clinton', 'Orlando', 'Arnold', 'Jimmie', 'Jackie', 'Felix', 'Corey', 'Gerard', 'Roderick', 'Javier', 'Roland', 'Clyde', 'Ross', 'Jody', 'Clayton', 'Ferdinan', 'Herman', 'Nick', 'Julio', 'Wendell']
female200NamesConstruct = ['Elizabet', 'Mary', 'Catherin', 'Deborah', 'Susan', 'Christin', 'Ann', 'Jane', 'Karen', 'Patricia', 'Cynthia', 'Laura', 'Theresa', 'Lori', 'Linda', 'Tami', 'Caroline', 'Sandra', 'Angel', 'Julia', 'Donna', 'Sherry', 'Pamela', 'Jennifer', 'Brenda', 'Cheryl', 'Barbara', 'Sharon', 'Margaret', 'Nancy', 'Joan', 'Rebecca', 'Diane', 'Victoria', 'Denise', 'Tina', 'Amy', 'Jacqueli', 'Milicent', 'Teri', 'Dawn', 'Ellen', 'Rose', 'Rhonda', 'Paula', 'Stephani', 'Wendy', 'Dinah', 'Sheila', 'Judy', 'Lyn', 'Staci', 'Alice', 'Constanc', 'Keri', 'Sarah', 'Jill', 'Karla', 'Dara', 'Joyce', 'Georgina', 'Janice', 'Valerie', 'Shelly', 'Martha', 'Wanda', 'Monica', 'Bonnie', 'Regina', 'Jodi', 'Sonia', 'Betty', 'Gail', 'Beverly', 'Evelyn', 'Colleen', 'Gloria', 'Penelope', 'Frances', 'Lou', 'Roberta', 'Shirley', 'Tamar', 'Ruth', 'Nora', 'Maureen', 'Marci', 'Helen', 'Veronica', 'Melanie', 'Dorothy', 'Virginia', 'Melinda', 'Tonya', 'Gwen', 'Sylvia', 'Rachel', 'Holly', 'Heather', 'Yolanda', 'Heidi', 'Rita', 'Toni', 'Yvonne', 'Jamie', 'Marilyn', 'April', 'Crystal', 'Sally', 'Yvette', 'Tania', 'Phyllis', 'Charlott', 'Nicole', 'Charlene', 'Belinda', 'Janine', 'Audrey', 'Bridget', 'Marla', 'Lily', 'Shawna', 'Vanessa', 'Candice', 'Lucy', 'Juana', 'Emily', 'Doris', 'Glenda', 'Casandra', 'Felicia', 'Clara', 'Natalia', 'Melody', 'Amanda', 'Wilma', 'Grace', 'Cecilia', 'Irene', 'Rox', 'Kay', 'Vivian', 'Geri', 'Arlene', 'Doreen', 'Ramona', 'Leta', 'Tara', 'Lydia', 'Josephin', 'Lois', 'Danielle', 'Lauren', 'Ada', 'Sabina', 'Katrina', 'Berna', 'Esther', 'Chris', 'Dolores', 'Claud', 'Adriana', 'Delores', 'Edith', 'Erica', 'Samantha', 'June', 'Ginger', 'Iris', 'Mildred', 'Priscill', 'Ruby', 'Trina', 'Nina', 'Geraldin', 'Rochelle', 'Naomi', 'Gretchen', 'Beatrice', 'Irma', 'Hope', 'Lana', 'Edna', 'Dahlia', 'Tiffany', 'Mona', 'Maribel', 'Florence', 'Olga', 'Alisa', 'Camilla', 'Faith', 'Cora', 'Dora', 'Lourdes', 'Myra', 'Alma', 'Nadine', 'Celeste', 'Desiree']

whiteConstruct = ['White','Whites','White_American','White_Americans',
'white','whites','white_american','white_americans',
]
blackConstruct = ['Black','Blacks','African_American','African_Americans','Black_American','Black_Americans',
'black','blacks','african_american','african_americans','black_american','black_americans'
]

#from https://science.sciencemag.org/content/356/6334/183.full
europeanNamesConstruct = ['Adam','Chip','Harry','Josh','Roger','Alan','Frank','Ian','Justin','Ryan','Andrew','Fred','Jack','Matthew','Stephen', 
    'Brad','Greg','Jed','Paul','Todd','Brandon','Hank','Jonathan','Peter','Wilbur','Amanda','Courtney','Heather',
    'Melanie','Sara','Amber','Crystal','Katie','Meredith','Shannon','Betsy','Donna','Kristin','Nancy','Stephanie',
    'Bobbie_Sue','Ellen','Lauren','Peggy','Sue_Ellen','Colleen','Emily','Megan','Rachel','Wendy']
	
africanAmericanNamesConstruct = ['Alonzo','Jamel','Lerone','Percell','Theo','Alphonse','Jerome','Leroy','Rasaan',
'Torrance','Darnell','Lamar','Lionel','Rashaun','Tyree','Deion','Lamont','Malik','Terrence','Tyrone',
'Everol','Lavon','Marcellus','Terryl','Wardell','Aiesha','Lashelle','Nichelle','Shereen','Temeka',
'Ebony','Latisha','Shaniqua','Tameisha','Teretha','Jasmine','Latonya','Shanise','Tanisha','Tia',
'Lakisha','Latoya','Sharise','Tashika','Yolanda','Lashandra','Malika','Shavonn','Tawanda','Yvette',]

hispanicConstruct = ['Hispanic','Hispanics','Latino','Latinos','Hispanic_American','Hispanic_Americans',
					'hispanic','hispanics','latino','latinos','hispanic_american','hispanic_americans',
]
asianConstruct = ['Asian','Asians','Asian_American','Asian_Americans',
				  'asian','asians','asian_american','asian_americans',
]

heterosexualityConstruct = ['heterosexual','heterosexuals','heterosexuality']                    
homosexualityConstruct =  ['homosexual','homosexuals','gay','gays','lesbian','lesbians','lgbt','lgbtq','glbt','lgb','homosexuality']

religiousConstruct = ['Christian','Christians','Christianity','Catholic','Catholics','Catholicism',
                          'Protestant','Protestants','Protestantism','Muslim','Muslims','Moslem','Moslems','Islam',
                          'Jew','Jews','Judaism','Hindu','Hindus','Hinduism', 'Buddhist','Buddhists','Buddhism',
                          'Mormon','Mormons','Mormonism',
                          'Evangelical','Evangelicals','Evangelicalism',
						  'christian','christians','christianity','catholic','catholics','catholicism',
                          'protestant','protestants','protestantism','muslim','muslims','moslem','moslems','islam',
                          'jew','jews','judaism','hindu','hindus','hinduism', 'buddhist','buddhists','buddhism',
                          'mormon','mormons','mormonism',
                          'evangelical','evangelicals','evangelicalism',
						  ]
                          
nonreligiousConstruct = ['nonreligious','non_religiosity','secular','secularism','secularist','secularists',
                          'atheist','atheists','atheism','agnostic','agnostics','agnosticism',
                          'religionless','irreligious','irreligiosity','nonbeliever','nonbelievers','non_believer'
                         ] 

christianityConstruct = ['Christian','Christians','Christianity',
						'christian','christians','christianity'
]
islamConstruct = ['Muslim','Muslims','Islam',
				  'muslim','muslims','islam',
]

elderlyConstruct = ['elderly','elders','old','aged','aging','senior_citizen','senior_citizens','retired','old_age']
youthConstruct = ['youth','young','youngness','youthfulness','young_citizen','young_citizens']

middleClassConstruc = ['working_class', 'middle_class','blue_collar','white_collar', 'wage_earners']
upperClassConstruct = ['upper_class','affluent','rich', 'wealthy','prosperous','moneyed']

plainLookingConstruct = ['unattractive','plain_looking','homely','ugly','unappealing']
goodLookingConstruct = ['beautiful', 'handsome', 'cute', 'attractive', 'good_looking'] 

conservativesConstruct = ['conservative','conservatives','right_winger','rightwinger','right_wingers','rightwingers','right_wing','rightwing','right_leaning']
liberalsConstruct = ['liberal','liberals','progressive','progressives','left_winger','leftwinger','left_wingers','leftwingers','left_wing','leftwing','left_leaning']

republicansConstruct = ['Republican', 'Republicans','GOP','Republican_Party', 'Republican_voter', 'Republican_voters','registered_Republican','registered_Republicans',
						'republican', 'republicans','gop','republican_party', 'republican_voter', 'republican_voters','registered_republican','registered_republicans',

]
democratsConstruct = ['Democrat', 'Democrats','Democratic_Party','Democrat_voter','Democrat_voters','registered_Democrat','registered_Democrats',
					 'democrat', 'democrats','democratic_party','democrat_voter','democrat_voters','registered_democrat','registered_democrats',

]

conservatismConstruct = ['conservatism','neoconservatism','illiberalism','ultraconservatism','far_right']
liberalismConstruct = ['liberalism', 'progressivism','egalitarianism','ultraliberalism','far_left']

#US presidents 
republicanPresidents = ['Dwight_Eisenhower','Eisenhower','Richard_Nixon','Nixon','Gerald_Ford','Ronald_Reagan','Reagan',
'George_Bush','Bush','Donald_Trump','Trump'] 
democratPresidents = ['Franklin_Roosevelt','Roosevelt','Harry_Truman','Truman','John_Kennedy','Kennedy','Lyndon_Johnson','Jimmy_Carter'
'Carter','Bill_Clinton','Clinton','Barack_Obama','Obama']

#https://www.telegraph.co.uk/news/worldnews/northamerica/usa/6990965/The-most-influential-US-conservatives-20-1.html
influentialConservativesConstruct = ['Dick_Cheney','Cheney','Rush_Limbaugh','Limbaugh','Map_Drudge','Drudge','Sarah_Palin','Palin',
                      'Robert_Gates','Gates','Glenn_Beck','Beck',
                      'Roger_Ailes','Ailes','David_Petraeus','Petraeus','Paul_Ryan','Ryan','Tim_Pawlenty','Pawlenty',
                      'Mitt_Romney','Romney','George_Bush','Bush','John_Roberts','Roberts','Haley_Barbour','Barbour',
                      'Eric_Cantor','Cantor','John McCain','McCain','Mike_Pence','Pence','Bob_McDonnell','McDonnell',
                       'Newt_Gingrich','Gingrich','Mike_Huckabee','Huckabee'       
                     ]
					 
influentialLiberalsConstruct = ['Barak_Obama','Obama','Hillary_Clinton','Clinton','Nancy_Pelosi','Pelosi','Bill_Clinton','Clinton',
                      'Rahm_Emanuel','Emanuel','Al_Gore','Gore','Oprah_Winfrey','Winfrey',
                     ' Tim Geithner','Geithner','David_Axelrod','Axelrod',' Harry_Reid','Reid','Michelle_Obama','Obama',
                      'Arianna_Huffington','Huffington','Sonia_Sotomayor','Sotomayor','Denis_McDonough','McDonough',
                      'Janet_Napolitano','Napolitano','Mark_Warner','Warner','Robert_Gibbs','Gibbs',
                      'Barney_Frank','Frank','John_Kerry','Kerry','Eric_Holder','Holder'
                     ]

