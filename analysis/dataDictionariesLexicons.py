from bigDictionariesLexicons import * 
from bigDictionariesAdjectives import *
from bigDictionariesOther import *
from bigDictionariesInquirer import *
from collections import OrderedDict
from polesConstructs import *
from testData import *

LexiconsEnsembl = [harvardGeneralInquirer3623,WEAT1, vaderLexicon7062,NRCEmotionLexicon5555,opinionLexicon6786,afinnLexicon2477,
        positiveNegativeAdjetives762,positiveNegativeAdjetives197,happySadAdjectives122,niceMeanAdjetives228,intelligentDullAdjetives75,
        inquirerViceVirtue1277,inquirerHostileAffiliation1176,inquirerPowerConflictCooperation294,inquirerEnlightenmentLossGain151,
        inquirerTransactionLossGain197,inquirerAffectNegativePositive261
        ]

dataDict={

    '0-1': {
        'name': 'bipolar  Occupations',
        'constructPole1' : maleConstruct,
        'constructPole2' : femaleConstruct,
        'RealDataLexicons' : [percentageOccupationFemale]
    },
    
    '0-2': {
        'name': 'bipolar  GDP per capita',
        'constructPole1' : poorCountryConstruct,
        'constructPole2' : richCountryConstruct,
        'RealDataLexicons' : [countriesToGdpDictionary],
    },    
    
    '0-3': {
        'name': 'bipolar Car Brand prices',
        'constructPole1' : cheapCarsConstruct,
        'constructPole2' : expensiveCarsConstruct,
        'RealDataLexicons' : [carPrices],
    },    

  
    '0-4': {
        'name': 'bipolar  Voting Behavior by Demographic Group',
        'constructPole1' : conservativesConstruct,
        'constructPole2' : liberalsConstruct,        
        'RealDataLexicons' : [voteByEthnicity],
    }, 
    
    '0-5': {
        'name': 'bipolar  Voting Behavior by Profession', #http://verdantlabs.com/politics_of_professions/
        'constructPole1' : conservativesConstruct,
        'constructPole2' : liberalsConstruct,        
        'RealDataLexicons' : [votingByProfession],
    },


    '0-6': {
        'name': 'Death & Life',
        'constructPole1' : deathConstruct,
        'constructPole2' : lifeConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
        'axisName' : "Death to Life Axis",
    },		
        
    
    '0-7': {
        'name': 'Disease & Health',
        'constructPole1' : diseaseConstruct,
        'constructPole2' : healthConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
        'axisName' : "Disease to Health Axis",
    },

    '0-8': {
        'name': 'Dictatorship & Democracy',
        'constructPole1' : dictatorshipConstruct,
        'constructPole2' : democracyConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
        'axisName' : "Dictatorship to Democracy Axis",
    },    
	
    '0-9': {
        'name': 'Malevolent & Respectable Figures',
        'constructPole1' : evilPeopleConstruct,
        'constructPole2' : goodPeopleConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
        'axisName' : "Malevolent to Respectable Axis",
    },    
    
    

    '1-1': {
        'name': 'gender general',
        'constructPole1' : maleConstruct,
        'constructPole2' : femaleConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },  

    '1-2': {
        'name': 'gender family roles',
        'constructPole1' : maleFamilyConstruct,
        'constructPole2' : femaleFamilyConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },
	
    '1-3': {
        'name': 'gender and young age',
        'constructPole1' : boysConstruct,
        'constructPole2' : girlsConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    }, 
	
    '1-4': {
        'name': 'gender masculinity and femininity',
        'constructPole1' : masculinityConstruct,
        'constructPole2' : femininityConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },  
	
    '1-5': {
        'name': 'gender and popular given names ',
        'constructPole1' : male200NamesConstruct,
        'constructPole2' : female200NamesConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },  
    
    '2-1': {
        'name': 'Whites and African-Americans',
        'constructPole1' : whiteConstruct,
        'constructPole2' : blackConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },    

    '2-2': {
        'name': 'popular given names among Whites and African Americans',
        'constructPole1' : europeanNamesConstruct,
        'constructPole2' : africanAmericanNamesConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    }, 	

    '2-3': {
        'name': 'Whites and Hispanics',
        'constructPole1' : whiteConstruct,
        'constructPole2' : hispanicConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },     
	
    '2-4': {
        'name': 'Whites and Asians',
        'constructPole1' : whiteConstruct,
        'constructPole2' : asianConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },     
	
    '3-1': {
        'name': 'sexual orientation',
        'constructPole1' : heterosexualityConstruct,
        'constructPole2' : homosexualityConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },	
	
    '4-1': {
        'name': 'religiosity',
        'constructPole1' : religiousConstruct,
        'constructPole2' : nonreligiousConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },	

    '4-2': {
        'name': 'religion Christianity and Islam',
        'constructPole1' : christianityConstruct,
        'constructPole2' : islamConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },	
	
    '5-1': {
        'name': 'age',
        'constructPole1' : elderlyConstruct,
        'constructPole2' : youthConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },	
	
    '6-1': {
        'name': 'socioeconomic status',
        'constructPole1' : middleClassConstruc,
        'constructPole2' : upperClassConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },	
	
    '7-1': {
        'name': 'physical appearance',
        'constructPole1' : plainLookingConstruct,
        'constructPole2' : goodLookingConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },	

    '8-1': {
        'name': 'personal ideology',
        'constructPole1' : conservativesConstruct,
        'constructPole2' : liberalsConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },     

    '8-2': {
        'name': 'party affiliation and political parties',
        'constructPole1' : republicansConstruct,
        'constructPole2' : democratsConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },    

    '8-3': {
        'name': 'U.S. presidents',
        'constructPole1' : republicanPresidents,
        'constructPole2' : democratPresidents,
        'RealDataLexicons' : LexiconsEnsembl,
    },	

    '8-4': {
        'name': 'ideologies abstract',
        'constructPole1' : conservatismConstruct,
        'constructPole2' : liberalismConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },	
    
    '8-5': {
        'name': 'influential conservatives and liberals',
        'constructPole1' : influentialConservativesConstruct,
        'constructPole2' : influentialLiberalsConstruct,
        'RealDataLexicons' : LexiconsEnsembl,
    },	
}


