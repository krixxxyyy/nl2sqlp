{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .SFNS-Semibold;\f1\fnil\fcharset0 .SFNS-Regular;\f2\fswiss\fcharset0 Helvetica;
\f3\fnil\fcharset0 .AppleSystemUIFontMonospaced-Regular;\f4\fnil\fcharset128 HiraginoSans-W5;\f5\fswiss\fcharset0 Helvetica-Bold;
\f6\froman\fcharset0 Times-Bold;\f7\froman\fcharset0 Times-Roman;\f8\froman\fcharset0 TimesNewRomanPSMT;
}
{\colortbl;\red255\green255\blue255;\red14\green14\blue14;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c6700\c6700\c6700;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs44 \cf2 Universal NL2SQLP
\f1\b0\fs28 \
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs30 \cf2 A Schema-Agnostic Natural Language to SQL Engine with Clarification Support
\f1\b0\fs28 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Overview
\f1\b0\fs28 \
\
Universal NL2SQLP is a schema-agnostic Natural Language to SQL (NL2SQL) system that converts user queries written in plain English into accurate, deterministic SQL queries.\
\
Unlike traditional NL2SQL systems that rely on hardcoded schemas or heuristic mappings, this system is designed as a multi-stage semantic pipeline with an integrated clarification mechanism to prevent silent failures and incorrect SQL generation.\
\
The system never guesses when uncertain \'97 it asks.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Key Objectives
\f1\b0\fs28 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	Convert natural language queries into valid SQL\
	\'95	Work with any database schema without code changes\
	\'95	Eliminate incorrect SQL due to ambiguity\
	\'95	Provide human-in-the-loop clarification\
	\'95	Maintain explainability and stability\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Design Philosophy
\f1\b0\fs28 \
\
The system behaves like a semantic compiler rather than a direct text-to-SQL mapper.\
\
Natural Language Query\
\uc0\u8595 \
Normalization\
\uc0\u8595 \
Logical Form Construction\
\uc0\u8595 \
Query Planning\
\uc0\u8595 \
SQL Generation\
\uc0\u8595 \
Clarification (if required)\
\uc0\u8595 \
Final SQL\
\
This architecture ensures correctness, modularity, and enterprise-grade reliability.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Key Features
\f1\b0\fs28 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	Schema-Agnostic Design\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\li260\sl324\slmult1\pardirnatural\partightenfactor0
\cf2 Works for any database by updating 
\f3 schema.json
\f1 . No hardcoding.\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	Custom Lightweight Language Model\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\li260\sl324\slmult1\pardirnatural\partightenfactor0
\cf2 Not prompt-based. Not vendor-dependent. Designed for schema reasoning and SQL intent detection.\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	Clarification-Driven Reliability\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\li260\sl324\slmult1\pardirnatural\partightenfactor0
\cf2 Ambiguous queries trigger clarification questions instead of incorrect SQL.\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	Deterministic SQL Generation\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\li260\sl324\slmult1\pardirnatural\partightenfactor0
\cf2 SQL is generated from a logical plan with validated joins and columns.\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	Explainability\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\li260\sl324\slmult1\pardirnatural\partightenfactor0
\cf2 Every query passes through explicit reasoning stages.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs30 \cf2 Project Structure\
nl2sql_app/\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  app.py                     # Streamlit UI entry point\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  main.py                    # Pipeline orchestrator\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  encoder.py                 # Semantic encoding\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  normaliser.py              # Input normalization\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  logical_form.py            # Logical representation builder\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  planner.py                 # Query planning and join inference\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  sql_generator.py           # Deterministic SQL generation\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  clarifier.py               # Ambiguity detection and clarification\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  schema_utils.py            # Schema reasoning utilities\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  lm_adapter.py              # Custom language model abstraction\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  explain.py                 # SQL explanation generator\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  schema.json                # Database schema (configurable)\

\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  universal_nl2sql_lm/        # Custom language model (structure only)\
\uc0\u9474    
\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  config.json\
\uc0\u9474    
\f4 \'84\'a5\'84\'9f\'84\'9f
\f0  tokenizer.json\
\uc0\u9474    
\f5 \uc0\u9492 \u9472 \u9472 
\f0  README.md\

\f5 \uc0\u9492 \u9472 \u9472 
\f0  .gitignore\
\
\

\fs34 Clarification Mechanism (Key Highlight)
\f1\b0\fs28 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0
\cf2 \
Traditional NL2SQL systems fail silently when queries are ambiguous.\
This system does not.\
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs30 \cf2 Example Interaction
\f1\b0\fs28 \
\
User Query\
highest salary department\
\
System (Clarification Triggered)\
Do you want the department with the highest individual salary\
or the highest average salary? (max / avg)\
\
User Response\
avg\
\
Generated SQL\
SELECT departments.name, AVG(employees.salary)\
FROM employees\
JOIN departments\
  ON employees.department_id = departments.id\
GROUP BY departments.name;\
\
Key observations:\
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	The system does not assume user intent\
	\'95	Ambiguity is resolved using a single focused clarification\
	\'95	SQL is generated only after confirmation\
	\'95	Guarantees zero silent failures\
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 System Comparison\
\

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth2000\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx2880
\clvertalc \clshdrawnil \clwWidth2840\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx5760
\clvertalc \clshdrawnil \clwWidth1600\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sa240\qc\partightenfactor0

\f6\fs24 \cf0 \expnd0\expndtw0\kerning0
Aspect\cell 
\pard\intbl\itap1\pardeftab720\sa240\qc\partightenfactor0
\cf0 Traditional NL2SQL\cell 
\pard\intbl\itap1\pardeftab720\sa240\qc\partightenfactor0
\cf0 This System\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth2000\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx2880
\clvertalc \clshdrawnil \clwWidth2840\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx5760
\clvertalc \clshdrawnil \clwWidth1600\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0

\f7\b0 \cf0 Schema dependency\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0         Hardcoded\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 Config-driven\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth2000\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx2880
\clvertalc \clshdrawnil \clwWidth2840\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx5760
\clvertalc \clshdrawnil \clwWidth1600\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 Ambiguity handling\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0        Silent failure\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 Clarification-based\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth2000\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx2880
\clvertalc \clshdrawnil \clwWidth2840\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx5760
\clvertalc \clshdrawnil \clwWidth1600\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 SQL reliability\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0         Heuristic\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 Deterministic\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth2000\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx2880
\clvertalc \clshdrawnil \clwWidth2840\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx5760
\clvertalc \clshdrawnil \clwWidth1600\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 Explainability\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0            Low\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 High\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalc \clshdrawnil \clwWidth2000\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx2880
\clvertalc \clshdrawnil \clwWidth2840\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx5760
\clvertalc \clshdrawnil \clwWidth1600\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl20 \clpadb20 \clpadr20 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 Enterprise readiness\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0         Limited\cell 
\pard\intbl\itap1\pardeftab720\sa240\partightenfactor0
\cf0 Strong\cell \lastrow\row
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 \kerning1\expnd0\expndtw0 \
Running the Application
\f1\b0\fs28 \
\
Create virtual environment (recommended):  python3 -m venv venv\
source venv/bin/activate\
\
Install dependencies:  pip install streamlit\
\
Run the app (IMPORTANT):\
Do NOT use 
\f3 \cf2 python app.py
\f1 \cf2 \
Correct command:  streamlit run app.py\
Open the URL shown in the terminal (usually http://localhost:8501)\
\

\f0\b\fs34 Adapting to a New Database
\f1\b0\fs28 \
\
To use a different database schema:\
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f8 \cf2 	1.	Update 
\f3 schema.json
\f1 \

\f8 	2.	Modify table names, columns, and data types\
\
No code changes required.\
No retraining required.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Model Weights
\f1\b0\fs28 \
\
Model weights are not included in this repository due to GitHub size constraints.\
\
To use a trained model:\
\pard\tqr\tx260\tx420\li420\fi-420\sl324\slmult1\sb240\partightenfactor0

\f8 \cf2 	1.	Download 
\f3 model.safetensors
\f1  separately\

\f8 	2.	Place it inside 
\f3 universal_nl2sql_lm/
\f1 \
\
This follows standard ML engineering practices.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Use Cases
\f1\b0\fs28 \
\pard\tqr\tx100\tx260\li260\fi-260\sl324\slmult1\sb240\partightenfactor0
\cf2 	\'95	Natural language analytics\
	\'95	Business intelligence interfaces\
	\'95	Conversational database querying\
	\'95	Academic research in NLP and databases\
	\'95	Enterprise proof-of-concept systems\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 Author Notes
\f1\b0\fs28 \
\
This project prioritizes correctness over shortcuts, stability over demos, and transparency over black-box behavior.\
\
It is suitable for academic evaluation, interviews, and production-oriented prototypes.\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f2\fs24 \cf0 \

\f1 \uc0\u11835 
\f2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f1\fs28 \cf2 \
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\sl324\slmult1\pardirnatural\partightenfactor0

\f0\b\fs34 \cf2 License
\f1\b0\fs28 \
\
This project is intended for educational and research purposes.}