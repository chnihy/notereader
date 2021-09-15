#! python
# templates
from copy import copy


templates = { 
	"Blank Template": {
				"gridmaker":{
					"beats": "",
					"beat_type":"",
					"a":"",
					"b":"",
					"select_grid":"",
					"reversing":"",
					"octaves":""
				},
				"a_pattern_mp_measure_index":{
					"chunk_key":"",
					"noteRepeats":"",
					"root":"",
					"scaletype":"",
					"gpm":True,
					"scale_descend":"",
					"offset":""
				},
				"b_pattern_mp_measure_index":{
					"chunk_key":"",
					"noteRepeats":"",
					"root":"",
					"scaletype":"",
					"gpm":True,
					"scale_descend":"",
					"offset":""
				}	
			},

	"1234s vs. 3rds": {
				"time_and_key":{
					"beats":"4",
					"beat_type":"4",
					"root":"c",
					"scaletype":"major",
					"octaves":4,
				},
				"gridmaker":{
					"beats": "4",
					"beat_type":"4",
					"a":"16",
					"b":"8",
					"select_grid":"1",
					"reversing":False,
				},
				"a_key_pattern_index":{
					"chunk_key":["one","two","three","four"],
					"noteRepeats":True,
					"root":"c",
					"scaletype":"major",
					"gpm":True,
					"scale_descend":True,
					"offset":"default",
					"beats":4
				},
				"b_key_pattern_index":{
					"chunk_key":["one","three"],
					"noteRepeats":True,
					"root":"c",
					"scaletype":"major",
					"gpm":True,
					"scale_descend":True,
					"offset":"default",
					"beats":4
				}
			},
	

	"1234s vs. 3rds stacking": { 
				"time_and_key":{
					"beats":"4",
					"beat_type":"4",
					"root":"c",
					"scaletype":"major",
					"octaves":4
				},
				"gridmaker":{
					"beats": "4",
					"beat_type":"4",
					"a":"16",
					"b":"8",
					"select_grid":"2",
					"reversing":False,
				},
				"a_key_pattern_index":{
					"chunk_key":["one","two","three","four"],
					"noteRepeats":True,
					"root":"c",
					"scaletype":"major",
					"gpm":True,
					"scale_descend":True,
					"offset":"default",
					"beats":4
				},
				"b_key_pattern_index":{
					"chunk_key":["one","three"],
					"noteRepeats":True,
					"root":"c",
					"scaletype":"major",
					"gpm":True,
					"scale_descend":True,
					"offset":"default",
					"beats":4
				}
			}


	}

temp_templates = copy(templates)