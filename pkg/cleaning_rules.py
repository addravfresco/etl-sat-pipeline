"""
CLEANING_RULES.PY - REPOSITORIO MAESTRO DE NORMALIZACIÓN
Versión Forense Generada: 2026-02-20
"""

REEMPLAZOS_MOJIBAKE = {
    # ==========================================================================
    # NIVEL 1: CORRECCIONES QUIRÚRGICAS (Evidencia Forense Real)
    # Corrección de apellidos y palabras exactas encontradas en el escaneo.
    # ==========================================================================
    
    # 1.1 Correcciones con el caracter de reemplazo Unicode (\ufffd)
    # Lote 3: Ñ rotas, vocales acentuadas, diéresis y terminaciones autocompletadas
    "CA\ufffdADAS": "CAÑADAS",
    "MADRILE\ufffdA": "MADRILEÑA",
    "PERIA\ufffdEZ": "PERIAÑEZ",
    "PEQUE\ufffdOS": "PEQUEÑOS",
    "CALDI\ufffdO": "CALDIÑO",
    "PE\ufffdAFORT": "PEÑAFORT",
    "ORDO\ufffdES": "ORDOÑES",
    "MARFILE\ufffdO": "MARFILEÑO",
    "CONDICI\ufffdN": "CONDICION",
    "CA\ufffdONGO": "CAÑONGO",
    "ARTI\ufffdO": "ARTIÑO",
    "CARDE\ufffdO": "CARDEÑO",
    "SIA\ufffdEZ": "SIAÑEZ",
    "CASTA\ufffdUELA": "CASTAÑUELA", # Autocompletado
    "G\ufffdNTNER": "GUNTNER",       # Diéresis capturada
    "GO\ufffdI": "GOÑI",
    "JIMI\ufffdNEZ": "JIMINEZ",
    "PANAME\ufffdA": "PANAMEÑA",
    "PARDI\ufffdAS": "PARDIÑAS",
    "ENSUE\ufffdO": "ENSUEÑO",
    "VI\ufffdEDO": "VIÑEDO",
    "DR\ufffdGER": "DRAGER",        # Diéresis (Dräger)
    "ORDU\ufffdEZ": "ORDUÑEZ",
    "SERME\ufffdO": "SERMEÑO",
    "DISE\ufffdADOR": "DISEÑADOR",
    "PE\ufffdUELA": "PEÑUELA",
    "I\ufffdAKI": "IÑAKI",
    "ELECTR\ufffdNICO": "ELECTRONICO", # Autocompletado
    "RANCA\ufffdO": "RANCAÑO",
    "JARALE\ufffdO": "JARALEÑO",
    "URUE\ufffdA": "URUEÑA",
    "FANDI\ufffdO": "FANDIÑO",
    "LEA\ufffdO": "LEAÑO",
    "CA\ufffdON": "CAÑON",
    "V\ufffdZQUEZ": "VAZQUEZ",
    "PA\ufffdEDA": "PAÑEDA",
    "TIZCARE\ufffdO": "TIZCAREÑO",
    "DO\ufffdEZ": "DOÑEZ",
    "SCH\ufffdTZ": "SCHUTZ",        # Diéresis (Schütz)
    "NI\ufffdEZ": "NIÑEZ",
    "ARG\ufffdELLO": "ARGUELLO",
    "CHARQUE\ufffdO": "CHARQUEÑO",  # Autocompletado
    "D\ufffdAZ": "DIAZ",
    "PE\ufffdAMILLER": "PEÑAMILLER",
    "FERRI\ufffdO": "FERRIÑO",
    "YUCAT\ufffdN": "YUCATAN",
    "CARTE\ufffdO": "CARTEÑO",
    "NORTE\ufffdO": "NORTEÑO",
    "M\ufffdRIDA": "MERIDA",
    # Lote 4: Vocales acentuadas, Ñ rotas, diéresis y autocompletados
    "VALGA\ufffdON": "VALGAÑON",
    "PALME\ufffdO": "PALMEÑO",
    "BARRA\ufffdON": "BARRAÑON",
    "MADUE\ufffdA": "MADUEÑA",
    "VILLAFA\ufffdEZ": "VILLAFAÑEZ",
    "LORO\ufffdA": "LOROÑA",
    "GARANT\ufffdAS": "GARANTIAS",
    "LE\ufffdADOR": "LEÑADOR",
    "CAMI\ufffdA": "CAMIÑA",
    "VILLACA\ufffdA": "VILLACAÑA",
    "NORTE\ufffdA": "NORTEÑA",
    "DOM\ufffdNGUEZ": "DOMINGUEZ",  # Autocompletado
    "ALTE\ufffdO": "ALTEÑO",
    "GA\ufffdA": "GAÑA",
    "SANTIVA\ufffdEZ": "SANTIVAÑEZ", # Autocompletado
    "RAME\ufffdO": "RAMEÑO",
    "LE\ufffdN": "LEON",
    "T\ufffdRK": "TURK",             # Diéresis (Türk)
    "BI\ufffdUELO": "BIÑUELO",
    "UVI\ufffdA": "UVIÑA",
    "G\ufffdEMES": "GUEMES",         # Diéresis (Güemes)
    "GUARE\ufffdO": "GUAREÑO",
    "G\ufffdTERMANN": "GUTERMANN",  # Diéresis autocompletada (Gütermann)
    "ISLE\ufffdO": "ISLEÑO",
    "ORVA\ufffdANO": "ORVAÑANO",
    "TAXQUE\ufffdA": "TAXQUEÑA",
    "DESPU\ufffdS": "DESPUES",
    "PARDI\ufffdO": "PARDIÑO",
    "MONTA\ufffdES": "MONTAÑES",
    "PRESENTACI\ufffdN": "PRESENTACION", # Autocompletado
    "RISUE\ufffdO": "RISUEÑO",
    "ALTE\ufffdA": "ALTEÑA",
    "EMPE\ufffdO": "EMPEÑO",
    "JATE\ufffdO": "JATEÑO",
    "RUBLI\ufffdOS": "RUBLIÑOS",
    "Y\ufffdIGUEZ": "YÑIGUEZ",
    "CA\ufffdIZALES": "CAÑIZALES",
    "M\ufffdNDEZ": "MENDEZ",
    "H\ufffdBILES": "HABILES",
    "CABA\ufffdEZ": "CABAÑEZ",
    "SE\ufffdORIAL": "SEÑORIAL",
    "ENDA\ufffdU": "ENDAÑU",
    "M\ufffdXICO": "MEXICO",
    "SOPE\ufffdA": "SOPEÑA",
    "EXIBICI\ufffdN": "EXIBICION",  # Respetando la falta de H de origen
    "D\ufffdBITO": "DEBITO",
    "SU\ufffdIGA": "SUÑIGA",
    "OAXAQUE\ufffdA": "OAXAQUEÑA", # Autocompletado
    "MI\ufffdRCOLES": "MIERCOLES",
    "ROQUE\ufffdI": "ROQUEÑI",
    "GABI\ufffdA": "GABIÑA",
    "PE\ufffdAFLORES": "PEÑAFLORES", # Autocompletado
    "MU\ufffdETONES": "MUÑETONES",   # Autocompletado
    "LEGIDE\ufffdO": "LEGIDEÑO",
    "MU\ufffdOZCANO": "MUÑOZCANO",   # Autocompletado
    "MU\ufffdIZA": "MUÑIZA",
    "MONTA\ufffdAS": "MONTAÑAS",
    "PE\ufffdITA": "PEÑITA",
    "L\ufffdMITE": "LIMITE",
    "IBA\ufffdES": "IBAÑES",
    "VIA\ufffdA": "VIAÑA",
    "SECE\ufffdA": "SECEÑA",
    "PEREZNU\ufffdEZ": "PEREZNUÑEZ", # Autocompletado
    "JALAPE\ufffdA": "JALAPEÑA",
    "CA\ufffdETAS": "CAÑETAS",
    "PE\ufffdAS": "PEÑAS",
    "ONTA\ufffdON": "ONTAÑON",
    "PE\ufffdALVA": "PEÑALVA",
    "PI\ufffdAN": "PIÑAN",
    "TROITI\ufffdO": "TROITIÑO",
    "SE\ufffdALES": "SEÑALES",
    "C\ufffdSAR": "CESAR",
    "CA\ufffdIZO": "CAÑIZO",
    "DUE\ufffdAZ": "DUEÑAZ",
    "SE\ufffdAL": "SEÑAL",
    "SE\ufffdALIZACION": "SEÑALIZACION", # Autocompletado
    "EUMA\ufffdA": "EUMAÑA",
    "VEL\ufffdZQUEZ": "VELAZQUEZ",
    "G\ufffdITRON": "GUITRON",       # Diéresis (Güitron)
    # Lote 5: Operación, Diéresis Alemanas, Vocales y Autocompletados
    "ESTA\ufffdON": "ESTAÑON",
    "AZO\ufffdOS": "AZOÑOS",
    "D\ufffdRR": "DURR",               # Diéresis (Dürr)
    "SU\ufffdER": "SUÑER",
    "ALVA\ufffdIL": "ALVAÑIL",
    "PILE\ufffdO": "PILEÑO",
    "URU\ufffdUELA": "URUÑUELA",
    "FERN\ufffdNDEZ": "FERNANDEZ",
    "ORDO\ufffdO": "ORDOÑO",
    "CARDE\ufffdAS": "CARDEÑAS",
    "BALLE\ufffdO": "BALLEÑO",
    "A\ufffdAS": "AÑAS",
    "DO\ufffdATES": "DOÑATES",
    "GOMEZCA\ufffdA": "GOMEZCAÑA",    # Autocompletado
    "ESTA\ufffdADOR": "ESTAÑADOR",
    "ERA\ufffdA": "ERAÑA",
    "IDU\ufffdATE": "IDUÑATE",
    "ENSE\ufffdAT": "ENSEÑAT",
    "H\ufffdCTOR": "HECTOR",
    "CALDER\ufffdN": "CALDERON",
    "BRASILE\ufffdO": "BRASILEÑO",
    "YBA\ufffdEZ": "YBAÑEZ",
    "PESTA\ufffdO": "PESTAÑO",
    "COMEZA\ufffdA": "COMEZAÑA",
    "TORA\ufffdO": "TORAÑO",
    "ARCE\ufffdO": "ARCEÑO",
    "MIDUE\ufffdO": "MIDUEÑO",
    "ORDE\ufffdANA": "ORDEÑANA",
    "TACUBE\ufffdO": "TACUBEÑO",
    "PI\ufffdAS": "PIÑAS",
    "SE\ufffdALAMIENTO": "SEÑALAMIENTO", # Autocompletado
    "BECO\ufffdA": "BECOÑA",
    "GASTELE\ufffdA": "GASTELEÑA",
    "ASCA\ufffdO": "ASCAÑO",
    "ZARE\ufffdANA": "ZAREÑANA",
    "SECE\ufffdAS": "SECEÑAS",
    "ADRI\ufffdN": "ADRIAN",
    "P\ufffdLIZA": "POLIZA",
    "CERVI\ufffdO": "CERVIÑO",
    "MARO\ufffdO": "MAROÑO",
    "DO\ufffdO": "DOÑO",
    "LING\ufffdISTICO": "LINGUISTICO",  # Diéresis y acento (Lingüístico)
    "VIDA\ufffdO": "VIDAÑO",
    "PE\ufffdARAN": "PEÑARAN",
    "DO\ufffdAN": "DOÑAN",
    "SOF\ufffdA": "SOFIA",
    "CA\ufffdIBE": "CAÑIBE",
    "RA\ufffdL": "RAUL",
    "CRUCE\ufffdO": "CRUCEÑO",
    "MERI\ufffdO": "MERIÑO",
    "A\ufffdOS": "AÑOS",
    "M\ufffdRQUEZ": "MARQUEZ",
    "SEBASTI\ufffdN": "SEBASTIAN",
    "MI\ufffdO": "MIÑO",
    "ESCA\ufffdUELA": "ESCAÑUELA",
    "COTO\ufffdETO": "COTOÑETO",
    "RA\ufffdO": "RAÑO",
    "MOSI\ufffdO": "MOSIÑO",
    "VENTURE\ufffdO": "VENTUREÑO",
    "ATLIXQUE\ufffdO": "ATLIXQUEÑO",   # Autocompletado
    "ROMA\ufffdA": "ROMAÑA",
    "BALGA\ufffdON": "BALGAÑON",
    "DISE\ufffdADOR": "DISEÑADOR",
    "DA\ufffdOS": "DAÑOS",
    "ALMAC\ufffdN": "ALMACEN",
    "PI\ufffdATARO": "PIÑATARO",
    "VALDEPE\ufffdA": "VALDEPEÑA",
    "CATALU\ufffdA": "CATALUÑA",
    "BARAGA\ufffdO": "BARAGAÑO",
    "ORDE\ufffdO": "ORDEÑO",
    "TECRUCE\ufffdO": "TECRUCEÑO",
    "CORT\ufffdS": "CORTES",
    "ALEMA\ufffdY": "ALEMANY",        # Origen Catalán
    "SABI\ufffdON": "SABIÑON",
    "EDUCACI\ufffdN": "EDUCACION",
    "CARMI\ufffdA": "CARMIÑA",
    "ABELDA\ufffdO": "ABELDAÑO",
    "CICE\ufffdO": "CICEÑO",
    "RIQUE\ufffdO": "RIQUEÑO",
    "EVALUACI\ufffdN": "EVALUACION",   # Autocompletado
    "VIRUE\ufffdA": "VIRUEÑA",
    "A\ufffdEZ": "AÑEZ",
    "ALAZA\ufffdEZ": "ALAZAÑEZ",
    "CORU\ufffdA": "CORUÑA",
    "RIA\ufffdOS": "RIAÑOS",
    "LI\ufffdA": "LIÑA",
    "MEO\ufffdO": "MEOÑO",
    "DA\ufffdINO": "DAÑINO",
    "PE\ufffdARANDA": "PEÑARANDA",
    "M\ufffdLLER": "MULLER",           # Diéresis (Müller)
    "SU\ufffdREZ": "SUAREZ",
    "MINATITL\ufffdN": "MINATITLAN",   # Autocompletado
    "PI\ufffdATA": "PIÑATA",
    "CAZA\ufffdAS": "CAZAÑAS",
    "PAZE\ufffdA": "PAZEÑA",
    "CONSTRUCCI\ufffdN": "CONSTRUCCION", # Autocompletado deductivo
    "G\ufffdERECA": "GUERECA",         # Diéresis (Güereca)
    "BA\ufffdON": "BAÑON",
    "ESTUPI\ufffdON": "ESTUPIÑON",
    "CAMA\ufffdOS": "CAMAÑOS",
    # Lote 6: Doble corrupción (NÚÑEZ), Diéresis, Operación y Autocompletados
    "M\ufffdXIMO": "MAXIMO",
    "ARL\ufffdO": "ARLIO",
    "PARDI\ufffdA": "PARDIÑA",
    "MEJ\ufffdA": "MEJIA",
    "NORTE\ufffdITA": "NORTEÑITA",
    "PI\ufffdUELA": "PIÑUELA",
    "FARI\ufffdA": "FARIÑA",
    "PASCUALE\ufffdO": "PASCUALEÑO",  # Autocompletado
    "U\ufffdATE": "UÑATE",
    "G\ufffdEROS": "GUEROS",          # Diéresis (Güeros)
    "TO\ufffdA": "TOÑA",
    "C\ufffdRDENAS": "CARDENAS",
    "LI\ufffdAS": "LIÑAS",
    "PI\ufffdEDA": "PINEDA",          # Frecuentemente Pineda
    "LIA\ufffdO": "LIAÑO",
    "TORRE\ufffdN": "TORREON",
    "NORTE\ufffdAS": "NORTEÑAS",
    "ANTU\ufffdA": "ANTUÑA",
    "DESEMPE\ufffdO": "DESEMPEÑO",
    "BARQUE\ufffdO": "BARQUEÑO",
    "SAMPEDRE\ufffdO": "SAMPEDREÑO",  # Autocompletado
    "GARRU\ufffdA": "GARRUÑA",
    "AUT\ufffdNOMA": "AUTONOMA",
    "GRA\ufffdA": "GRAÑA",
    "DUR\ufffdN": "DURAN",
    "SIGO\ufffdA": "SIGOÑA",
    "URBI\ufffdA": "URBIÑA",
    "SUPERDO\ufffdA": "SUPERDOÑA",    # Autocompletado
    "V\ufffdCTOR": "VICTOR",
    "RI\ufffdON": "RIÑON",
    "BRISE\ufffdAS": "BRISEÑAS",
    "G\ufffdERO": "GUERO",
    "M\ufffdS": "MAS",
    "PI\ufffdAL": "PIÑAL",
    "ADO\ufffdO": "ADOÑO",
    "\ufffdA": "ÑA",                  # Letra suelta capturada
    "GALV\ufffdN": "GALVAN",
    "I\ufffdARRITU": "IÑARRITU",
    "MUI\ufffdAN": "MUIÑAN",
    "MERCANC\ufffdA": "MERCANCIA",    # Autocompletado
    "TRASPE\ufffdA": "TRASPEÑA",
    "PICA\ufffdAS": "PICAÑAS",
    "RAM\ufffdN": "RAMON",
    "P\ufffdGUESE": "PAGUESE",
    "ALTE\ufffdOS": "ALTEÑOS",
    "REBOSE\ufffdO": "REBOSEÑO",
    "BARRE\ufffdADA": "BARREÑADA",
    "LOGRO\ufffdO": "LOGROÑO",
    "PISA\ufffdA": "PISAÑA",
    "BOQUI\ufffdO": "BOQUIÑO",
    "MUI\ufffdETONES": "MUIÑETONES",  # Autocompletado
    "MART\ufffdN": "MARTIN",
    "AAR\ufffdN": "AARON",            # (Aarón)
    "KU\ufffdASICH": "KUÑASICH",
    "ESPA\ufffdOLAS": "ESPAÑOLAS",
    "VERSA\ufffdEZ": "VERSAÑEZ",
    "DO\ufffdES": "DOÑES",
    "SOI\ufffdANES": "SOIÑANES",
    "MARQUE\ufffdO": "MARQUEÑO",
    "PE\ufffdARRIETA": "PEÑARRIETA",
    "N\ufffd\ufffdEZ": "NUÑEZ",        # MAGIA FORENSE: Doble ruptura (NÚÑEZ) curada
    "BELTR\ufffdN": "BELTRAN",
    "OAXAQUE\ufffdO": "OAXAQUEÑO",    # Autocompletado
    "BELE\ufffdO": "BELEÑO",
    "LACHE\ufffdO": "LACHEÑO",
    "IBARG\ufffdEN": "IBARGUEN",      # Diéresis (Ibargüen)
    "YPI\ufffdA": "YPIÑA",
    "F\ufffdTIMA": "FATIMA",
    "CESE\ufffdAS": "CESEÑAS",
    "PE\ufffdABRONCE": "PEÑABRONCE",  # Autocompletado
    "PA\ufffdALES": "PAÑALES",
    "ARRIBE\ufffdO": "ARRIBEÑO",
    "FARI\ufffdAS": "FARIÑAS",
    "PEA\ufffdA": "PEAÑA",
    "SHESE\ufffdA": "SHESEÑA",
    "MOSI\ufffdOS": "MOSIÑOS",
    "D\ufffdCK": "DUCK",              # Diéresis Alemana (Dück)
    "MA\ufffdUECO": "MAÑUECO",
    "EXPORTDISE\ufffdO": "EXPORTDISEÑO", # Autocompletado
    "TRILING\ufffdE": "TRILINGUE",    # Diéresis (Trilingüe)
    "PA\ufffdUELITO": "PAÑUELITO",
    "RU\ufffdZ": "RUIZ",
    "ESPA\ufffdOLES": "ESPAÑOLES",
    "G\ufffdERE": "GUERE",
    "ROSLI\ufffdOL": "ROSLIÑOL",
    "MESE\ufffdO": "MESEÑO",
    "UBLI\ufffdA": "UBLIÑA",
    "SA\ufffdL": "SAUL",
    "ALAZA\ufffdES": "ALAZAÑES",
    "CHILE\ufffdO": "CHILEÑO",
    "R\ufffdOS": "RIOS",
    "ROM\ufffdN": "ROMAN",
    "MAR\ufffdN": "MARIN",
    "VA\ufffdO": "VAÑO",
    "CADE\ufffdANES": "CADEÑANES",
    "MA\ufffdANA": "MAÑANA",
    "MA\ufffdE": "MAÑE",
    "MU\ufffdIS": "MUÑIS",
    "PADRE\ufffdAN": "PADREÑAN",
    "MURA\ufffdA": "MURAÑA",
    # Lote 7: Palabras cortadas, diéresis, vocales y Ñ operativas
    "RA\ufffdA": "RAÑA",
    "QUECHULE\ufffdO": "QUECHULEÑO", # Autocompletado
    "CA\ufffdARTE": "CAÑARTE",
    "IVA\ufffdEZ": "IVAÑEZ",
    "CORTE\ufffdO": "CORTEÑO",
    "BRASILE\ufffdA": "BRASILEÑA",
    "LOMBRA\ufffdA": "LOMBRAÑA",
    "LORO\ufffdO": "LOROÑO",
    "SE\ufffdORIO": "SEÑORIO",
    "FARI\ufffdO": "FARIÑO",
    "PE\ufffdAIRA": "PEÑAIRA",
    "JULI\ufffdN": "JULIAN",
    "SALVA\ufffdO": "SALVAÑO",
    "SARDI\ufffdAS": "SARDIÑAS",
    "PARDI\ufffdAZ": "PARDIÑAZ",
    "AGUI\ufffdON": "AGUIÑON",
    "VI\ufffdOPLASTIA": "VIÑOPLASTIA", # Autocompletado
    "BOLAI\ufffdITOS": "BOLAIÑITOS",
    "NERVI\ufffdO": "NERVIÑO",
    "SURE\ufffdOS": "SUREÑOS",
    "G\ufffdIZADO": "GUIZADO",        # Diéresis (Güizado)
    "DOI\ufffdAS": "DOIÑAS",
    "ERMITA\ufffdO": "ERMITAÑO",
    "BO\ufffdAR": "BOÑAR",
    "CHALQUE\ufffdO": "CHALQUEÑO",   # Autocompletado
    "BRITE\ufffdO": "BRITEÑO",
    "A\ufffdO": "AÑO",
    "YESE\ufffdA": "YESEÑA",
    "EST\ufffdMULOS": "ESTIMULOS",
    "CAPTACI\ufffdN": "CAPTACION",
    "DELEGACI\ufffdN": "DELEGACION", # Autocompletado
    "GARCIAPI\ufffdA": "GARCIAPIÑA",
    # Lote 8: Dobles rupturas (ZÚÑIGA), Nombres Aztecas, Diéresis y Autocompletados
    "MAC\ufffdAS": "MACIAS",
    "CAPULE\ufffdO": "CAPULEÑO",
    "TEQUILE\ufffdA": "TEQUILEÑA",
    "SUSTITUCI\ufffdN": "SUSTITUCION", # Autocompletado
    "GUADA\ufffdA": "GUADAÑA",
    "BENTE\ufffdO": "BENTEÑO",
    "SARE\ufffdANA": "SAREÑANA",
    "PI\ufffdEIRA": "PIÑEIRA",
    "CA\ufffdO": "CAÑO",
    "ARG\ufffdERO": "ARGUERO",         # Diéresis (Argüero)
    "CUAUHT\ufffdMOC": "CUAUHTEMOC",  # Autocompletado (Cuauhtémoc)
    "VI\ufffdALS": "VIÑALS",
    "Z\ufffd\ufffdIGA": "ZUÑIGA",      # MAGIA FORENSE: Doble ruptura (ZÚÑIGA)
    "MAR\ufffdA": "MARIA",
    "ESPA\ufffdITA": "ESPAÑITA",
    "MADRO\ufffdO": "MADROÑO",
    "GRU\ufffdON": "GRUÑON",
    "CAMU\ufffdAS": "CAMUÑAS",
    "C\ufffdRDOVA": "CORDOVA",
    "CHAVE\ufffdA": "CHAVEÑA",
    "U\ufffdA": "UÑA",
    "SOL\ufffdS": "SOLIS",
    "BEN\ufffdTEZ": "BENITEZ",
    "GUARDER\ufffdA": "GUARDERIA",    # Autocompletado
    "MA\ufffdANERO": "MAÑANERO",
    "F\ufffdLIX": "FELIX",
    "ZOPE\ufffdA": "ZOPEÑA",

    "COMPA\ufffdIA": "COMPAÑIA",
    "D\ufffdAS": "DIAS",
    "DEDUCCI\ufffdN": "DEDUCCION",
    "ZU\ufffdIGA": "ZUÑIGA",
    "EXHIBICI\ufffdN": "EXHIBICION",
    "PI\ufffdA": "PIÑA",
    "TREVI\ufffdO": "TREVIÑO",
    "P\ufffdBLICO": "PUBLICO",
    "MU\ufffdIZ": "MUÑIZ",
    "CR\ufffdDITO": "CREDITO",
    "ACU\ufffdA": "ACUÑA",
    "VILLASE\ufffdOR": "VILLASEÑOR",
    "BA\ufffdUELOS": "BAÑUELOS",
    "BOLA\ufffdOS": "BOLAÑOS",
    "QUI\ufffdONES": "QUIÑONES",
    "NI\ufffdO": "NIÑO",
    "BRISE\ufffdO": "BRISEÑO",
    "DUE\ufffdAS": "DUEÑAS",
    "DISE\ufffdO": "DISEÑO",
    "I\ufffdIGUEZ": "IÑIGUEZ",
    "BA\ufffdOS": "BAÑOS",
    "PI\ufffdON": "PIÑON",
    "GUDI\ufffdO": "GUDIÑO",
    "AVI\ufffdA": "AVIÑA",
    "MONTA\ufffdEZ": "MONTAÑEZ",
    "NU\ufffdO": "NUÑO",
    "CABA\ufffdAS": "CABAÑAS",
    "ZERME\ufffdO": "ZERMEÑO",
    "ENSE\ufffdANZA": "ENSEÑANZA",
    "COUTI\ufffdO": "COUTIÑO",
    "ORDU\ufffdA": "ORDUÑA",
    "ESPA\ufffdA": "ESPAÑA",
    # Lote 9: Palabras agudas (ón), Diéresis internacionales, y Autocompletados
    "ARSE\ufffdO": "ARSEÑO",
    "TO\ufffdO": "TOÑO",
    "CARME\ufffdO": "CARMEÑO",
    "PESTA\ufffdAS": "PESTAÑAS",
    "N\ufffdM": "NUM",                # Núm (Abreviatura de Número)
    "MADRI\ufffdAN": "MADRIÑAN",
    "EL\ufffdAS": "ELIAS",            # Elías
    "ALA\ufffdA": "ALAÑA",
    "ACOMPA\ufffdA": "ACOMPAÑA",
    "SERVICA\ufffdA": "SERVICAÑA",
    "MOIS\ufffdS": "MOISES",          # Moisés
    "GRANADE\ufffd": "GRANADEÑO",     # Autocompletado
    "PICASE\ufffdO": "PICASEÑO",
    "CASTE\ufffdEDA": "CASTEÑEDA",    # (Variante de Castañeda)
    "SURE\ufffdA": "SUREÑA",
    "CODIFICACI\ufffd": "CODIFICACION", # Autocompletado
    "GUARE\ufffdA": "GUAREÑA",
    "SESE\ufffdAS": "SESEÑAS",
    "VI\ufffdEZ": "VIÑEZ",
    "CARPI\ufffdA": "CARPIÑA",
    "RIVERE\ufffdA": "RIVEREÑA",
    "TOLUQUE\ufffd": "TOLUQUEÑO",     # Autocompletado
    "BATALL\ufffdN": "BATALLON",
    "COPE\ufffdO": "COPEÑO",
    "PORTE\ufffdO": "PORTEÑO",
    "MONCL\ufffdO": "MONCLIO",
    "LEA\ufffdEZ": "LEAÑEZ",
    "CE\ufffdAL": "CEÑAL",
    "CA\ufffdIPA": "CAÑIPA",
    "TRANQUE\ufffd": "TRANQUEÑO",     # Autocompletado
    "UCA\ufffdA": "UCAÑA",
    "SU\ufffdE": "SUÑE",
    "MU\ufffdER": "MULLER",           # Diéresis (Müller)
    "CERDE\ufffdA": "CERDEÑA",
    "SO\ufffdADOR": "SOÑADOR",
    "GUILL\ufffdN": "GUILLEN",        # Guillén
    "ORT\ufffdZ": "ORTIZ",            # Ortíz
    "CARRE\ufffdN": "CARREON",        # Carreón
    "L\ufffdZARO": "LAZARO",          # Lázaro
    "TRIVI\ufffdO": "TRIVIÑO",
    "OUBLI\ufffdA": "OUBLIÑA",
    "CADE\ufffdANEZ": "CADEÑANEZ",
    "AD\ufffdN": "ADAN",              # Adán
    "SAUTE\ufffdA": "SAUTEÑA",
    "BASCU\ufffdAN": "BASCUÑAN",
    "MU\ufffdOS": "MUÑOS",
    "LIMI\ufffdANA": "LIMIÑANA",
    "PELOT\ufffdN": "PELOTON",        # Pelotón
    "TABASQUE\ufffd": "TABASQUEÑO",   # Autocompletado
    "TRIGUE\ufffdA": "TRIGUEÑA",
    "CA\ufffdADERO": "CAÑADERO",
    # Lote 10: Apellidos agudos, Operación y Autocompletados (SANTAMARÍA, ADQUISICIÓN)
    "SALDI\ufffdA": "SALDIÑA",
    "NICOL\ufffdS": "NICOLAS",         # Nicolás
    "V\ufffdSQUEZ": "VASQUEZ",         # Vásquez
    "MOR\ufffdN": "MORIN",             # Morín
    "Y\ufffdIGO": "YÑIGO",
    "ADMI\ufffdN": "ADMIN",             # Admín (Abreviatura común en sistemas)
    "CECE\ufffdO": "CECEÑO",
    "ELEVE\ufffdO": "ELEVEÑO",
    "REA\ufffdOS": "REAÑOS",
    "PE\ufffdATO": "PEÑATO",
    "ROC\ufffdO": "ROCIO",             # Rocío
    "BEL\ufffdN": "BELEN",             # Belén
    "COSTE\ufffdITO": "COSTEÑITO",
    "MU\ufffdOHIERR": "MUÑOHIERRO",    # Autocompletado
    "ORTE\ufffdO": "ORTEÑO",
    "ECON\ufffdMICO": "ECONOMICO",     # Económico
    "BRIZE\ufffdO": "BRIZEÑO",
    "SANTILL\ufffdN": "SANTILLAN",     # Santillán
    "NARL\ufffdO": "NARLIÑO",
    "A\ufffdORBE": "AÑORBE",
    "TEG\ufffdI": "TEGUI",             # Tegüi / Tegúi
    "ACEPTACI\ufffd": "ACEPTACION",    # Autocompletado
    "LA\ufffdADO": "LAÑADO",
    "ESPETU\ufffdAL": "ESPETUÑAL",
    "COL\ufffdN": "COLON",             # Colón
    "ROBRE\ufffdO": "ROBREÑO",
    "ALADUE\ufffdA": "ALADUEÑA",
    "TECOM\ufffdN": "TECOMAN",         # Tecomán
    "DA\ufffdU": "DAÑU",
    "G\ufffdENTELLA": "GUENTELLA",     # Diéresis (Güentella)
    "ADQUISICI\ufffd": "ADQUISICION",  # Autocompletado
    "AMOZOQUE\ufffd": "AMOZOQUEÑO",    # Autocompletado
    "PERI\ufffdON": "PERIÑON",
    "P\ufffdBLICA": "PUBLICA",         # Pública
    "KA\ufffdETAS": "KAÑETAS",
    "ZIZA\ufffdA": "ZIZAÑA",
    "CICE\ufffdO": "CICEÑO",
    "ALVA\ufffdEZ": "ALVAÑEZ",
    "ESPITU\ufffdAL": "ESPITUÑAL",
    "CRIST\ufffdBAL": "CRISTOBAL",     # Cristóbal
    "OROPL\ufffdA": "OROPLIÑA",
    "VINCULACI\ufffd": "VINCULACION",  # Autocompletado
    "PE\ufffdASCOS": "PEÑASCOS",
    "ZUETA\ufffdA": "ZUETAÑA",
    "SERGI\ufffdO": "SERGIÑO",
    "FELE\ufffdOS": "FELEÑOS",
    "BARTOLE\ufffd": "BARTOLEÑO",      # Autocompletado
    "VELDA\ufffdEZ": "VELDAÑEZ",
    "TAMPIQUE\ufffd": "TAMPIQUEÑO",    # Autocompletado
    "ANDURL\ufffdA": "ANDURLIÑA",
    "SANMARQUE\ufffd": "SANMARQUEÑO",  # Autocompletado
    "FR\ufffdAS": "FRIAS",             # Frías
    "TRISTE\ufffdO": "TRISTEÑO",
    "SALDL\ufffdAS": "SALDLIÑAS",
    "CASTA\ufffdAS": "CASTAÑAS",
    "CONCHE\ufffd": "CONCHEÑO",        # Autocompletado
    "LUMBRA\ufffdO": "LUMBRAÑO",
    "SE\ufffdALETICA": "SEÑALETICA",   # Señalética
    "ARAG\ufffdN": "ARAGON",           # Aragón
    "MURL\ufffdO": "MURLIÑO",
    "VALD\ufffdS": "VALDES",           # Valdés
    "RASC\ufffdN": "RASCON",           # Rascón
    "RINC\ufffdN": "RINCON",           # Rincón
    "ANTO\ufffdO": "ANTOÑO",
    "TO\ufffdITA": "TOÑITA",
    "CHENTE\ufffdOS": "CHENTEÑOS",
    "JAIRSHL\ufffdO": "JAIRSHLIÑO",
    "PI\ufffdONEZ": "PIÑONEZ",
    "SCH\ufffdADOW": "SCHADOW",         # Diéresis (Schädow)
    "PERPI\ufffdA": "PERPIÑA",
    "GUDI\ufffdOS": "GUDIÑOS",
    "T\ufffdTULOS": "TITULOS",         # Títulos
    "ABELDA\ufffdEZ": "ABELDAÑEZ",
    "ORDE\ufffdA": "ORDEÑA",
    "ALTE\ufffdAS": "ALTEÑAS",
    "ORO\ufffdA": "OROÑA",
    "ALC\ufffdNTARA": "ALCANTARA",     # Alcántara
    "N\ufffdJERA": "NAJERA",           # Nájera
    "CASPE\ufffdA": "CASPEÑA",
    "VALMA\ufffdA": "VALMAÑA",
    "TU\ufffdAS": "TUÑAS",
    "SALBA\ufffdO": "SALBAÑO",
    "BEDRI\ufffdANA": "BEDRIÑANA",
    "DEAG\ufffdEROS": "DEAGUEROS",     # Diéresis (Deagüeros)
    "LICITACI\ufffdN": "LICITACION",   # Licitación
    "JOAQU\ufffdN": "JOAQUIN",         # Joaquín
    "SANTAMAR\ufffd": "SANTAMARIA",    # Autocompletado
    "I\ufffdARRA": "IÑARRA",
    "ARRU\ufffdADA": "ARRUÑADA",
    "AR\ufffdVALO": "AREVALO",         # Arévalo
    "COCA\ufffdO": "COCAÑO",
    "ART\ufffdCULO": "ARTICULO",       # Artículo
    "RA\ufffdON": "RAÑON",
    "EGA\ufffdA": "EGAÑA",
    "S\ufffdENZ": "SAENZ",             # Sáenz
    "BRE\ufffdAS": "BREÑAS",
    # Lote 11: Nombres propios, Operación, Diéresis y Autocompletados (CÓDIGO, CONDONACIÓN)
    "I\ufffdIGUES": "IÑIGUES",
    "ARMENDI\ufffdR": "ARMENDARIZ",   # Autocompletado deductivo
    "PE\ufffdAROJA": "PEÑAROJA",
    "OUVI\ufffdA": "OUVIÑA",
    "CA\ufffdERO": "CAÑERO",
    "VI\ufffdOLAS": "VIÑOLAS",
    "BOQUE\ufffdA": "BOQUEÑA",
    "REQUE\ufffdO": "REQUEÑO",
    "ESCA\ufffdUELA": "ESCAÑUELA",
    "MULTISE\ufffdAL": "MULTISEÑAL",  # Autocompletado
    "ESC\ufffdRCEGA": "ESCARCEGA",    # Escárcega
    "SALDA\ufffdO": "SALDAÑO",
    "ARRIGUE\ufffdO": "ARRIGUEÑO",
    "FILOL\ufffdGICA": "FILOLOGICA",  # Filológica
    "G\ufffdLVEZ": "GALVEZ",          # Gálvez
    "ALDA\ufffdA": "ALDAÑA",
    "VI\ufffdEGAS": "VIÑEGAS",
    "PEQUE\ufffdITA": "PEQUEÑITA",
    "COMPA\ufffdER": "COMPAÑERO",     # Autocompletado
    "RENDI\ufffdN": "RENDICION",      # Rendición (Autocompletado)
    "ATENCI\ufffdN": "ATENCION",      # Atención
    "PER\ufffdZ": "PEREZ",            # Pérez
    "CURE\ufffdA": "CUREÑA",
    "PI\ufffdEROS": "PIÑEROS",
    "CASA\ufffdA": "CASAÑA",
    "REHABILITACI\ufffd": "REHABILITACION", # Autocompletado
    "MOA\ufffdA": "MOAÑA",
    "MERO\ufffdO": "MEROÑO",
    "QUITE\ufffdO": "QUITEÑO",
    "BENJAM\ufffdN": "BENJAMIN",      # Benjamín
    "SE\ufffdAS": "SEÑAS",
    "VILLAG\ufffdMEZ": "VILLAGOMEZ",  # Villagómez
    "VIDA\ufffdEZ": "VIDAÑEZ",
    "AVIL\ufffdS": "AVILES",          # Avilés
    "VI\ufffdALES": "VIÑALES",
    "PEZTA\ufffdA": "PEZTAÑA",
    "POLIC\ufffdA": "POLICIA",        # Policía
    "ZEDE\ufffdO": "ZEDEÑO",
    "TEMIXQUE\ufffd": "TEMIXQUEÑO",   # Autocompletado
    "MA\ufffdOS": "MAÑOS",
    "G\ufffdIDO": "GUIDO",            # Diéresis (Güido)
    "MOCLI\ufffdOZ": "MOCLIÑOZ",
    "CONDONACI\ufffd": "CONDONACION",  # Autocompletado
    "COMUNDEI\ufffd": "COMUNDEÑO",    # Autocompletado
    "PE\ufffdAGUIRR": "PEÑAGUIRRE",   # Autocompletado
    "LURUE\ufffdA": "LURUEÑA",
    "ALEM\ufffdN": "ALEMAN",          # Alemán
    "CENTE\ufffdO": "CENTEÑO",
    "ZE\ufffdA": "ZEÑA",
    "GO\ufffdY": "GOÑY",
    "CA\ufffdAL": "CAÑAL",
    "DEVU\ufffdLVAS": "DEVUELVAS",    # Devuélvas
    "RENTER\ufffdA": "RENTERIA",      # Rentería
    "C\ufffdBRESE": "COBRESE",        # Cóbrese
    "ISTME\ufffdOS": "ISTMEÑOS",
    "VI\ufffdE": "VIÑE",
    "EPIFA\ufffdO": "EPIFAÑO",
    "TULTITL\ufffdN": "TULTITLAN",    # Tultitlán
    "JAG\ufffdEY": "JAGUEY",          # Diéresis (Jagüey)
    "AZCA\ufffdO": "AZCAÑO",
    "CASCARLI\ufffdA": "CASCARLIÑA",
    "OPTIDISE\ufffdO": "OPTIDISEÑO",  # Autocompletado
    "BRA\ufffdAS": "BRAÑAS",
    "RELACI\ufffdN": "RELACION",      # Relación
    "G\ufffdNGORA": "GONGORA",        # Góngora
    "ORME\ufffdO": "ORMEÑO",
    "PITIQUE\ufffdOS": "PITIQUEÑOS",
    "COUSLI\ufffdO": "COUSLIÑO",
    "RESCA\ufffdO": "RESCAÑO",
    "VALENT\ufffdN": "VALENTIN",      # Valentín
    "BILING\ufffdES": "BILINGUES",    # Diéresis (Bilingües)
    "C\ufffdDIGO": "CODIGO",          # Código
    "J\ufffdRGEN": "JURGEN",          # Diéresis (Jürgen)
    "GARAPI\ufffdAD": "GARAPIÑADO",   # Autocompletado
    "LAMU\ufffdO": "LAMUÑO",
    "ARTI\ufffdANO": "ARTIÑANO",
    "SE\ufffdARQ": "SEÑARQ",
    "G\ufffdENDULAI": "GUENDULAIN",   # Autocompletado (Güendulain)
    "DISE\ufffdARTE": "DISEÑARTE",
    "LE\ufffdO": "LEÑO",
    "PROTECCI\ufffd": "PROTECCION",   # Autocompletado
    "VIA\ufffdEZ": "VIAÑEZ",
    "MURE\ufffdO": "MUREÑO",
    "CAMPLI\ufffdO": "CAMPLIÑO",
    "G\ufffdNESIS": "GENESIS",        # Génesis
    "NUXA\ufffdO": "NUXAÑO",
    "GRA\ufffdEN": "GRAÑEN",
    "YVA\ufffdEZ": "YVAÑEZ",
    "ACLIXQUE\ufffd": "ACLIXQUEÑO",   # Autocompletado
    "CARLI\ufffdITO": "CARLIÑITO",
    "ESCARRE\ufffdO": "ESCARREÑO",
    # Lote 12: Dobles rupturas (ORDÓÑEZ), Fiscales, Gentilicios y Diéresis
    "SA\ufffdEZ": "SAÑEZ",
    "PERE\ufffdA": "PEREÑA",
    "ACE\ufffdA": "ACEÑA",
    "PEREZPE\ufffdA": "PEREZPEÑA",
    "JA\ufffdAS": "JAÑAS",
    "EXVI\ufffdEDOS": "EXVIÑEDOS",
    "DAR\ufffdO": "DARIO",             # Darío
    "TECNOL\ufffdGIC": "TECNOLOGICO",   # Autocompletado (Tecnológico)
    "ACORU\ufffdA": "ACORUÑA",
    "ALBI\ufffdO": "ALBIÑO",
    "PI\ufffd\ufffdN": "PIÑON",        # MAGIA FORENSE: Doble ruptura (PIÑÓN)
    "MEZTE\ufffdO": "MEZTEÑO",
    "JAIRZLI\ufffdHO": "JAIRZLIÑHO",
    "TEPEQUE\ufffd": "TEPEQUEÑO",      # Autocompletado
    "GARB\ufffdE": "GARBUE",           # Diéresis (Garbüe)
    "M\ufffdA": "MIA",                 # Mía
    "PARA\ufffdO": "PARAÑO",
    "CA\ufffdALS": "CAÑALS",
    "CARCA\ufffdA": "CARCAÑA",
    "TENANGUE\ufffd": "TENANGUEÑO",    # Autocompletado
    "DUE\ufffdA": "DUEÑA",
    "MULTILING\ufffd": "MULTILINGUE",  # Autocompletado y Diéresis (Multilingüe)
    "SIM\ufffdN": "SIMON",             # Simón
    "VERCA\ufffdAMO": "VERCAÑAMO",
    "IN\ufffdS": "INES",               # Inés
    "TAQUI\ufffdOS": "TAQUIÑOS",
    "TORU\ufffdO": "TORUÑO",
    "SE\ufffdALETICA": "SEÑALETICA",   # Señalética
    "ALCA\ufffdA": "ALCAÑA",
    "DISE\ufffdADOS": "DISEÑADOS",
    "COORDINACI\ufffd": "COORDINACION", # Autocompletado
    "MARMA\ufffdA": "MARMAÑA",
    "GIR\ufffdN": "GIRON",             # Girón
    "CA\ufffdITA": "CAÑITA",
    "CHAVARR\ufffdA": "CHAVARRIA",     # Chavarría
    "DA\ufffdO": "DAÑO",
    "CATA\ufffdEDA": "CATAÑEDA",
    "TR\ufffdMITES": "TRAMITES",       # Trámites
    "SUGRA\ufffdES": "SUGRAÑES",
    "CHANTE\ufffdO": "CHANTEÑO",
    "EFRA\ufffdN": "EFRAIN",           # Efraín
    "ASCA\ufffdIO": "ASCAÑIO",
    "CAVA\ufffdAS": "CAVAÑAS",
    "CATAVI\ufffdA": "CATAVIÑA",
    "CASCADLI\ufffdA": "CASCADLIÑA",
    "VIVA\ufffdO": "VIVAÑO",
    "ISA\ufffdAS": "ISAIAS",           # Isaías
    "GARANT\ufffdA": "GARANTIA",       # Garantía
    "KURIBRE\ufffdA": "KURIBREÑA",
    "BR\ufffdCKNER": "BRUCKNER",       # Diéresis (Brückner)
    "CALCA\ufffdO": "CALCAÑO",
    "PE\ufffdAGRAN": "PEÑAGRANDE",     # Autocompletado
    "FACTURACI\ufffd": "FACTURACION",  # Autocompletado (Facturación)
    "ESTABILIZACI\ufffd": "ESTABILIZACION", # Autocompletado
    "CASTLI\ufffdEIRA": "CASTLIÑEIRA",
    "ORD\ufffd\ufffdEZ": "ORDOÑEZ",    # MAGIA FORENSE: Doble ruptura (ORDÓÑEZ)
    "JER\ufffdNIMO": "JERONIMO",       # Jerónimo
    "NA\ufffdES": "NAÑES",
    "CRUSE\ufffdO": "CRUSEÑO",
    "GODI\ufffdNEZ": "GODINEZ",        # Godínez
    "FLA\ufffdO": "FLAÑO",
    "MUI\ufffdO": "MUIÑO",
    "LO\ufffdA": "LOÑA",
    "SANTIVA\ufffdES": "SANTIVAÑES",
    "BERM\ufffdDEZ": "BERMUDEZ",       # Bermúdez
    "PADR\ufffdN": "PADRON",           # Padrón
    "CHEG\ufffdE": "CHEGUE",           # Diéresis (Chegüe)
    "PERFIDISE\ufffd": "PERFIDISEÑO",  # Autocompletado
    "A\ufffdOVEROS": "AÑOVEROS",
    "ESPI\ufffdEIRO": "ESPIÑEIRO",
    "MARISKE\ufffdA": "MARISKEÑA",
    "SOL\ufffdRZANO": "SOLORZANO",     # Solórzano
    "PE\ufffdANEGRA": "PEÑANEGRA",
    "TLAXQUE\ufffdO": "TLAXQUEÑO",
    "YAZM\ufffdN": "YAZMIN",           # Yazmín
    "ACAPULQUE\ufffd": "ACAPULQUEÑO",  # Autocompletado
    "CAUTI\ufffdO": "CAUTIÑO",
    "O\ufffdA": "OÑA",
    "BENDA\ufffdA": "BENDAÑA",
    "BL\ufffdHEN": "BLUHEN",           # Diéresis (Blühen)
    "NARV\ufffdEZ": "NARVAEZ",         # Narváez
    "VALLE\ufffdO": "VALLEÑO",
    "CANC\ufffdN": "CANCUN",           # Cancún
    "LUISLI\ufffdO": "LUISLIÑO",
    "OPERACI\ufffdN": "OPERACION",     # Operación
    "CARLE\ufffdO": "CARLEÑO",
    "SUZA\ufffdA": "SUZAÑA",
    "HUICHAPE\ufffd": "HUICHAPEÑO",    # Autocompletado
    "LAVI\ufffdA": "LAVIÑA",
    "IND\ufffdGENA": "INDIGENA",       # Indígena
    "GARDE\ufffdA": "GARDEÑA",
    "OTO\ufffdEL": "OTOÑEL",
    "G\ufffdEREQUE": "GUEREQUE",       # Diéresis (Güereque)
    "GORVE\ufffdA": "GORVEÑA",
    "GORRLI\ufffdO": "GORRLIÑO",
    "ALBA\ufffdILERIA": "ALBAÑILERIA", # Albañilería
    "A\ufffdADIDOS": "AÑADIDOS",
    "D\ufffdNNCOME": "DUNNCOME",       # Diéresis (Dünncome)
    "CAZTA\ufffdEDA": "CAZTAÑEDA",
    "COFLI\ufffdO": "COFLIÑO",
    # Lote 13: Gentilicios, Apellidos agudos, Operación y Autocompletados
    "OPE\ufffdO": "OPEÑO",
    "CARPI\ufffdO": "CARPIÑO",
    "CASTA\ufffdARE": "CASTAÑARES",    # Autocompletado deductivo
    "TING\ufffdINDIN": "TINGUINDIN",  # Diéresis y acento (Tingüindín)
    "MU\ufffdOZABA": "MUÑOZABAL",     # Autocompletado
    "PERIA\ufffdES": "PERIAÑES",
    "SANLUISE\ufffd": "SANLUISEÑO",   # Autocompletado
    "COZUMELE\ufffd": "COZUMELEÑO",   # Autocompletado
    "ORIZABE\ufffdA": "ORIZABEÑA",
    "DURANGUE\ufffd": "DURANGUEÑO",   # Autocompletado
    "TLAXIAQUE\ufffd": "TLAXIAQUEÑO", # Autocompletado
    "DIFUSI\ufffdN": "DIFUSION",      # Difusión
    "CASTA\ufffdER": "CASTAÑER",
    "CA\ufffdARES": "CAÑARES",
    "VIDUE\ufffdO": "VIDUEÑO",
    "BARA\ufffdANO": "BARAÑANO",
    "ALDU\ufffdEZ": "ALDUÑEZ",
    "CONSTRUSUE\ufffd": "CONSTRUSUEÑOS", # Autocompletado deductivo
    "JAIRZLI\ufffdO": "JAIRZLIÑO",
    "ESPI\ufffdEIRA": "ESPIÑEIRA",
    "VECO\ufffdA": "VECOÑA",
    "ARMI\ufffdO": "ARMIÑO",
    "LASA\ufffdA": "LASAÑA",
    "A\ufffdEL": "AÑEL",
    "CUSQUE\ufffdA": "CUSQUEÑA",
    "MOTI\ufffdO": "MOTIÑO",
    "CASTA\ufffdA": "CASTAÑA",
    "DIVISI\ufffdN": "DIVISION",      # División
    "PU\ufffdO": "PUÑO",
    "COU\ufffdAGO": "COUÑAGO",
    "PLOBA\ufffdOS": "PLOBAÑOS",
    "FERREBA\ufffdC": "FERREBAÑO",    # Deductivo
    "GERM\ufffdN": "GERMAN",          # Germán
    "AGUILL\ufffdN": "AGUILLON",      # Aguillón
    "BRAGA\ufffdA": "BRAGAÑA",
    "REBA\ufffdO": "REBAÑO",
    "PR\ufffdXIMO": "PROXIMO",        # Próximo
    "MALAG\ufffdN": "MALAGON",        # Malagón
    "USA\ufffdO": "USAÑO",
    "PE\ufffdO": "PEÑO",
    "VELARDE\ufffdA": "VELARDEÑA",
    "TLALPE\ufffdA": "TLALPEÑA",
    "COCORE\ufffdA": "COCOREÑA",
    "MAZCARE\ufffd": "MAZCAREÑO",     # Autocompletado
    "IG\ufffdAKI": "IÑAKI",           # Corrección de captura
    "CASTORE\ufffdA": "CASTOREÑA",
    "B\ufffdEZ": "BAEZ",              # Báez
    "PI\ufffdOL": "PIÑOL",
    "MA\ufffdAS": "MAÑAS",
    "ESPU\ufffdES": "ESPUÑES",
    "SERVI\ufffdN": "SERVION",        # Servión
    "BOLA\ufffdOZ": "BOLAÑOZ",
    "CA\ufffdATE": "CAÑATE",
    "ANTO\ufffdIO": "ANTONIO",        # Corrección de captura (Antoñio -> Antonio)
    "CA\ufffdUELAS": "CAÑUELAS",
    "UNIDISE\ufffdO": "UNIDISEÑO",
    "SEI\ufffdKOWSKI": "SEINKOWSKI",  # Autocompletado visual
    "CA\ufffdITAS": "CAÑITAS",
    "ARTAI\ufffdAN": "ARTAÑAN",       # Artañan
    "PILO\ufffdA": "PILOÑA",
    "TERRU\ufffdOS": "TERRUÑOS",
    "NI\ufffdODAGUI": "NIÑODAGUI",
    "JA\ufffdIL": "JAÑIL",
    "SALOM\ufffdN": "SALOMON",        # Salomón
    "GASTA\ufffdAGA": "GASTAÑAGA",
    "COTIZACI\ufffd": "COTIZACION",   # Autocompletado
    "GORBE\ufffdA": "GORBEÑA",
    "ECHEVERR\ufffd": "ECHEVERRIA",   # Autocompletado
    "A\ufffdADIDO": "AÑADIDO",
    "SU\ufffdOL": "SUÑOL",
    "VERZA\ufffdEZ": "VERZAÑEZ",
    "PE\ufffdALTA": "PEÑALTA",
    "LAG\ufffdI": "LAGUI",            # Diéresis (Lagüi)
    "SANTOSBE\ufffd": "SANTOSBEÑO",   # Autocompletado
    "PUNTE\ufffdO": "PUNTEÑO",
    "OLGU\ufffdN": "OLGUIN",          # Olguín
    "MARYTO\ufffdA": "MARYTOÑA",
    "M\ufffdA": "MIA",                # Mía
    "CA\ufffdIBANO": "CAÑIBANO",
    "NARLI\ufffdAN": "NARLIÑAN",
    "TOLUQUE\ufffdA": "TOLUQUEÑA",
    "ARA\ufffdO": "ARAÑO",
    "F\ufffdSICA": "FISICA",          # Física
    "G\ufffdENDOLIN": "GUENDOLIN",    # Diéresis (Güendolin)
    "CASTA\ufffdEDA": "CASTAÑEDA",
    "SUENI\ufffdOS": "SUEÑOS",        # Corrección deductiva
    "MAT\ufffdAS": "MATIAS",          # Matías
    "ZAPI\ufffdA": "ZAPIÑA",
    "SAUCE\ufffdO": "SAUCEÑO",
    "BAI\ufffdULS": "BAÑULS",
    "TER\ufffdN": "TERAN",            # Terán
    "I\ufffdURRIA": "IÑURRIA",
    "V\ufffdLEZ": "VELEZ",            # Vélez
    "R\ufffdSTUNGSF": "RUSTUNGSF",    # Diéresis (Rüstungs...)
    "MAZATE\ufffdO": "MAZATEÑO",
    "CARMI\ufffdA": "CARMIÑA",
    "TAGUE\ufffdA": "TAGUEÑA",
    "OTA\ufffdO": "OTAÑO",
    "DISTRIBUCI\ufffd": "DISTRIBUCION", # Autocompletado
    "CALVI\ufffdO": "CALVIÑO",
    # Lote 14: Palabras operativas cortadas, Diéresis internacionales y Apellidos
    "EDLI\ufffdHO": "EDLIÑHO",
    "YDU\ufffdATE": "YDUÑATE",
    "BALAG\ufffdER": "BALAGUER",        # Diéresis (Balagüer)
    "D\ufffdSSELDOR": "DUSSELDORF",      # Autocompletado (Düsseldorf)
    "VEL\ufffdSQUEZ": "VELASQUEZ",       # Velásquez
    "\ufffdEZ": "ÑEZ",                   # Terminación huérfana
    "LOPECEDE\ufffd": "LOPECEDEÑO",      # Autocompletado
    "ARISTIMU\ufffd": "ARISTIMUÑO",      # Autocompletado
    "RISUE\ufffdOS": "RISUEÑOS",
    "N\ufffdSTOR": "NESTOR",             # Néstor
    "MA\ufffdANIN": "MAÑANIN",
    "GUARACHE\ufffd": "GUARACHEÑO",      # Autocompletado
    "SARCE\ufffdO": "SARCEÑO",
    "MARROQU\ufffd": "MARROQUIN",        # Autocompletado (Marroquín)
    "PRUA\ufffdO": "PRUAÑO",
    "MILDISE\ufffdOS": "MILDISEÑOS",
    "PARAISE\ufffdO": "PARAISEÑO",
    "CAMPA\ufffdAS": "CAMPAÑAS",
    "CHL\ufffdA": "CHLIÑA",
    "ORDU\ufffdES": "ORDUÑES",
    "CERRETE\ufffdO": "CERRETEÑO",
    "LUJ\ufffdN": "LUJAN",               # Luján
    "CABALLER\ufffd": "CABALLERIA",      # Autocompletado deductivo
    "FALC\ufffdN": "FALCON",             # Falcón
    "SALMER\ufffdN": "SALMERON",         # Salmerón
    "GARCIAPE\ufffd": "GARCIAPEÑA",      # Autocompletado
    "ERMI\ufffdO": "ERMIÑO",
    "O\ufffdEZ": "OÑEZ",
    "PAZMI\ufffdO": "PAZMIÑO",
    "EKHI\ufffdE": "EKHIÑE",
    "CERDE\ufffdO": "CERDEÑO",
    "LOP\ufffdZ": "LOPEZ",               # (Error de origen: Lopéz)
    "GUIA\ufffdEZ": "GUIAÑEZ",
    "CASTL\ufffdEYRA": "CASTLIÑEYRA",
    "B\ufffdRBARA": "BARBARA",           # Bárbara
    "CASTEL\ufffdN": "CASTELAN",         # Castelán
    "AGUIRRE\ufffdA": "AGUIRREÑA",
    "ARA\ufffdA": "ARAÑA",
    "ZACAR\ufffdAS": "ZACARIAS",         # Zacarías
    "LING\ufffdISTICA": "LINGUISTICA",   # Diéresis (Lingüística)
    "OLAI\ufffdETA": "OLAIÑETA",
    "RINCONE\ufffdO": "RINCONEÑO",
    "G\ufffdITIAN": "GUITIAN",           # Diéresis (Güitian)
    "GA\ufffdEZ": "GAÑEZ",
    "ALBE\ufffdO": "ALBEÑO",
    "MI\ufffdAN": "MIÑAN",
    "CHARME\ufffdO": "CHARMEÑO",
    "IDENTIFICACI\ufffd": "IDENTIFICACION", # Autocompletado
    "NEV\ufffdREZ": "NEVAREZ",           # Nevárez
    "CA\ufffdELLAS": "CAÑELLAS",
    "BAG\ufffdES": "BAGUES",             # Diéresis (Bagües)
    "PING\ufffdI": "PINGUI",             # Diéresis (Pingüi)
    "ACAD\ufffdMICO": "ACADEMICO",       # Académico
    "G2DISE\ufffdO": "G2DISEÑO",
    "PE\ufffdAVERA": "PEÑAVERA",
    "EURODISE\ufffd": "EURODISEÑO",      # Autocompletado
    "N\ufffd8": "NUMERO 8",              # Corrección visual
    "CADL\ufffdANOS": "CADLIÑANOS",
    "OTO\ufffdO": "OTOÑO",
    "CIA\ufffdEZ": "CIAÑEZ",
    "PE\ufffdACORAD": "PEÑACORADA",      # Autocompletado
    "VILLFA\ufffdA": "VILLFAÑA",
    "ZAPACU\ufffdA": "ZAPACUÑA",
    "SER\ufffdN": "SERON",               # Serón
    "M\ufffdGGENBU": "MUGGENBURG",        # Autocompletado y Diéresis
    "CA\ufffdES": "CAÑES",
    "ME\ufffdO": "MEÑO",
    "MI\ufffdE": "MIÑE",
    "JALAPE\ufffdO": "JALAPEÑO",
    "ARRL\ufffdAGA": "ARRLIÑAGA",
    "ENGRO\ufffdAT": "ENGROÑAT",
    "G\ufffdICHO": "GUICHO",             # Diéresis (Güicho)
    "H\ufffdROES": "HEROES",             # Héroes
    "TURUE\ufffdO": "TURUEÑO",
    "PEQUENI\ufffdC": "PEQUENIÑOS",      # Autocompletado deductivo
    "RIQUE\ufffdA": "RIQUEÑA",
    "BIZUA\ufffdO": "BIZUAÑO",
    "SEP\ufffdLVEDA": "SEPULVEDA",       # Sepúlveda
    "ERMITA\ufffdA": "ERMITAÑA",
    "PE\ufffdAILILLO": "PEÑAILILLO",
    "ACEA\ufffdEZ": "ACEAÑEZ",
    "ORODO\ufffdEZ": "ORODOÑEZ",
    "INFORMACI\ufffd": "INFORMACION",    # Autocompletado
    "ARROYE\ufffdOS": "ARROYEÑOS",
    "TECNODISE\ufffd": "TECNODISEÑO",    # Autocompletado
    "CU\ufffdA": "CUÑA",
    "PAVISE\ufffdALE": "PAVISEÑALES",    # Autocompletado
    "DELI\ufffdO": "DELIÑO",
    "MARISTME\ufffd": "MARISTMEÑO",      # Autocompletado
    "C\ufffdZARES": "CAZARES",           # Cázares
    "PLI\ufffdANGO": "PLIÑANGO",
    "JU\ufffdOR": "JUNIOR",              # Junior (Júnior)
    "BA\ufffdOMOBIL": "BAÑOMOBIL",
    "TECNOL\ufffdGIC": "TECNOLOGICO",    # Autocompletado
    "BOJ\ufffdRQUEZ": "BOJORQUEZ",       # Bojórquez
    "EFR\ufffdN": "EFREN",               # Efrén
    "C\ufffdRDOBA": "CORDOBA",           # Córdoba
    "MEDIACI\ufffdN": "MEDIACION",       # Mediación
    "PLI\ufffdEIROS": "PLIÑEIROS",
    # Lote 15: Dobles rupturas (YÁÑEZ), Legales, Administrativos y Diéresis
    "OTA\ufffdES": "OTAÑES",
    "BA\ufffdOZ": "BAÑOZ",
    "R\ufffdO": "RIO",                  # Río
    "ZAMORE\ufffdA": "ZAMOREÑA",
    "COMPA\ufffdER": "COMPAÑERO",      # Autocompletado
    "CU\ufffdADO": "CUÑADO",
    "CORROV\ufffdA": "CORROVIÑA",
    "RAMS\ufffdS": "RAMSES",           # Ramsés
    "PADRI\ufffdAN": "PADRIÑAN",
    "GONZALEZNU\ufffd": "GONZALEZNUÑEZ", # Autocompletado
    "CA\ufffdIZALEZ": "CAÑIZALEZ",
    "MO\ufffdOZ": "MOÑOZ",
    "LE\ufffdEROS": "LEÑEROS",
    "AU\ufffdON": "AUÑON",
    "PE\ufffdARRUBIA": "PEÑARRUBIA",
    "ZAPE\ufffdASCO": "ZAPEÑASCO",
    "COMESA\ufffdA": "COMESAÑA",
    "LUI\ufffdA": "LUIÑA",
    "VIDA\ufffdAS": "VIDAÑAS",
    "SOCORRE\ufffd": "SOCORREÑO",      # Autocompletado
    "S\ufffdMANO": "SIMANO",           # Símano
    "BR\ufffdDER": "BRUDER",           # Diéresis (Brüder)
    "CA\ufffdAGAS": "CAÑAGAS",
    "VI\ufffdECOM": "VIÑECOM",
    "SECRETAR\ufffd": "SECRETARIA",    # Autocompletado (Secretaría)
    "AVENDA\ufffd\ufffd": "AVENDAÑO",  # MAGIA FORENSE: Doble ruptura
    "MIG\ufffdON": "MIGUIÑON",
    "M\ufffdLTIPLE": "MULTIPLE",       # Múltiple
    "MONTA\ufffdITA": "MONTAÑITA",
    "REVISI\ufffdN": "REVISION",       # Revisión
    "COCU\ufffdAME": "COCUÑAME",
    "MUI\ufffdANA": "MUIÑANA",
    "CARPE\ufffdA": "CARPEÑA",
    "ENSE\ufffdA": "ENSEÑA",
    "ECONOM\ufffdA": "ECONOMIA",       # Economía
    "DAV\ufffdA": "DAVIÑA",
    "ENV\ufffdO": "ENVIO",             # Envío
    "CAMALE\ufffdO": "CAMALEÑO",
    "CORT\ufffdAS": "CORTIÑAS",
    "SO\ufffdA": "SOÑA",
    "KARM\ufffdA": "KARMIÑA",
    "PRECISI\ufffdN": "PRECISION",     # Precisión
    "SEG\ufffdN": "SEGUN",             # Según
    "VICU\ufffdO": "VICUÑO",
    "MILL\ufffdN": "MILLON",           # Millón
    "GASPARE\ufffdO": "GASPAREÑO",
    "CREACI\ufffdN": "CREACION",       # Creación
    "TORRE\ufffdA": "TORREÑA",
    "CONSERVACI\ufffd": "CONSERVACION", # Autocompletado
    "HOLGU\ufffdN": "HOLGUIN",         # Holguín
    "N\ufffdZHET": "NUZHET",           # Diéresis (Nüzhet)
    "C\ufffdMARA": "CAMARA",           # Cámara
    "CAZA\ufffdAZ": "CAZAÑAZ",
    "DISE\ufffdANDO": "DISEÑANDO",
    "ALEGR\ufffdA": "ALEGRIA",         # Alegría
    "P\ufffdEZ": "PAEZ",               # Páez
    "BENTUR\ufffdO": "BENTURIÑO",
    "D\ufffdVALOS": "DAVALOS",         # Dávalos
    "ARG\ufffdESO": "ARGUESO",         # Diéresis (Argüeso)
    "HERN\ufffdN": "HERNAN",           # Hernán
    "CONSIGNACI\ufffd": "CONSIGNACION", # Autocompletado
    "SERI\ufffdA": "SERIA",
    "M\ufffdDICO": "MEDICO",           # Médico
    "AVI\ufffdOA": "AVIÑOA",
    "BOGMU\ufffdOZ": "BOGMUÑOZ",
    "PROA\ufffdOS": "PROAÑOS",
    "SALDA\ufffdAS": "SALDAÑAS",
    "G\ufffdERITOS": "GUERITOS",       # Diéresis (Güeritos)
    "REPOSICI\ufffdN": "REPOSICION",   # Reposición
    "PORR\ufffdO": "PORRIÑO",
    "EXPROPIACI\ufffd": "EXPROPIACION", # Autocompletado
    "SANTANE\ufffdO": "SANTANEÑO",
    "ASUNCI\ufffdN": "ASUNCION",       # Asunción
    "GARN\ufffdO": "GARNIÑO",
    "MA\ufffdANIM": "MAÑANIM",
    "YBA\ufffdES": "YBAÑES",
    "MICA\ufffdA": "MICAÑA",
    "DONACI\ufffdN": "DONACION",       # Donación
    "Y\ufffd\ufffdEZ": "YAÑEZ",        # MAGIA FORENSE: Doble ruptura (YÁÑEZ)
    "URDI\ufffdOLA": "URDIÑOLA",
    "QU\ufffdO": "QUIÑO",
    "CANCELL\ufffdO": "CANCELLIÑO",
    "ECODISE\ufffdO": "ECODISEÑO",
    "M\ufffdDICA": "MEDICA",           # Médica
    "ECODISE\ufffd": "ECODISEÑO",      # Autocompletado
    "APANGUE\ufffd": "APANGUEÑO",      # Autocompletado
    "CASTA\ufffdAR": "CASTAÑAR",
    "CASTELLA\ufffd": "CASTELLANO",    # Autocompletado
    "PACE\ufffdITO": "PACEÑITO",
    "I\ufffdEGUEZ": "IÑEGUEZ",
    "HOR\ufffdN": "HORAN",             # Horán
    "SO\ufffdALES": "SOÑALES",
    "CA\ufffdIL": "CAÑIL",
    "PORTELL\ufffdA": "PORTELLIÑA",
    "ARP\ufffdO": "ARPIÑO",
    "VILLACA\ufffdAS": "VILLACAÑAS",
    "G\ufffdNTER": "GUNTER",           # Diéresis (Günter)
    "AG\ufffdERA": "AGUERA",           # Diéresis (Agüera)
    "VA\ufffdUELOS": "VAÑUELOS",
    "CANTE\ufffdS": "CANTEÑOS",        # Autocompletado
    # Lote 16: Nombres alemanes, Lugares autocompletados y Apellidos Agudos
    "H\ufffdPFL": "HOPFL",             # Diéresis (Höpfl)
    "PRETE\ufffdIDAS": "PRETEÑIDAS",
    "LUDE\ufffdA": "LUDEÑA",
    "SEA\ufffdES": "SEAÑES",
    "MU\ufffdUZ": "MUÑUZ",
    "PREVENCI\ufffd": "PREVENCION",    # Autocompletado
    "IRA\ufffdETA": "IRAÑETA",
    "NAVIDE\ufffdO": "NAVIDEÑO",
    "CARLI\ufffdETA": "CARLIÑETA",
    "ALC\ufffdNTAR": "ALCANTARA",      # Autocompletado (Alcántara)
    "RAME\ufffdOS": "RAMEÑOS",
    "TREBL\ufffdO": "TREBLIÑO",
    "PINZ\ufffdN": "PINZON",           # Pinzón
    "GARA\ufffdA": "GARAÑA",
    "M\ufffdSICA": "MUSICA",           # Música
    "SCH\ufffdTZE": "SCHUTZE",         # Diéresis (Schütze)
    "TA\ufffdO": "TAÑO",
    "PE\ufffdALES": "PEÑALES",
    "SO\ufffdAR": "SOÑAR",
    "ARGE\ufffdAL": "ARGEÑAL",
    "CAMI\ufffdN": "CAMION",           # Camión
    "CU\ufffdLLAR": "CUELLAR",         # Cuéllar
    "IGU\ufffdIZ": "IGUÑIZ",
    "DESENGA\ufffd": "DESENGAÑO",      # Autocompletado
    "CASTA\ufffdEIRA": "CASTAÑEIRA",
    "AVELDA\ufffdES": "AVELDAÑES",
    "SE\ufffdORIZ": "SEÑORIZ",
    "MI\ufffdARRO": "MIÑARRO",
    "TA\ufffdA": "TAÑA",
    "G\ufffdNTHER": "GUNTHER",         # Diéresis (Günther)
    "PROPIA\ufffdO": "PROPIAÑO",
    "J\ufffdUREGUI": "JAUREGUI",       # Jáuregui
    "PE\ufffdAMAR": "PEÑAMAR",
    "SE\ufffdALANDIA": "SEÑALANDIA",
    "CAFETER\ufffdA": "CAFETERIA",     # Cafetería
    "FEDI\ufffdAN": "FEDIÑAN",
    "ENRIQUE\ufffdO": "ENRIQUEÑO",     # Autocompletado deductivo visual
    "ORDO\ufffdA": "ORDOÑA",
    "ESTUPI\ufffdAL": "ESTUPIÑAL",
    "PATRI\ufffdN": "PATRION",         # Patrión
    "MI\ufffdAUR": "MIÑAUR",
    "ZARAZ\ufffdA": "ZARAZUA",         # Zarazúa
    "BALMA\ufffdA": "BALMAÑA",
    "VI\ufffdANUEVA": "VIÑANUEVA",
    "GONZAL\ufffdZ": "GONZALEZ",       # Gonzaléz -> Gonzalez
    "CAMA\ufffdEZ": "CAMAÑEZ",
    "COVI\ufffdA": "COVIÑA",
    "DO\ufffdANA": "DOÑANA",
    "TRASLAVI\ufffdO": "TRASLAVIÑO",
    "ORDO\ufffdANA": "ORDOÑANA",
    "BAZ\ufffdN": "BAZAN",             # Bazán
    "PE\ufffdAHERRE": "PEÑAHERRERA",   # Autocompletado
    "MA\ufffdANITAS": "MAÑANITAS",
    "I\ufffdIESTA": "INIESTA",         # Iñiesta -> Iniesta
    "SCH\ufffdTTE": "SCHUTTE",         # Diéresis (Schütte)
    "INGENIER\ufffdA": "INGENIERIA",   # Ingeniería
    "ENDO\ufffdU": "ENDOÑU",
    "VESTINI\ufffdA": "VESTINIÑA",
    "ME\ufffdOS": "MEÑOS",
    "MU\ufffdIVE": "MUÑIVE",
    "DU\ufffdALDS": "DUÑALDS",
    "LI\ufffdEIRO": "LIÑEIRO",
    "FERM\ufffdN": "FERMIN",           # Fermín
    "BUDI\ufffdO": "BUDIÑO",
    "MUI\ufffdEQUITA": "MUIÑEQUITA",
    "AVANPI\ufffdA": "AVANPIÑA",
    "TRIST\ufffdN": "TRISTAN",         # Tristán
    "FISCALE\ufffdO": "FISCALEÑO",
    "MAGALL\ufffdN": "MAGALLON",       # Magallón
    "XALAPE\ufffdA": "XALAPEÑA",
    "CALI\ufffdA": "CALIÑA",
    "MUNGUI\ufffdA": "MUNGUIÑA",
    "SE\ufffdALIZACI": "SEÑALIZACION", # Autocompletado
    "ZAMARR\ufffdN": "ZAMARRON",       # Zamarrón
    "SE\ufffdALMEX": "SEÑALMEX",
    "HERRE\ufffdO": "HERREÑO",
    "CARRE\ufffdA": "CARREÑA",
    "PE\ufffdAFRIA": "PEÑAFRIA",
    "BURGE\ufffdO": "BURGEÑO",
    "TEOTIHUAC\ufffd": "TEOTIHUACAN",  # Autocompletado
    "TRANSVI\ufffdA": "TRANSVIÑA",
    "SIRE\ufffdA": "SIREÑA",
    "ALMAZ\ufffdN": "ALMAZAN",         # Almazán
    "OAXAQUE\ufffd": "OAXAQUEÑO",      # Autocompletado
    "BARQUE\ufffdAS": "BARQUEÑAS",
    "MESTE\ufffdO": "MESTEÑO",
    "DI\ufffdIGUEZ": "DIÑIGUEZ",
    "MARI\ufffdES": "MARIÑES",
    "ALBI\ufffdANA": "ALBIÑANA",
    "CESE\ufffdO": "CESEÑO",
    "SURUA\ufffdEZ": "SURUAÑEZ",
    "ENCARNACI\ufffd": "ENCARNACION",  # Autocompletado
    "CALA\ufffdA": "CALAÑA",
    "MANTI\ufffdCOR": "MANTIÑCORA",    # Autocompletado deductivo
    "PARDI\ufffdEZ": "PARDIÑEZ",
    "SI\ufffdIGO": "SIÑIGO",
    "ANTO\ufffdETA": "ANTOÑETA",
    "COSLI\ufffdA": "COSLIÑA",
    "ILLAI\ufffdEZ": "ILLAIÑEZ",
    # Lote 17: Académicos, Médicos, Doble Corrupción y Autocompletados
    "BA\ufffdES": "BAÑES",
    "JARZLI\ufffdHO": "JARZLIÑHO",
    "VESU\ufffdA": "VESUÑA",
    "GARCI\ufffdA": "GARCIA",
    "CASTA\ufffd\ufffd": "CASTAÑO",     # MAGIA FORENSE: Doble ruptura
    "CA\ufffdIVE": "CAÑIVE",
    "JIMEN\ufffdZ": "JIMENEZ",         # Jiménez
    "CASTA\ufffdEDO": "CASTAÑEDO",
    "INFANTER\ufffd": "INFANTERIA",    # Autocompletado (Infantería)
    "COMISI\ufffdN": "COMISION",       # Comisión
    "CA\ufffdIZAREZ": "CAÑIZAREZ",
    "MEDELLI\ufffdN": "MEDELLIN",      # Medellín
    "CASTA\ufffdUEL": "CASTAÑUELA",    # Autocompletado
    "MARTIG\ufffdON": "MARTIGÑON",
    "K\ufffdCHEN": "KUCHEN",           # Diéresis (Küchen)
    "WONGI\ufffdIS": "WONGIÑIS",
    "GRALI\ufffdO": "GRALIÑO",
    "CANCELACI\ufffd": "CANCELACION",  # Autocompletado
    "SATE\ufffdA": "SATEÑA",
    "G\ufffdICOZA": "GUICOZA",         # Diéresis (Güicoza)
    "MAGARLI\ufffdOS": "MAGARLIÑOS",
    "MAGA\ufffdAS": "MAGAÑAS",
    "BORGO\ufffdON": "BORGOÑON",
    "SISE\ufffdA": "SISEÑA",
    "CASTREJI\ufffdN": "CASTREJON",
    "TRASBLI\ufffdA": "TRASBLIÑA",
    "URDA\ufffdEZ": "URDAÑEZ",
    "PAY\ufffdN": "PAYAN",             # Payán
    "PROHA\ufffdO": "PROHAÑO",
    "PE\ufffdALBER": "PEÑALBER",
    "BAIL\ufffdN": "BAILEN",           # Bailén
    "RODRLI\ufffdGUE": "RODRLIGUEZ",   # Autocompletado deductivo
    "DO\ufffdAZ": "DOÑAZ",
    "ROLDI\ufffdN": "ROLDIN",
    "A\ufffdREA": "AUREA",             # Áurea
    "PATI\ufffdA": "PATIÑA",
    "QUER\ufffdTARO": "QUERETARO",     # Querétaro
    "MIGRLI\ufffdO": "MIGRLIÑO",
    "ADJUDICACI\ufffd": "ADJUDICACION",# Autocompletado
    "SOTOBA\ufffdAD": "SOTOBAÑADO",    # Autocompletado
    "KARLI\ufffdHO": "KARLIÑHO",
    "ACAPULQUE\ufffd": "ACAPULQUEÑO",  # Autocompletado
    "BA\ufffdS": "BAÑOS",              # Autocompletado visual
    "V\ufffdA": "VIA",                 # Vía
    "YECE\ufffdA": "YECEÑA",
    "CA\ufffdAZ": "CAÑAZ",
    "RIBERE\ufffdO": "RIBEREÑO",
    "SERRETE\ufffdO": "SERRETEÑO",
    "T\ufffdCNICA": "TECNICA",         # Técnica
    "J\ufffdRAND": "JURAND",           # Diéresis (Jürand)
    "F\ufffdGUEMAN": "FUGUEMAN",       # Diéresis (Fügueman)
    "BICU\ufffdA": "BICUÑA",
    "MOZOPE\ufffdA": "MOZOPEÑA",
    "C\ufffdMPUTO": "COMPUTO",         # Cómputo
    "MONSE\ufffdOR": "MONSEÑOR",
    "ZUMBE\ufffdO": "ZUMBEÑO",
    "GALI\ufffdN": "GALION",
    "BILLASE\ufffdOR": "BILLASEÑOR",   # Conservamos la B original
    "Y\ufffdIGUES": "YÑIGUES",
    "MARDO\ufffdO": "MARDOÑO",
    "CIG\ufffdE": "CIGUE",             # Diéresis (Cigüe)
    "GAMI\ufffdIO": "GAMIÑIO",
    "MU\ufffdECA": "MUÑECA",
    "SE\ufffdORIALES": "SEÑORIALES",
    "RIZUE\ufffdO": "RIZUEÑO",
    "GR\ufffdNBERG": "GRUNBERG",       # Diéresis (Grünberg)
    "ERREHMU\ufffdZ": "ERREHMUÑZ",
    "ENDA\ufffdO": "ENDAÑO",
    "MAGA\ufffdES": "MAGAÑES",
    "ERSE\ufffdOZ": "ERSEÑOZ",
    "PI\ufffdAR": "PIÑAR",
    "CHEG\ufffdES": "CHEGUES",         # Diéresis (Chegües)
    "BIBA\ufffdO": "BIBAÑO",
    "MO\ufffdET": "MOÑET",
    "SANTAMAR\ufffd": "SANTAMARIA",    # Autocompletado
    "BUSQUE\ufffdO": "BUSQUEÑO",
    "FERREPE\ufffdA": "FERREPEÑA",
    "UNIVERSIT\ufffd": "UNIVERSITARIO", # Autocompletado
    "SOI\ufffdADORA": "SOIÑADORA",
    "SOLOI\ufffdO": "SOLOIÑO",
    "LIZ\ufffdRRAGA": "LIZARRAGA",     # Lizárraga
    "SACHLI\ufffdA": "SACHLIÑA",
    "SCHORE\ufffdO": "SCHOREÑO",
    "TRAUMATOLOG\ufffd": "TRAUMATOLOGIA", # Autocompletado
    "ACAD\ufffdMICA": "ACADEMICA",     # Académica
    "BOLO\ufffdA": "BOLOÑA",
    "FISIOLOG\ufffdA": "FISIOLOGIA",   # Fisiología
    "MONZ\ufffdN": "MONZON",           # Monzón
    "P\ufffdRAMO": "PARAMO",           # Páramo
    "VLI\ufffdOLO": "VLIÑOLO",
    "HONTA\ufffdON": "HONTAÑON",
    "ESTA\ufffdO": "ESTAÑO",
    "BU\ufffdUEL": "BUÑUEL",           # Buñuel
    "LING\ufffdISTICO": "LINGUISTICO", # Diéresis (Lingüístico)
    "CASAG\ufffdON": "CASAGUON",
    "PAULLI\ufffdO": "PAULLIÑO",
    "CASTAI\ufffdOLA": "CASTAÑOLA",    # Autocompletado/Corrección
    "PO\ufffdOS": "POÑOS",
    "TEMISQUE\ufffd": "TEMISQUEÑO",    # Autocompletado
    "IVAI\ufffdES": "IVAIÑES",
    # Lote 18: Procesos Administrativos (Operación HR/Legal), Dobles rupturas y Gentilicios
    "COMPA\ufffdY": "COMPAÑY",         # Variante de Company / Compañía
    "MACEDO\ufffdA": "MACEDOÑA",
    "GADA\ufffdON": "GADAÑON",
    "ISLE\ufffdOS": "ISLEÑOS",
    "FESTINLI\ufffdOS": "FESTINLIÑOS",
    "10D\ufffdAS": "10DIAS",           # Operativo
    "MURGU\ufffdA": "MURGUIA",         # Murguía
    "IBARG\ufffdENG": "IBARGUENGOITIA", # Autocompletado deductivo
    "CORRECCI\ufffd": "CORRECCION",    # Autocompletado
    "ALIMENTACI\ufffd": "ALIMENTACION", # Autocompletado
    "I\ufffdIQUEZ": "IÑIQUEZ",
    "REQUISICI\ufffd": "REQUISICION",  # Autocompletado
    "TECNOBA\ufffd": "TECNOBAÑO",      # Autocompletado
    "G\ufffdNDARA": "GANDARA",         # Gándara
    "READAPTACI\ufffd": "READAPTACION", # Autocompletado
    "ALC\ufffdZAR": "ALCAZAR",         # Alcázar
    "BARAGA\ufffdA": "BARAGAÑA",
    "PARAISE\ufffdOS": "PARAISEÑOS",
    "LIQUIDA\ufffd\ufffd": "LIQUIDACION", # MAGIA FORENSE: Doble ruptura
    "CULIACI\ufffdN": "CULIACAN",      # Corrección visual (Culiacán)
    "GEN\ufffdRICO": "GENERICO",       # Genérico
    "GRI\ufffdAN": "GRIÑAN",
    "PAULE\ufffdO": "PAULEÑO",
    "TAMPIQUE\ufffd": "TAMPIQUEÑO",    # Autocompletado
    "CE\ufffdERA": "CEÑERA",
    "CA\ufffdONEZ": "CAÑONEZ",
    "ARL\ufffdEZ": "ARLIEZ",
    "MOSOPE\ufffdA": "MOSOPEÑA",
    "GARA\ufffdONE": "GARAÑONES",      # Autocompletado
    "BALI\ufffdOS": "BALIÑOS",
    "ERE\ufffdA": "EREÑA",
    "PE\ufffdOLITO": "PEÑOLITO",
    "BUTRAGUE\ufffd": "BUTRAGUEÑO",    # Autocompletado
    "ART\ufffdCULOS": "ARTICULOS",     # Artículos
    "MUI\ufffdECO": "MUIÑECO",
    "AGROCA\ufffdA": "AGROCAÑA",
    "ALBARRI\ufffdN": "ALBARRIÑON",
    "D\ufffdNNPHAR": "DUNNPHARM",      # Autocompletado (Dünnpharm)
    "CAMU\ufffdES": "CAMUÑES",
    "BRL\ufffdEZ": "BRLIEZ",
    "RETO\ufffdOS": "RETOÑOS",
    "ESPECT\ufffdCU": "ESPECTACULO",   # Autocompletado
    "LE\ufffdATEROS": "LEÑATEROS",
    "HOTO\ufffdEL": "HOTOÑEL",
    "ESCA\ufffdO": "ESCAÑO",
    "PI\ufffdATAS": "PIÑATAS",
    "MONTA\ufffdAN": "MONTAÑAN",
    "LAVI\ufffdO": "LAVIÑO",
    "EXTRA\ufffdO": "EXTRAÑO",
    "VLI\ufffdAO": "VLIÑAO",
    "MOSLI\ufffdOZ": "MOSLIÑOZ",
    "PE\ufffdALUER": "PEÑALUER",
    "VALLARTE\ufffd": "VALLARTEÑO",    # Autocompletado
    "BARA\ufffdA": "BARAÑA",
    "VLI\ufffdEIRA": "VLIÑEIRA",
    "\ufffdERE": "ÑERE",               # Terminación suelta
    "GER\ufffdNIMO": "GERONIMO",       # Gerónimo
    "PERIF\ufffdRICC": "PERIFERICO",   # Corrección de typo de origen
    "MULTIDISE\ufffd": "MULTIDISEÑO",  # Autocompletado
    "LUISHLI\ufffdO": "LUISHLIÑO",
    "KEI\ufffdA": "KEIÑA",
    "LEAI\ufffdIZ": "LEAIÑIZ",
    "ROJE\ufffdA": "ROJEÑA",
    "JESSE\ufffdA": "JESSEÑA",
    "MOREI\ufffdO": "MOREIÑO",
    "JARE\ufffdO": "JAREÑO",
    "INTERLING\ufffd": "INTERLINGUA",  # Autocompletado deductivo
    "PINTE\ufffdO": "PINTEÑO",
    "MUZLI\ufffdO": "MUZLIÑO",
    "REGLI\ufffdN": "REGLION",
    "OPTIMIZACI\ufffd": "OPTIMIZACION", # Autocompletado
    "ORGANIZACI\ufffd": "ORGANIZACION", # Autocompletado
    "TERMINACI\ufffd": "TERMINACION",  # Autocompletado
    "Y\ufffdPEZ": "YEPEZ",             # Yépez
    "SAMULI\ufffdO": "SAMULIÑO",
    "KANCA\ufffdA": "KANCAÑA",
    "GATE\ufffdO": "GATEÑO",
    "GARGA\ufffdITIS": "GARGAÑITIS",
    "ANLI\ufffdUU": "ANLIÑUU",
    "REVOLUCI\ufffd": "REVOLUCION",    # Autocompletado
    "CIG\ufffdENZA": "CIGUENZA",       # Diéresis (Cigüenza)
    "AMPLIACI\ufffdN": "AMPLIACION",   # Ampliación
    "KARY\ufffdO": "KARYÑO",
    "CANDAME\ufffd": "CANDAMEÑO",      # Autocompletado
    "OLI\ufffdN": "OLION",             # Olión
    "AG\ufffdITA": "AGUITA",           # Diéresis (Agüita)
    "TUNG\ufffdI": "TUNGUI",           # Diéresis (Tungüi)
    "BRLI\ufffdAS": "BRLIÑAS",
    "CA\ufffdAMO": "CAÑAMO",
    "CHAV\ufffdZ": "CHAVEZ",           # Chávez
    "AVERTA\ufffdO": "AVERTAÑO",
    "INVESTIGACI\ufffd": "INVESTIGACION", # Autocompletado
    "MARTI\ufffdNEZ": "MARTINEZ",      # MAGIA FORENSE: Typo en base origen (Martiñnez)
    "QUINZLI\ufffdO": "QUINZLIÑO",
    "BENTURE\ufffd": "BENTUREÑO",      # Autocompletado
    "HUATUSQUE\ufffd": "HUATUSQUEÑO",  # Autocompletado
    "LEJIDE\ufffdO": "LEJIDEÑO",
    # Lote 19: Nombres prehispánicos (Xóchitl), Dobles Rupturas (Ibáñez) y Diéresis
    "GOM\ufffdZ": "GOMEZ",             # Gómez
    "I\ufffdAR": "IÑAR",
    "I\ufffdARRITO": "IÑARRITO",
    "IB\ufffd\ufffdEZ": "IBAÑEZ",      # MAGIA FORENSE: Doble ruptura (Ibáñez)
    "YAG\ufffdES": "YAGUES",           # Diéresis (Yagües)
    "P\ufffdB": "PUB",                 # Púb
    "CABA\ufffdAZ": "CABAÑAZ",
    "AG\ufffdEDA": "AGUEDA",           # Águeda
    "VILLACE\ufffdOR": "VILLACEÑOR",
    "AGU\ufffdAGA": "AGUIÑAGA",        # Corrección de typo origen
    "MAG\ufffdINA": "MAGUINA",         # Diéresis (Magüina)
    "HERREJ\ufffdN": "HERREJON",       # Herrejón
    "SALD\ufffdVAR": "SALDIVAR",       # Saldívar
    "NICARAG\ufffdE": "NICARAGUENSE",  # Autocompletado (Nicaragüense)
    "PEDIATR\ufffdA": "PEDIATRIA",     # Pediatría
    "PAV\ufffdN": "PAVON",             # Pavón
    "GRE\ufffdITAS": "GREÑITAS",
    "CHICH\ufffdN": "CHICHEN",         # Chichén
    "I\ufffdIGA": "IÑIGA",
    "CARRAMI\ufffdA": "CARRAMIÑA",
    "TRIVLI\ufffdOS": "TRIVLIÑOS",
    "JERSLI\ufffdHIO": "JERSLIÑHIO",
    "COTO\ufffdIETO": "COTOÑIETO",
    "PLI\ufffdERES": "PLIÑERES",
    "ZOI\ufffdANEZ": "ZOIÑANEZ",
    "PELI\ufffdEZ": "PELIÑEZ",
    "GUASAVE\ufffdA": "GUASAVEÑA",
    "JAI\ufffdEZ": "JAIÑEZ",
    "ZUZA\ufffdA": "ZUZAÑA",
    "ILVE\ufffdO": "ILVEÑO",
    "PLI\ufffdIAN": "PLIÑIAN",
    "MUI\ufffdU": "MUIÑU",
    "RIVE\ufffdA": "RIVEÑA",
    "TOBI\ufffdN": "TOBION",           # Tobión
    "CHAI\ufffdICUEN": "CHAIÑICUEN",
    "GOI\ufffdE": "GOIÑE",
    "VISENTE\ufffdO": "VISENTEÑO",
    "INTERDISE\ufffd": "INTERDISEÑO",  # Autocompletado
    "FORMA\ufffdUK": "FORMAÑUK",
    "OTHI\ufffdN": "OTHION",           # Othión
    "PAI\ufffdIAGUA": "PAIÑIAGUA",     # Variante de Paniagua
    "M\ufffdHETS": "MUHETS",           # Diéresis (Mühets)
    "CHOIXE\ufffdOS": "CHOIXEÑOS",
    "YEZE\ufffdA": "YEZEÑA",
    "NUI\ufffdIZ": "NUIÑIZ",
    "TRAVLI\ufffdO": "TRAVLIÑO",
    "G\ufffdBEL": "GOBEL",             # Diéresis (Göbel)
    "GIBRI\ufffdN": "GIBRAN",          # Corrección visual (Gibrán)
    "PEQUE\ufffdIN": "PEQUEÑIN",
    "GARZI\ufffdN": "GARZON",          # Corrección de typo origen (Garzón)
    "HERNANDI\ufffd": "HERNANDIÑEZ",   # Autocompletado deductivo
    "G\ufffdIDMAN": "GUIDMAN",         # Diéresis (Güidman)
    "LISE\ufffdA": "LISEÑA",
    "AGULI\ufffdEGA": "AGULIÑEGA",
    "ORE\ufffdA": "OREÑA",
    "BLACE\ufffdO": "BLACEÑO",
    "H\ufffdTTICH": "HUTTICH",         # Diéresis (Hüttich)
    "HIP\ufffdLITO": "HIPOLITO",       # Hipólito
    "VLI\ufffdEGRA": "VLIÑEGRA",
    "ODOI\ufffdA": "ODOIÑA",
    "ANTOI\ufffdITA": "ANTOIÑITA",
    "RIVERE\ufffdOS": "RIVEREÑOS",
    "ARREGU\ufffdN": "ARREGUIN",       # Arreguín
    "TOI\ufffdOALEXIS": "TOÑOALEXIS",  # Limpieza de typo de captura
    "YAI\ufffdIAK": "YAIÑIAK",
    "HERMLI\ufffdITA": "HERMLIÑITA",
    "CEZE\ufffdA": "CEZEÑA",
    "ORAI\ufffdEGUES": "ORAIÑEGUES",
    "ILBE\ufffdO": "ILBEÑO",
    "ANTILLI\ufffdN": "ANTILLON",      # Corrección de typo origen (Antillón)
    "BIE\ufffdKO": "BIEÑKO",
    "DISE\ufffdADA": "DISEÑADA",
    "YHAIRSLI\ufffdO": "YHAIRSLIÑO",
    "BARRANQUE\ufffd": "BARRANQUEÑO",  # Autocompletado
    "MUI\ufffdOSCAN": "MUIÑOSCAN",
    "ALPA\ufffdES": "ALPAÑES",
    "X\ufffdCHITL": "XOCHITL",         # Xóchitl
    "AZOI\ufffdOZ": "AZOIÑOZ",
    "COUTLI\ufffdIO": "COUTLIÑIO",
    "BAI\ufffdEROS": "BAIÑEROS",
    "JI\ufffdQUEZ": "JIQUEZ",          # Jíquez
    "EDYH\ufffdO": "EDYÑO",            # Corrección visual
    "MUCLI\ufffdOS": "MUCLIÑOS",
    "HERMLI\ufffdA": "HERMLIÑA",
    "ITAI\ufffdUU": "ITAIÑUU",
    "EURE\ufffdA": "EUREÑA",
    "CAI\ufffdESTRO": "CAIÑESTRO",
    "BAI\ufffdUELO": "BAÑUELO",         # Corrección de captura
    "RCASTA\ufffdED": "RCASTAÑEDA",    # Autocompletado
    "YETZE\ufffdA": "YETZEÑA",
    "M\ufffdNZEL": "MUNZEL",           # Diéresis (Münzel)
    "PAROAI\ufffdO": "PAROAIÑO",
    "ORDA\ufffdEZ": "ORDAÑEZ",
    "ORVLI\ufffdA": "ORVLIÑA",
    "ENDEMAI\ufffdO": "ENDEMAIÑO",
    "LIA\ufffdOS": "LIAÑOS",
    "NARANJE\ufffdA": "NARANJEÑA",
    "GRICE\ufffdA": "GRICEÑA",
    "DISE\ufffdARTIC": "DISEÑARTIC",
    "ATENGUE\ufffdO": "ATENGUEÑO",
    # Lote 20: Fechas rotas, Autocompletados corporativos, Dobles rupturas y Diéresis
    "SECCI\ufffdN": "SECCION",         # Sección
    "LEOVA\ufffdE": "LEOVAÑE",
    "CAMU\ufffdO": "CAMUÑO",
    "SAU\ufffdE": "SAUÑE",
    "YESSE\ufffdA": "YESSEÑA",
    "PER\ufffdODO": "PERIODO",         # Período
    "PERIF\ufffdRICC": "PERIFERICO",   # Corrección visual/typo origen
    "AMORTIZACI\ufffd": "AMORTIZACION", # Autocompletado
    "ENSUE\ufffdOS": "ENSUEÑOS",
    "VILLAL\ufffdN": "VILLALON",       # Villalón
    "JORD\ufffdN": "JORDAN",           # Jordán
    "ENSE\ufffdANZA": "ENSEÑANZA",
    "CA\ufffdETA": "CAÑETA",
    "INVITACI\ufffdN": "INVITACION",   # Invitación
    "AMAGUA\ufffdA": "AMAGUAÑA",
    "JOAOSLI\ufffdO": "JOAOSLIÑO",
    "VA\ufffdALES": "VAÑALES",
    "ANG\ufffdIZ": "ANGUIZ",           # Diéresis (Angüiz)
    "EGUL\ufffdO": "EGULIÑO",
    "CRUZE\ufffdO": "CRUZEÑO",
    "CATAL\ufffdN": "CATALAN",         # Catalán
    "SAG\ufffdEZ": "SAGUEZ",           # Diéresis (Sagüez)
    "ACTIPE\ufffdA": "ACTIPEÑA",
    "GL\ufffdCKSKINI": "GLUCKSKINI",   # Diéresis (Glückskini)
    "ALBA\ufffdILES": "ALBAÑILES",
    "GARC\ufffdS": "GARCES",           # Garcés
    "I\ufffdIGES": "IÑIGES",
    "FEDERACI\ufffd": "FEDERACION",    # Autocompletado
    "MONTA\ufffdON": "MONTAÑON",
    "TH\ufffdRMER": "THURMER",         # Diéresis (Thürmer)
    "RAY\ufffdN": "RAYON",             # Rayón
    "LESL\ufffdSKA": "LESLINSKA",      # Corrección visual (Leslińska)
    "BIBE\ufffdA": "BIBEÑA",
    "REDISE\ufffdO": "REDISEÑO",
    "A\ufffdUEZ": "AÑUEZ",
    "G\ufffdIRIZA": "GUIRIZA",         # Diéresis (Güiriza)
    "GUTIERR\ufffdZ": "GUTIERREZ",     # Gutiérrez
    "BORGO\ufffdA": "BORGOÑA",
    "19\ufffd09": "19-09",             # Corrección de fecha/folio corrupto
    "BRICE\ufffdA": "BRICEÑA",
    "ALPE\ufffdASA": "ALPEÑASA",
    "MU\ufffd\ufffdZ": "MUÑOZ",        # MAGIA FORENSE: Doble ruptura
    "BA\ufffdUL": "BAÑUL",
    "G\ufffdENDALY": "GUENDALY",       # Diéresis (Güendaly)
    "AJALCRLI\ufffdA": "AJALCRLIÑA",
    "VRISE\ufffdO": "VRISEÑO",
    "ROSE\ufffdO": "ROSEÑO",
    "TREVLI\ufffdOS": "TREVLIÑOS",
    "FINCA\ufffdA": "FINCAÑA",
    "SAI\ufffdA": "SAIÑA",
    "TESCARE\ufffdO": "TESCAREÑO",
    "QUI\ufffdON": "QUIÑON",
    "I\ufffdA": "IÑA",
    "FARI\ufffdAS": "FARIÑAS",
    "SUBDIRECCI\ufffd": "SUBDIRECCION", # Autocompletado
    "DOMPE\ufffdO": "DOMPEÑO",
    "C\ufffdCERES": "CACERES",         # Cáceres
    "ZERCLI\ufffdO": "ZERCLIÑO",
    "VIRGLI\ufffdA": "VIRGLIÑA",
    "BLASE\ufffdO": "BLASEÑO",
    "LAMORE\ufffdA": "LAMOREÑA",
    "G\ufffdILLO": "GUILLO",           # Diéresis (Güillo)
    "FUENTE\ufffdO": "FUENTEÑO",
    "VIRI\ufffdEZ": "VIRIÑEZ",
    "WISHI\ufffdACK": "WISHIÑACK",
    "TERRACE\ufffdO": "TERRACEÑO",
    "CURACI\ufffdN": "CURACION",       # Curación
    "ARTAG\ufffdAN": "ARTAGNAN",       # Corrección visual (d'Artagnan / Artagñan)
    "ZUXA\ufffdA": "ZUXAÑA",
    "LUDE\ufffdA": "LUDEÑA",           # (Ludueña / Ludeña)
    "ANTIG\ufffdEDA": "ANTIGUEDAD",    # Autocompletado (Antigüedad)
    "AGULI\ufffdADA": "AGULIÑADA",
    "ENEDLI\ufffdO": "ENEDLIÑO",
    "COPTLI\ufffdO": "COPTLIÑO",
    "PEZTI\ufffdA": "PEZTIÑA",
    "G\ufffdIZAR": "GUIZAR",           # Diéresis (Güízar)
    "FAI\ufffdA": "FAIÑA",
    "ABELDA\ufffdES": "ABELDAÑES",
    "ALI\ufffdN": "ALION",             # Alión
    "ELEBE\ufffdO": "ELEBEÑO",
    "SALI\ufffdZ": "SALIOZ",           # Corrección visual
    "BARREALE\ufffd": "BARREALEÑO",    # Autocompletado
    "HORTE\ufffdO": "HORTEÑO",
    "QUI\ufffdONES": "QUIÑONES",
    "BEHTA\ufffdA": "BEHTAÑA",
    "BIBA\ufffdOS": "BIBAÑOS",
    "ZU\ufffdEGA": "ZUÑEGA",
    "TANDLI\ufffdO": "TANDLIÑO",
    "XU\ufffdU": "XUÑU",
    "BEGO\ufffdE": "BEGOÑE",
    "PAI\ufffdAFOR": "PAIÑAFOR",
    "CASA\ufffdEJA": "CASAÑEJA",
    "COMPA\ufffdET": "COMPAÑET",
    "TUXPE\ufffdA": "TUXPEÑA",
    "BERISTA\ufffdE": "BERISTAINE",    # Corrección visual (Beristaine)
    "SUE\ufffdA": "SUEÑA",
    "CAZA\ufffdA": "CAZAÑA",
    "R\ufffdTTER": "RUTTER",           # Diéresis (Rütter)
    "PARRALE\ufffd": "PARRALEÑO",      # Autocompletado
    # Lote 21: Doble ruptura (MAÑÓN), Autocompletados y Diéresis
    "SAPI\ufffdA": "SAPIÑA",
    "G\ufffdIDA": "GUIDA",             # Diéresis (Güida)
    "ANG\ufffdES": "ANGUES",
    "VILLASA\ufffdA": "VILLASAÑA",
    "GONZ\ufffdLES": "GONZALES",       # Gonzáles
    "CA\ufffdOS": "CAÑOS",
    "MU\ufffdUA": "MUÑUA",
    "GIJ\ufffdN": "GIJON",             # Gijón
    "NU\ufffdER": "NUÑER",
    "IGARTE\ufffdO": "IGARTEÑO",
    "F\ufffdRSTER": "FORSTER",         # Diéresis (Förster)
    "TROTASUE\ufffd": "TROTASUEÑOS",   # Autocompletado
    "LIC\ufffdN": "LICON",             # Licón
    "DEVOLUCI\ufffd": "DEVOLUCION",    # Autocompletado
    "CAMPL\ufffdAS": "CAMPLIÑAS",
    "\ufffdURE": "ÑURE",
    "YASM\ufffdN": "YASMIN",           # Yasmín
    "KARA\ufffdICAS": "KARAÑICAS",
    "CA\ufffdOLES": "CAÑOLES",
    "CORT\ufffdZ": "CORTEZ",           # Cortéz
    "WRE\ufffdA": "WREÑA",
    "ROSAL\ufffdA": "ROSALIA",         # Rosalía
    "MON\ufffdRREZ": "MONARREZ",       # Monárrez
    "SE\ufffdALINE": "SEÑALINEA",      # Autocompletado deductivo
    "ANT\ufffdNEZ": "ANTUNEZ",         # Antúnez
    "VILLAGR\ufffdN": "VILLAGRAN",     # Villagrán
    "S\ufffdNCER": "SANCER",           # Sáncer
    "GARRAMU\ufffd": "GARRAMUÑO",      # Autocompletado
    "BAT\ufffdN": "BATAN",             # Batán
    "BU\ufffdA": "BUÑA",
    "CA\ufffdENGUEZ": "CAÑENGUEZ",
    "JAIRZHL\ufffdO": "JAIRZHLIÑO",
    "CARL\ufffdAN": "CARLIAN",
    "ARGUL\ufffdE": "ARGULIE",
    "C\ufffdLULA": "CELULA",           # Célula
    "U\ufffdAS": "UÑAS",
    "GATU\ufffdALES": "GATUÑALES",
    "BIZALU\ufffdA": "BIZALUÑA",
    "GRE\ufffdAS": "GREÑAS",
    "PASE\ufffdO": "PASEÑO",
    "MOTA\ufffdO": "MOTAÑO",
    "KANT\ufffdN": "KANTON",           # Kantón
    "BR\ufffdCKEN": "BRUCKEN",         # Diéresis (Brücken)
    "BOL\ufffdVAR": "BOLIVAR",         # Bolívar
    "PL\ufffdUELO": "PLIÑUELO",
    "M\ufffdBLEX": "MUBLEX",           # Diéresis (Müblex)
    "FIA\ufffdO": "FIAÑO",
    "ESCAND\ufffdN": "ESCANDON",       # Escandón
    "VISO\ufffdE": "VISOÑE",
    "OMA\ufffdON": "OMAÑON",
    "SE\ufffdORITA": "SEÑORITA",       # Señorita
    "VLI\ufffdOL": "VLIÑOL",
    "AGRODISE\ufffd": "AGRODISEÑO",    # Autocompletado
    "ZURI\ufffdE": "ZURIÑE",
    "TRASVL\ufffdO": "TRASVLIÑO",
    "SE\ufffdALESA": "SEÑALESA",
    "RUBL\ufffdOZ": "RUBLIÑOZ",
    "BIBL\ufffdE": "BIBLIE",           # Biblié
    "MA\ufffd\ufffdN": "MAÑON",        # MAGIA FORENSE: Doble ruptura (MAÑÓN)
    "D\ufffdLARES": "DOLARES",         # Dólares
    "ARG\ufffdELLEZ": "ARGUELLEZ",     # Diéresis (Argüellez)
    "EU\ufffdN": "EUAN",               # Euán
    "NORTE\ufffdOS": "NORTEÑOS",
    "YUNU\ufffdN": "YUNUEN",           # Yunuén
    "ME\ufffdESTOS": "MEÑESTOS",
    "ACAD\ufffdMICO": "ACADEMICO",     # Académico
    "TORIBE\ufffdO": "TORIBEÑO",
    "D\ufffdBORA": "DEBORA",           # Débora
    "EJ\ufffdRCITO": "EJERCITO",       # Ejército
    "CRIS\ufffdSTOM": "CRISOSTOMO",    # Autocompletado (Crisóstomo)
    "SE\ufffdUELO": "SEÑUELO",
    "VERD\ufffdN": "VERDON",           # Verdón
    "VLI\ufffdATEROS": "VLIÑATEROS",
    "OCO\ufffdA": "OCOÑA",
    "CALIFORNE\ufffd": "CALIFORNEÑO",  # Autocompletado
    "TAMPIQUE\ufffd": "TAMPIQUEÑO",    # Autocompletado
    "TO\ufffdIFEL": "TOÑIFEL",
    "KA\ufffdEZ": "KAÑEZ",
    "ABD\ufffdN": "ABDON",             # Abdón
    "PIRA\ufffdA": "PIRAÑA",
    "TODOSANTE\ufffd": "TODOSANTEÑO",  # Autocompletado
    "CORPE\ufffdO": "CORPEÑO",
    "YLLA\ufffdIS": "YLLAÑIS",
    "SALDA\ufffdAR": "SALDAÑAR",
    "TO\ufffdOS": "TOÑOS",
    "PA\ufffdO": "PAÑO",
    "CA\ufffdAK": "CAÑAK",
    "PIC\ufffdN": "PICON",             # Picón
    "MONTA\ufffdOS": "MONTAÑOS",
    "CA\ufffdARETE": "CAÑARETE",
    "LA\ufffdAS": "LAÑAS",
    "INNOVACI\ufffd": "INNOVACION",    # Autocompletado
    "MONTELBE\ufffd": "MONTELBEÑO",    # Autocompletado
    "DESE\ufffdOS": "DESEÑOS",
    "REPARACI\ufffd": "REPARACION",    # Autocompletado
    "TE\ufffdIDO": "TEÑIDO",
    "T\ufffdREN": "TUREN",             # Diéresis (Türen)
    "VICU\ufffdOL": "VICUÑOL",
    # Lote 22: Corrección de Typos (Sï¿½CHEZ), Nombres Compuestos y Autocompletados
    "RIG\ufffdACK": "RIGNACK",
    "M\ufffdNCH": "MUNCH",             # Diéresis (Münch)
    "COSTE\ufffdAS": "COSTEÑAS",
    "CR\ufffdDTIO": "CREDITO",         # Corrección de typo origen (Crédtio)
    "ANTIG\ufffdA": "ANTIGUA",         # Diéresis (Antigüa)
    "NUMERO\ufffdD": "NUMERO D",
    "\ufffdFIANZA": "FIANZA",          # Limpieza de basura inicial
    "OREG\ufffdN": "OREGON",           # Oregón
    "ESC\ufffdRGENA": "ESCARGENA",
    "SO\ufffdARTE": "SOÑARTE",
    "DISE\ufffdAIDEA": "DISEÑAIDEA",
    "ZU\ufffdIGAS": "ZUÑIGAS",
    "SE\ufffdEROS": "SEÑEROS",
    "YA\ufffdIN": "YAÑIN",
    "RONALDLI\ufffdC": "RONALDLIÑO",   # Corrección visual
    "GERONTOLI\ufffd": "GERONTOLOGIA", # Autocompletado
    "JUQUILE\ufffdO": "JUQUILEÑO",
    "NU\ufffdOZ": "NUÑOZ",
    "FARF\ufffdN": "FARFAN",           # Farfán
    "MARDO\ufffdA": "MARDOÑA",
    "TEC\ufffdMAC": "TECAMAC",         # Tecámac
    "ORA\ufffdEZ": "ORAÑEZ",
    "COCHII\ufffdERA": "COCHIÑERA",    # Corrección visual
    "NORTE\ufffdISIM": "NORTEÑISIMO",  # Norteñísimo
    "PIEDRE\ufffdA": "PIEDREÑA",
    "TEPIQUE\ufffdAS": "TEPIQUEÑAS",
    "CORPORACII\ufffd": "CORPORACION", # Autocompletado
    "CARIBE\ufffdOS": "CARIBEÑOS",
    "DISE\ufffdAR": "DISEÑAR",
    "VITRODISE\ufffd": "VITRODISEÑO",  # Autocompletado
    "PANTALE\ufffdN": "PANTALEON",     # Pantaleón
    "JUANANTO\ufffd": "JUANANTONIO",   # Autocompletado
    "GRDU\ufffdO": "GRDUÑO",           # Posible Garduño, se respeta la raíz
    "REJI\ufffdN": "REGION",           # Corrección deductiva
    "NA\ufffdELY": "NAYELY",           # Corrección fonética/visual
    "OFIDISE\ufffdO": "OFIDISEÑO",
    "HI\ufffdAH": "HIÑAH",
    "ENGA\ufffdO": "ENGAÑO",
    "CIGUE\ufffdA": "CIGUEÑA",
    "MEIRLI\ufffdO": "MEIRLIÑO",
    "P\ufffdPALO": "PAPALO",           # Pápalo
    "AGRONOMI\ufffd": "AGRONOMIA",     # Autocompletado
    "M\ufffdHLBAUER": "MUHLBAUER",     # Diéresis (Mühlbauer)
    "SE\ufffdALPROY": "SEÑALPROY",
    "B\ufffdLLE": "BULLE",             # Diéresis (Bülle)
    "SERVIEMPE\ufffd": "SERVIEMPEÑO",  # Autocompletado
    "JUR\ufffdDICAS": "JURIDICAS",     # Jurídicas
    "ELI\ufffdSEO": "ELISEO",          # Eliseo
    "GONZA\ufffdEZ": "GONZAÑEZ",
    "BISCALE\ufffdO": "BISCALEÑO",
    "ENSE\ufffdAPRE": "ENSEÑAPRE",
    "PATI\ufffdO": "PATIÑO",
    "CABLI\ufffdHO": "CABLIÑHO",
    "BERTI\ufffdN": "BERTIN",          # Bertín
    "\ufffdU": "ÑU",                   # Terminación huérfana
    "TUXQUE\ufffdA": "TUXQUEÑA",
    "POLIDISE\ufffdC": "POLIDISEÑOS",  # Autocompletado
    "FERRE\ufffdO": "FERREÑO",
    "MARE\ufffdY": "MAREÑY",
    "MUI\ufffdE": "MUIÑE",
    "BOCAMLI\ufffdO": "BOCAMLIÑO",
    "AGLI\ufffdAGA": "AGLIÑAGA",
    "EJECUCLI\ufffdN": "EJECUCION",    # Autocompletado
    "VALLI\ufffdA": "VALLIÑA",
    "GI\ufffdC": "GUIC",               # Diéresis deductiva (Güic)
    "VILLAFA\ufffdIA": "VILLAFAÑIA",
    "SE\ufffdALIZA": "SEÑALIZA",
    "JAIRZIHI\ufffdO": "JAIRZIHIÑO",
    "GR\ufffdNES": "GRUNES",           # Diéresis (Grünes)
    "S\ufffdCHEZ": "SANCHEZ",          # MAGIA FORENSE: Typo de origen curado
    "MONTAG\ufffdE": "MONTAGUE",       # Diéresis (Montagüe)
    "AGROALTE\ufffd": "AGROALTEÑO",    # Autocompletado
    "COITLI\ufffdO": "COITLIÑO",
    "\ufffdES": "ÑES",                 # Terminación huérfana
    "RIA\ufffdAS": "RIAÑAS",
    "NAH\ufffdM": "NAHUM",             # Nahúm
    "VISCALE\ufffdO": "VISCALEÑO",
    "MARLI\ufffdHO": "MARLIÑHO",
    "AGULI\ufffdEAGA": "AGULIÑEAGA",
    "HEN\ufffdNDEZ": "HERNANDEZ",      # Corrección de typo de origen
    "DISE\ufffdADOR": "DISEÑADOR",
    "IGARTE\ufffdA": "IGARTEÑA",
    "OCTODISE\ufffd": "OCTODISEÑO",    # Autocompletado
    "REP\ufffdBLICA": "REPUBLICA",     # República
    "ECOALTE\ufffdA": "ECOALTEÑA",
    "PLI\ufffdAMEX": "PLIÑAMEX",
    "GARCIACABA\ufffd": "GARCIACABAÑA", # Autocompletado deductivo
    "VI\ufffdLDEZ": "VALDEZ",          # Corrección visual (Valdéz)
    "PICE\ufffdO": "PICEÑO",
    "ARAG\ufffdEL": "ARAGUEL",         # Diéresis (Aragüel)
    "VILLASE\ufffdOS": "VILLASEÑOS",
    "NIME\ufffdO": "NIMEÑO",
    "MIO\ufffdO": "MIOÑO",
    "BUITR\ufffdN": "BUITRON",         # Buitrón
    "GLI\ufffdMMER": "GLUMMER",        # Diéresis (Glümmer)
    "MEN\ufffdNDEZ": "MENENDEZ",       # Menéndez
    "MARQUE\ufffdA": "MARQUEÑA",
    "PUBLISE\ufffdAL": "PUBLISEÑAL",
    "AVANDA\ufffdO": "AVANDAÑO",
    "PA\ufffdS": "PAIS",               # País
    # Lote 23: Dobles rupturas (SANTIBÁÑEZ), Typos de captura y Autocompletados Operativos
    "CHALPE\ufffdA": "CHALPEÑA",
    "ZAGUL\ufffdO": "ZAGULIÑO",
    "GALD\ufffdMEZ": "GALDAMEZ",       # Galdámez
    "ALE\ufffdA": "ALEÑA",
    "BU\ufffdUELOS": "BUÑUELOS",
    "BAJ\ufffdO": "BAJIO",             # Bajío
    "HERNA\ufffdND": "HERNANDEZ",      # Autocompletado deductivo
    "GALAV\ufffdZ": "GALAVIZ",         # Galavíz
    "AUTORIZACI\ufffd": "AUTORIZACION",# Autocompletado
    "G\ufffdNZALEZ": "GONZALEZ",       # Typo de origen (Gónzalez)
    "VALIDACI\ufffd": "VALIDACION",    # Autocompletado
    "MEDUE\ufffdA": "MEDUEÑA",
    "B\ufffdJAR": "BEJAR",             # Béjar
    "YVETRASON\ufffd": "YVETRASONA",   # Corrección visual
    "PA\ufffdAMEX": "PAÑAMEX",
    "TABASKE\ufffdIT": "TABASKEÑITA",  # Autocompletado
    "ZU\ufffdGA": "ZUÑIGA",            # Typo de origen (Zúñga)
    "NI\ufffdONAUTA": "NIÑONAUTA",
    "CIGUE\ufffdO": "CIGUEÑO",
    "AT\ufffdN": "ATUN",               # Atún
    "NU\ufffdIEZ": "NUÑEZ",            # Typo de origen (Nuñiez)
    "SANTIABA\ufffd": "SANTIBAÑEZ",    # Autocompletado y typo corregido
    "T\ufffdRMINOS": "TERMINOS",       # Términos
    "CABE\ufffdA": "CABEÑA",
    "MANCE\ufffdIDO": "MANCEÑIDO",
    "XOI\ufffdIJUMU": "XOIÑIJUMU",
    "CADE\ufffdALES": "CADEÑALES",
    "LU\ufffdVANO": "LUEVANO",         # Luévano
    "I\ufffdURRATEG": "IÑURRATEGUI",   # Autocompletado
    "MUI\ufffdIAN": "MUIÑIAN",
    "PAV\ufffdA": "PAVIA",             # Pavía
    "RUISE\ufffdORES": "RUISEÑORES",
    "CUAHUT\ufffdM": "CUAHUTEMOC",     # Autocompletado (Cuahutémoc)
    "ZECE\ufffdA": "ZECEÑA",
    "GUA\ufffdUNA": "GUAÑUNA",
    "SCH\ufffdLER": "SCHULER",         # Diéresis (Schüler)
    "CABA\ufffdERO": "CABAÑERO",
    "\ufffdHERN": "HERNANDEZ",         # Autocompletado y limpieza de inicio
    "ER\ufffdNDIRA": "ERENDIRA",       # Eréndira
    "VLI\ufffdAMATA": "VLIÑAMATA",
    "BARRE\ufffdA": "BARREÑA",
    "SE\ufffdALETIKA": "SEÑALETIKA",   # Señalétika
    "ANTIOQUE\ufffd": "ANTIOQUEÑO",    # Autocompletado
    "HUITR\ufffdN": "HUITRON",         # Huitrón
    "M\ufffdRIAM": "MIRIAM",           # Míriam
    "PE\ufffdATES": "PEÑATES",
    "MUI\ufffdANTE": "MUIÑANTE",
    "PUERTE\ufffdA": "PUERTEÑA",
    "ASOCIACI\ufffd": "ASOCIACION",    # Autocompletado
    "DA\ufffdHU": "DAÑHU",
    "PERIBA\ufffdEZ": "PERIBAÑEZ",
    "IR\ufffdN": "IRAN",               # Irán
    "ALAN\ufffdS": "ALANIS",           # Alanís
    "GONZALE\ufffdA": "GONZALEÑA",
    "PILATU\ufffdA": "PILATUÑA",
    "MARB\ufffdN": "MARBAN",           # Marbán
    "CASTAI\ufffdOZ": "CASTAÑOZ",      # Corrección deductiva
    "LADR\ufffdN": "LADRON",           # Ladrón
    "B\ufffdSICO": "BASICO",           # Básico
    "\ufffdNDEZ": "NDEZ",              # Terminación huérfana
    "LU\ufffdS": "LUIS",               # Luís
    "ACOMPA\ufffdA": "ACOMPAÑA",
    "SANTIB\ufffd\ufffd": "SANTIBAÑEZ",# MAGIA FORENSE: Doble ruptura
    "QU\ufffdMICA": "QUIMICA",         # Química
    "G\ufffdEY": "GUEY",               # Diéresis (Güey)
    "HIGLI\ufffdO": "HIGLIÑO",
    "DESIR\ufffdE": "DESIREE",         # Desirée
    "KARRE\ufffdO": "KARREÑO",
    "AVENIDA\ufffdO": "AVENIDAÑO",
    "OTO\ufffdIEL": "OTOÑIEL",
    "BAZALD\ufffdA": "BAZALDUA",       # Bazaldúa
    "BIOM\ufffdDICA": "BIOMEDICA",     # Biomédica
    "ANTO\ufffdITO": "ANTOÑITO",
    "IVA\ufffdN": "IVAN",              # Corrección de typo de origen
    "SESAI\ufffdAS": "SESAIÑAS",
    "ORTA\ufffdO": "ORTAÑO",
    "TO\ufffdITO": "TOÑITO",
    "GYV\ufffdES": "GYVES",            # Gyvés
    "ENSE\ufffdAR": "ENSEÑAR",
    "TOB\ufffdAS": "TOBIAS",           # Tobías
    "NE\ufffdEZ": "NEÑEZ",
    "GO\ufffdEZ": "GOÑEZ",             # Variante / Typo de Gómez
    "SE\ufffdORITO": "SEÑORITO",
    "SANTONI\ufffd": "SANTONIÑO",      # Autocompletado deductivo
    "MANTA\ufffdO": "MANTAÑO",
    "BERSA\ufffdES": "BERSAÑES",
    "MARSE\ufffdACH": "MARSEÑACH",
    "GAST\ufffdLUM": "GASTELUM",       # Gastélum
    "OTU\ufffdO": "OTUÑO",
    "SCHR\ufffdDER": "SCHRODER",       # Diéresis (Schröder)
    "VLI\ufffdALLONG": "VLIÑALLONGA",  # Autocompletado
    "CAZA\ufffdEZ": "CAZAÑEZ",
    "RONZ\ufffdN": "RONZON",           # Ronzón
    "NAVIDE\ufffdOS": "NAVIDEÑOS",
    "CAR\ufffdCTER": "CARACTER",       # Carácter
    "DEFINICI\ufffdN": "DEFINICION",   # Definición
    "PARASE\ufffdA": "PARASEÑA",
    "PROMARA\ufffdI": "PROMARAÑI",
    "ALZA\ufffdEZ": "ALZAÑEZ",
    "ANTU\ufffdEZ": "ANTUÑEZ",
    # Lote 24: Typos de usuario + Corrupción, Lugares, Diéresis y Profesiones
    "CAASTA\ufffdON": "CAASTAÑON",     # Typo de origen (Doble A)
    "MANDRL\ufffdATO": "MANDRLIATO",
    "GUERRE\ufffdA": "GUERREÑA",
    "BRET\ufffdN": "BRETON",           # Bretón
    "AM\ufffdZQUITA": "AMEZQUITA",     # Amézquita
    "HORTU\ufffdO": "HORTUÑO",
    "SERAFI\ufffdN": "SERAFIN",        # Serafín
    "YE\ufffdEZ": "YEÑEZ",
    "INSTALACI\ufffd": "INSTALACION",  # Autocompletado
    "VIZCA\ufffdNO": "VIZCAINO",       # Vizcaíno
    "ORLANDL\ufffdC": "ORLANDLIC",
    "PE\ufffdASQUIT": "PEÑASQUITOS",   # Autocompletado
    "EURODISE\ufffd": "EURODISEÑO",    # Autocompletado
    "AGUL\ufffdIAGA": "AGULIÑAGA",
    "SILVI\ufffdN": "SILVIAN",         # Silvián
    "AGGAMCA\ufffd": "AGGAMCAÑO",
    "MENDIZ\ufffdBA": "MENDIZABAL",    # Autocompletado (Mendizábal)
    "ORDU\ufffdOS": "ORDUÑOS",
    "BJ\ufffdRN": "BJORN",             # Diéresis (Björn)
    "PEDRICE\ufffdA": "PEDRICEÑA",
    "SURL\ufffdACH": "SURLIÑACH",
    "CALI\ufffdAS": "CALIÑAS",
    "G\ufffdLTIME": "GULTIME",         # Diéresis (Güiltime)
    "TOLE\ufffdO": "TOLEÑO",
    "Y\ufffdAKI": "YÑAKI",             # Yñaki
    "DISE\ufffdADUR": "DISEÑADURIA",   # Autocompletado
    "DA\ufffdESTA": "DAÑESTA",
    "CHAVL\ufffdA": "CHAVLIÑA",
    "ERG\ufffdIN": "ERGUIN",           # Diéresis (Ergüin)
    "BU\ufffdI": "BUÑI",
    "CAASTA\ufffdED": "CAASTAÑEDA",    # Typo y Autocompletado
    "CONSULTOR\ufffd": "CONSULTORIA",  # Autocompletado
    "NU\ufffdU": "NUÑU",
    "CARRL\ufffdO": "CARRLIÑO",
    "PI\ufffdADOSA": "PIÑADOSA",
    "MIL\ufffdN": "MILAN",             # Milán
    "PE\ufffdURI": "PEÑURI",
    "BIBA\ufffdEZ": "BIBAÑEZ",
    "CAAMA\ufffdA": "CAAMAÑA",
    "VIXHL\ufffdAC": "VIXHLIÑAC",
    "TEMIZQUE\ufffd": "TEMIZQUEÑO",    # Autocompletado
    "SALADA\ufffdA": "SALADAÑA",
    "O\ufffdATIVIA": "OÑATIVIA",
    "W\ufffdRSTE": "WURSTE",           # Diéresis (Würste)
    "SU\ufffdSTEGUI": "SUASTEGUI",     # Suástegui
    "CABRE\ufffdO": "CABREÑO",
    "AY\ufffdN": "AYON",               # Ayón
    "CARRI\ufffdN": "CARRION",         # Carrión
    "PA\ufffdAL": "PAÑAL",
    "PIRA\ufffdAS": "PIRAÑAS",
    "CASTA\ufffdDA": "CASTAÑEDA",      # Typo de usuario (Castañda)
    "A\ufffdORBEZ": "AÑORBEZ",
    "B\ufffdCHNER": "BUCHNER",         # Diéresis (Büchner)
    "D\ufffdUNERT": "DUNERT",          # Diéresis (Dünert)
    "A\ufffdELY": "AÑELY",
    "GUAJAQUE\ufffd": "GUAJAQUEÑO",    # Autocompletado
    "LEBE\ufffdA": "LEBEÑA",
    "A\ufffdADIENDC": "AÑADIENDO",     # Typo de usuario corregido
    "ECHEVARR\ufffd": "ECHEVARRIA",    # Autocompletado
    "INDUSTR\ufffdA": "INDUSTRIA",     # Industria
    "GALL\ufffdO": "GALLIÑO",
    "AVUNDA\ufffdO": "AVUNDAÑO",
    "CASTA\ufffdADA": "CASTAÑADA",
    "BA\ufffdALITEC": "BAÑALITEC",
    "ALVAR\ufffdO": "ALVARIÑO",
    "VIDA\ufffdES": "VIDAÑES",
    "VRICE\ufffdO": "VRICEÑO",
    "ZIA\ufffdEZ": "ZIAÑEZ",
    "QUI\ufffdIONEZ": "QUIÑONEZ",      # Typo de usuario (Quiñionez)
    "ZA\ufffdEZ": "ZAÑEZ",
    "MORE\ufffdA": "MOREÑA",
    "SA\ufffdDE": "SAÑDE",
    "CASTE\ufffdADA": "CASTEÑADA",     # Typo de usuario
    "VICTOR\ufffdA": "VICTORIA",       # Victoria
    "VEDA\ufffdA": "VEDAÑA",
    "VILLECA\ufffdA": "VILLECAÑA",
    "ACALQUE\ufffd": "ACALQUEÑO",      # Autocompletado
    "LIZE\ufffdA": "LIZEÑA",
    "PE\ufffdAPOBRE": "PEÑAPOBRE",
    "MONTERA\ufffdA": "MONTERAÑA",
    "BIODISE\ufffdO": "BIODISEÑO",
    "CREDISE\ufffdO": "CREDISEÑO",
    "CA\ufffdEDOS": "CAÑEDOS",
    "ARMU\ufffdA": "ARMUÑA",
    "GR\ufffdNBERG": "GRUNBERG",       # Diéresis (Grünberg)
    "ENTREVI\ufffdED": "ENTREVIÑEDOS", # Autocompletado
    "ESACRE\ufffdO": "ESACREÑO",
    "UR\ufffdAS": "URIAS",             # Urías
    "AVENDA\ufffdOS": "AVENDAÑOS",
    "COROME\ufffdO": "COROMEÑO",
    "CARE\ufffdO": "CAREÑO",
    "CARL\ufffdN": "CARLON",           # Carlón
    "GARA\ufffdON": "GARAÑON",
    "CASATA\ufffdED": "CASTAÑEDA",     # Typo de usuario y Autocompletado
    "SUE\ufffdAS": "SUEÑAS",
    "GAZTA\ufffdAGA": "GAZTAÑAGA",
    "CABORQUE\ufffd": "CABORQUEÑO",    # Autocompletado
    "ECOLOG\ufffdA": "ECOLOGIA",       # Ecología
    "RA\ufffdAL": "RAÑAL",
    # Lote 25: Typos de usuario (INSPECCIÓM), Corporativos, Diéresis Alemanas y Autocompletados
    "SANTOBE\ufffdA": "SANTOBEÑA",
    "MUR\ufffdT": "MURAT",             # Murat
    "INSPECCI\ufffdM": "INSPECCION",   # Typo de origen (Inspeccióm)
    "YOMONTA\ufffd": "YOMONTAÑO",      # Autocompletado deductivo
    "NERBL\ufffdO": "NERBLIÑO",
    "MARL\ufffdAS": "MARLIÑAS",
    "GALDU\ufffdO": "GALDUÑO",
    "CEPE\ufffdA": "CEPEÑA",
    "BLA\ufffdEDEZ": "BLAÑEDEZ",
    "GUAG\ufffdI": "GUAGUI",           # Diéresis (Güagüi)
    "CHAPE\ufffdO": "CHAPEÑO",
    "\ufffdENTREGA": "ENTREGA",        # Limpieza de basura inicial
    "SESL\ufffdN": "SESLION",          # Seslión
    "CASA\ufffdEZ": "CASAÑEZ",
    "VIGA\ufffdAS": "VIGAÑAS",
    "HIP\ufffdLVEDES": "HIPOLVEDES",   # (Hipólvedes)
    "TOTO\ufffdHO": "TOTOÑHO",
    "ARG\ufffdETA": "ARGUETA",         # Diéresis (Argüeta)
    "BEGO\ufffdIA": "BEGOÑIA",
    "ANTO\ufffdA": "ANTOÑA",
    "VIPL\ufffdA": "VIPLIÑA",
    "REPARITE\ufffdO": "REPARITEÑO",
    "GL\ufffdKY": "GLUKY",             # Diéresis (Glüky)
    "PA\ufffdART": "PAÑART",
    "G\ufffdISA": "GUISA",             # Diéresis (Güisa)
    "GORGO\ufffdO": "GORGOÑO",
    "PING\ufffdINOS": "PINGUINOS",     # Diéresis (Pingüinos)
    "VOLA\ufffdO": "VOLAÑO",
    "YPATL\ufffdO": "YPATLIÑO",
    "VL\ufffdAZ": "VLIÑAZ",
    "BRU\ufffdA": "BRUÑA",
    "PE\ufffdAGIO": "PEÑAGIO",
    "\ufffdORI": "ORI",                # Limpieza de basura inicial
    "K\ufffdRBER": "KORBER",           # Diéresis (Körber)
    "PATL\ufffdN": "PATLION",          # Patlión
    "CAML\ufffdO": "CAMLIÑO",
    "O\ufffdATAE": "OÑATAE",
    "P\ufffdBLOCO": "PUBLICO",         # Typo de origen (Públoco)
    "EFIGUE\ufffdA": "EFIGUEÑA",
    "ESPEC\ufffdFICO": "ESPECIFICO",   # Específico
    "CONSTITUCI\ufffd": "CONSTITUCION", # Autocompletado
    "H\ufffdBIL": "HABIL",             # Hábil
    "A\ufffdES": "AÑES",
    "JUL\ufffdAN": "JULIAN",           # Julián
    "MIR\ufffdN": "MIRON",             # Mirón
    "NL\ufffdOZ": "NLIÑOZ",
    "U\ufffdATES": "UÑATES",
    "LUA\ufffdA": "LUAÑA",
    "GALL\ufffdANEZ": "GALLIÑANEZ",
    "J\ufffdCRUZ": "JCRUZ",            # J. Cruz (Jí Cruz)
    "LACTOLE\ufffdE": "LACTOLEÑE",
    "VL\ufffdOLES": "VLIÑOLES",
    "CA\ufffdIZAL": "CAÑIZAL",
    "KACHL\ufffdA": "KACHLIÑA",
    "GEN\ufffdMICA": "GENOMICA",       # Genómica
    "M\ufffdDICOS": "MEDICOS",         # Médicos
    "GORDO\ufffdO": "GORDOÑO",
    "A\ufffdREOS": "AEREOS",           # Aéreos (Aëreos)
    "ENSE\ufffdAME": "ENSEÑAME",       # Enséñame
    "ORTA\ufffdEZ": "ORTAÑEZ",
    "ALVEDA\ufffdO": "ALVEDAÑO",
    "NEGR\ufffdN": "NEGRON",           # Negrón
    "ORGANDO\ufffd": "ORGANDOÑO",      # Autocompletado
    "JOYE\ufffdO": "JOYEÑO",
    "K\ufffdHNERT": "KUHNERT",         # Diéresis (Kühnert)
    "G\ufffdEREJO": "GUEREJO",         # Diéresis (Güerejo)
    "A\ufffdORGA": "AÑORGA",
    "\ufffdO": "O",                    # Basura suelta
    "PE\ufffdAFIL": "PEÑAFIL",
    "ZALD\ufffdVAR": "ZALDIVAR",       # Zaldívar
    "P\ufffdIBLICO": "PUBLICO",        # Typo de origen (Püiblico)
    "COTE\ufffdO": "COTEÑO",
    "COMPUDISE\ufffd": "COMPUDISEÑO",  # Autocompletado
    "MARSELE\ufffdO": "MARSELEÑO",
    "CHINE\ufffdA": "CHINEÑA",
    "HOGARE\ufffdO": "HOGAREÑO",
    "SERE\ufffdI": "SEREÑI",
    "MAG\ufffdI": "MAGUI",             # Diéresis (Magüi)
    "QUINO\ufffdEZ": "QUIÑONEZ",       # Typo de usuario corregido
    "MARITO\ufffdE": "MARITOÑE",
    "F\ufffdRDERTEC": "FORDERTEC",     # Diéresis (Fördertec)
    "WOLOJVIA\ufffd": "WOLOJVIAÑO",    # Autocompletado
    "CRECE\ufffdO": "CRECEÑO",
    "F\ufffdGEMANN": "FUGEMANN",       # Diéresis (Fügemann)
    "F\ufffdRREA": "FERREA",           # Férrea
    "VIDRIALE\ufffdO": "VIDRIALEÑO",
    "LEA\ufffdES": "LEAÑES",
    "ZU\ufffdOGA": "ZUÑOGA",
    "PE\ufffdAR": "PEÑAR",
    "TOURL\ufffdO": "TOURLIÑO",
    "MEDA\ufffdO": "MEDAÑO",
    "ANTO\ufffdIA": "ANTOÑIA",
    "MU\ufffdEZ": "MUÑEZ",
    "PE\ufffdE": "PEÑE",
    "MADUE\ufffdOS": "MADUEÑOS",
    "SE\ufffdALOAX": "SEÑALOAX",
    "SANTIBA\ufffdEA": "SANTIBAÑEA",
    "CHINE\ufffdO": "CHINEÑO",
    "LIA\ufffdEZ": "LIAÑEZ",
    "ALL\ufffdAN": "ALLIAN",           # Allián
    "RAZ\ufffdN": "RAZON",             # Razón
    "BERSA\ufffdEZ": "BERSAÑEZ",
    "ADECUACI\ufffd": "ADECUACION",    # Autocompletado
    "TOM\ufffdS": "TOMAS",            # Tomás
    "LABA\ufffdINO": "LABAÑINO",
    "MANR\ufffdQUE": "MANRIQUE",      # Manríquez / Manrique
    "Z\ufffdRATE": "ZARATE",          # Zárate
    "VILARI\ufffdO": "VILARIÑO",
    "MEO\ufffdOS": "MEOÑOS",
    "MOGO\ufffdE": "MOGOÑE",
    "M\ufffdX": "MEX",                 # Abreviatura de MÉX.
    "BALDEPE\ufffdA": "BALDEPEÑA",
    "MEAVEPE\ufffdA": "MEAVEPEÑA",
    "EDL\ufffdO": "EDLIÑO",
    "MING\ufffdER": "MINGUER",        # Diéresis (Mingüer)
    "BRASILE\ufffdOS": "BRASILEÑOS",
    "PE\ufffdAFOR": "PEÑAFOR",
    "BRISE\ufffdA": "BRISEÑA",
    "REALE\ufffdO": "REALEÑO",
    "CONSTRUDISE\ufffd": "CONSTRUDISEÑO", # Autocompletado deductivo
    "CALPE\ufffdO": "CALPEÑO",
    "PI\ufffdUELOS": "PIÑUELOS",
    "HITANDEG\ufffd": "HITANDEGUI",   # Diéresis autocompletada
    "L\ufffdNEA": "LINEA",            # Línea
    "NURE\ufffdA": "NUREÑA",
    "TE\ufffdIDOS": "TEÑIDOS",
    "ZIZL\ufffdHO": "ZIZLIHO",
    "CA\ufffdONES": "CAÑONES",
    "BA\ufffdEZ": "BAÑEZ",
    "S\ufffdD": "SUD",                # Diéresis alemana (Süd)
    "REMISI\ufffdN": "REMISION",
    "AVELDA\ufffdEZ": "AVELDAÑEZ",
    "PE\ufffdASCAL": "PEÑASCAL",
    "PI\ufffdARRIETA": "PIÑARRIETA",
    "LLA\ufffdEZ": "LLAÑEZ",
    "MEL\ufffdNDEZ": "MELENDEZ",      # Meléndez
    "GAYT\ufffdN": "GAYTAN",          # Gaytán
    "ORU\ufffdA": "ORUÑA",
    "COMPA\ufffdER": "COMPAÑERO",     # Autocompletado
    "T\ufffdCNICO": "TECNICO",        # Técnico
    "B\ufffdRCENAS": "BARCENAS",      # Bárcenas
    "ENR\ufffdQUEZ": "ENRIQUEZ",      # Enríquez
    "BAZA\ufffdEZ": "BAZAÑEZ",
    "SICE\ufffdA": "SICEÑA",
    "PI\ufffdEIRUA": "PIÑEIRUA",
    "IMPLEMENTACI\ufffd": "IMPLEMENTACION", # Autocompletado
    "PACHUQUE\ufffd": "PACHUQUEÑO",   # Autocompletado
    "SO\ufffdANEZ": "SOÑANEZ",
    "MARTE\ufffdO": "MARTEÑO",
    "BA\ufffdAREZ": "BAÑAREZ",
    "I\ufffdESTA": "IÑESTA",          # Iñesta
    "MU\ufffdECAS": "MUÑECAS",
    "LIM\ufffdN": "LIMON",            # Limón
    "DIEGUE\ufffdO": "DIEGUEÑO",
    "CER\ufffdN": "CERON",            # Cerón
    "CA\ufffdI": "CAÑI",
    "AGUST\ufffdN": "AGUSTIN",        # Agustín
    "D\ufffdVILA": "DAVILA",          # Dávila
    "CA\ufffdEDA": "CAÑEDA",
    "COSTE\ufffdIZAT": "COSTEÑIZACION", # Autocompletado deductivo
    "L\ufffdTTIG": "LUTTIG",          # Diéresis (Lüttig)
    "ZARCE\ufffdO": "ZARCEÑO",
    "DA\ufffdIEL": "DANIEL",          # Dañiel/Daniel roto
    "SANTIBA\ufffdEZ": "SANTIBAÑEZ",
    "CEDE\ufffdO": "CEDEÑO",
    "URE\ufffdA": "UREÑA",
    "MUCI\ufffdO": "MUCIÑO",
    "AGUI\ufffdAGA": "AGUIÑAGA",
    "CA\ufffdADA": "CAÑADA",
    "GAMI\ufffdO": "GAMIÑO",
    "VILLAFA\ufffdA": "VILLAFAÑA",
    "CESE\ufffdA": "CESEÑA",
    "ESCARE\ufffdO": "ESCAREÑO",
    "CA\ufffdEDO": "CAÑEDO",
    "DISE\ufffdOS": "DISEÑOS",
    "PE\ufffdOLES": "PEÑOLES",
    "PIZA\ufffdA": "PIZAÑA",
    "PE\ufffdAFIEL": "PEÑAFIEL",
    "TISCARE\ufffdO": "TISCAREÑO",
    "CARDE\ufffdA": "CARDEÑA",
    "VILLICA\ufffdA": "VILLICAÑA",
    "BURGUE\ufffdO": "BURGUEÑO",
    "CA\ufffdAS": "CAÑAS",
    "CECE\ufffdA": "CECEÑA",
    "MONTA\ufffdA": "MONTAÑA",
    "CHI\ufffdAS": "CHIÑAS",
    "PE\ufffdASCO": "PEÑASCO",
    "OMA\ufffdA": "OMAÑA",
    "VIDA\ufffdA": "VIDAÑA",
    "LI\ufffdAN": "LIÑAN",
    "A\ufffdORVE": "AÑORVE",
    "SA\ufffdUDO": "SAÑUDO",
    "TRASVI\ufffdA": "TRASVIÑA",
    "CASTA\ufffdOS": "CASTAÑOS",
    "DUE\ufffdEZ": "DUEÑEZ",
    "MASCARE\ufffdO": "MASCAREÑO",  # Asumiendo terminación O por la imagen cortada
    "MASCARE\ufffdAS": "MASCAREÑAS", # Asumiendo terminación AS por precaución
    "PEQUE\ufffdO": "PEQUEÑO",
    "NI\ufffdOS": "NIÑOS",
    "CARCA\ufffdO": "CARCAÑO",
    "RICA\ufffdO": "RICAÑO",
    "VI\ufffdEDOS": "VIÑEDOS",
    "PE\ufffdU": "PEÑU",            # Raíz parcial capturada
    "\ufffdURI": "ÑURI",            # Raíz parcial capturada
    "CATA\ufffdO": "CATAÑO",
    "SEDE\ufffdO": "SEDEÑO",
    "SARI\ufffdANA": "SARIÑANA",
    "MARA\ufffdON": "MARAÑON",
    "CASTA\ufffdO": "CASTAÑO",
    "BA\ufffdALES": "BAÑALES",
    "CURE\ufffdO": "CUREÑO",
    "LARRA\ufffdAGA": "LARRAÑAGA",
    "O\ufffdATE": "OÑATE",
    "VALDEPE\ufffdA": "VALDEPEÑA",
    "PE\ufffdAFLOR": "PEÑAFLOR",
    "COSTE\ufffdA": "COSTEÑA",
    "RIA\ufffdO": "RIAÑO",
    "CA\ufffdEZ": "CAÑEZ",
    "LEA\ufffdOS": "LEAÑOS",
    "CA\ufffdA": "CAÑA",
    "MA\ufffdON": "MAÑON",
    "VICU\ufffdA": "VICUÑA",
    "NA\ufffdEZ": "NAÑEZ",
    "PI\ufffdEIRO": "PIÑEIRO",
    "GENERACI\ufffdN": "GENERACION", # Asumiendo terminación N por la imagen cortada
    "SE\ufffdORA": "SEÑORA",
    "IPI\ufffdA": "IPIÑA",
    "OCA\ufffdAS": "OCAÑAS",
    "PI\ufffdUELAS": "PIÑUELAS",
    "VI\ufffdAS": "VIÑAS",
    "ESTUPI\ufffdAN": "ESTUPIÑAN",
    # Lote 2: Nombres, apellidos y palabras comunes (Ñ y vocales acentuadas)
    "SE\ufffdOR": "SEÑOR",
    "CAMPA\ufffdA": "CAMPAÑA",
    "GARC\ufffdA": "GARCIA",
    "CAAMA\ufffdO": "CAAMAÑO",
    "PE\ufffdATE": "PEÑATE",
    "MADUE\ufffdO": "MADUEÑO",
    "MARTI\ufffdON": "MARTIÑON",
    "TUFI\ufffdO": "TUFIÑO",
    "L\ufffdPEZ": "LOPEZ",
    "LE\ufffdERO": "LEÑERO",
    "ALBA\ufffdIL": "ALBAÑIL",
    "GAVI\ufffdO": "GAVIÑO",
    "PESTA\ufffdA": "PESTAÑA",
    "PI\ufffdERA": "PIÑERA",
    "BRE\ufffdA": "BREÑA",
    "GARCIDUE\ufffdAS": "GARCIDUEÑAS", # Terminación autocompletada
    "SAVI\ufffdON": "SAVIÑON",
    "GONZ\ufffdLEZ": "GONZALEZ",
    "RETO\ufffdO": "RETOÑO",
    "SEA\ufffdEZ": "SEAÑEZ",
    "LUQUE\ufffdO": "LUQUEÑO",
    "MU\ufffdOS": "MUÑOS",
    "DO\ufffdA": "DOÑA",
    "MARI\ufffdO": "MARIÑO",
    "P\ufffdREZ": "PEREZ",
    "JES\ufffdS": "JESUS",
    "RODR\ufffdGUEZ": "RODRIGUEZ", # Terminación autocompletada
    "S\ufffdNCHEZ": "SANCHEZ",
    "GAVI\ufffdA": "GAVIÑA",
    "I\ufffdIGO": "IÑIGO",
    "GL\ufffdCK": "GLUCK",
    "SOLUCI\ufffdN": "SOLUCION",
    "RIBERE\ufffdA": "RIBEREÑA",
    "CAMA\ufffdO": "CAMAÑO",
    "MARI\ufffdELARENA": "MARIÑELARENA", # Terminación autocompletada
    "DUE\ufffdES": "DUEÑES",
    "BARE\ufffdO": "BAREÑO",
    "ESTA\ufffdOL": "ESTAÑOL",
    "CHORE\ufffdO": "CHOREÑO",
    "AG\ufffdERO": "AGUERO",
    "ALBA\ufffdEZ": "ALBAÑEZ",
    "ARG\ufffdELLES": "ARGUELLES",
    "SESE\ufffdA": "SESEÑA",
    "PEQUE\ufffdA": "PEQUEÑA",
    "ZARI\ufffdANA": "ZARIÑANA",
    "BEGO\ufffdA": "BEGOÑA",
    "COSTE\ufffdO": "COSTEÑO",
    "CERME\ufffdO": "CERMEÑO",
    "CA\ufffdAMAR": "CAÑAMAR",
    "VICENTE\ufffdO": "VICENTEÑO",
    "MAR\ufffdA": "MARIA",
    "MASCARE\ufffdA": "MASCAREÑA",
    "VILLAFA\ufffdE": "VILLAFAÑE",
    "RAM\ufffdREZ": "RAMIREZ",
    "GUERE\ufffdA": "GUEREÑA",
    "CA\ufffdAVERAL": "CAÑAVERAL",
    "CERRITE\ufffdO": "CERRITEÑO",
    "CABA\ufffdA": "CABAÑA",
    "MI\ufffdON": "MIÑON",
    "VI\ufffdA": "VIÑA",
    "MAGARI\ufffdO": "MAGARIÑO",
    "PE\ufffdON": "PEÑON",
    "ESPA\ufffdOLA": "ESPAÑOLA",
    "ANTA\ufffdO": "ANTAÑO",
    "EMISI\ufffdN": "EMISION",
    "PI\ufffdONES": "PIÑONES",
    "EMPE\ufffdOS": "EMPEÑOS",
    "OLO\ufffdO": "OLOÑO",
    "URE\ufffdO": "UREÑO",
    "ESPA\ufffdOL": "ESPAÑOL",
    "MARDUE\ufffdO": "MARDUEÑO",
    "BASA\ufffdEZ": "BASAÑEZ",
    "BAI\ufffdAGA": "BAIÑAGA", 
    "MU\ufffdOA": "MUÑOA",
    "OCA\ufffdO": "OCAÑO",
    "G\ufffdMEZ": "GOMEZ",
    "BA\ufffdO": "BAÑO",
    "AGUI\ufffdA": "AGUIÑA",
    "CA\ufffdETE": "CAÑETE",
    "CASTA\ufffdARES": "CASTAÑARES", # Terminación autocompletada
    "ANTU\ufffdANO": "ANTUÑANO",
    "TUXPE\ufffdO": "TUXPEÑO",
    "PROA\ufffdO": "PROAÑO",
    "OAXAQUE\ufffdO": "OAXAQUEÑO", # Terminación autocompletada
    "SUE\ufffdOS": "SUEÑOS",
    "ZA\ufffdUDO": "ZAÑUDO",
    "ZARI\ufffdAN": "ZARIÑAN",
    "CASA\ufffdAS": "CASAÑAS",
    "CA\ufffdEROS": "CAÑEROS",
    "CA\ufffdERA": "CAÑERA",
    "D\ufffdA": "DIA",
    "ARRA\ufffdAGA": "ARRAÑAGA",
    "PI\ufffdEYRO": "PIÑEYRO",
    "CIGUE\ufffdALES": "CIGUEÑALES",
    "BA\ufffdUELAS": "BAÑUELAS",
    "BALI\ufffdO": "BALIÑO",
    "MADRUE\ufffdO": "MADRUEÑO",
    "CECE\ufffdAS": "CECEÑAS",
    "CUTI\ufffdO": "CUTIÑO",
    "N\ufffdMERO": "NUMERO",
    "MU\ufffdOZ": "MUÑOZ",
    "PE\ufffdA": "PEÑA",
    "MAGA\ufffdA": "MAGAÑA",
    "SALDA\ufffdA": "SALDAÑA",
    "CASTA\ufffdEDA": "CASTAÑEDA",
    "MONTA\ufffdO": "MONTAÑO",
    "IBA\ufffdEZ": "IBAÑEZ",
    "GARDU\ufffdO": "GARDUÑO",
    "HERN\ufffdNDEZ": "HERNANDEZ",
    "MART\ufffdNEZ": "MARTINEZ",
    "ORDO\ufffdEZ": "ORDOÑEZ",
    "CARRE\ufffdO": "CARREÑO",
    "OCA\ufffdA": "OCAÑA",
    "MARCELE\ufffdO": "MARCELEÑO",
    "CASTA\ufffdON": "CASTAÑON",
    "PATI\ufffdO": "PATIÑO",
    "AVENDA\ufffdO": "AVENDAÑO",
    "PE\ufffdALOZA": "PEÑALOZA",
    "AGUI\ufffdIGA": "AGUIÑIGA",
    "CARI\ufffdO": "CARIÑO",
    "NU\ufffdEZ": "NUÑEZ",
    "ORTU\ufffdO": "ORTUÑO",
    "YA\ufffdEZ": "YAÑEZ",
    "PE\ufffdUELAS": "PEÑUELAS",
    "ANG\ufffdLICA": "ANGELICA",
    "JAZM\ufffdN": "JAZMIN",
    "OTA\ufffdEZ": "OTAÑEZ",
    "\ufffdPUBLICO": "PUBLICO",
    "ORDU\ufffdO": "ORDUÑO",
    "GARDU\ufffdO": "GARDUÑO", # Repetido de arriba, pero en formato seguro
    "QUI\ufffdONEZ": "QUIÑONEZ",
    "BRICE\ufffdO": "BRICEÑO",
    "\ufffdLVAREZ": "ALVAREZ",

    # 1.2 Correcciones con el caracter Ð (D con guion)
    "CHILHUAQUEÐO": "CHILHUAQUEÑO",
    "MARIÐELARENA": "MARIÑELARENA",
    "GARCIDUEÐAS": "GARCIDUEÑAS",
    "CARCIDUEÐAS": "CARCIDUEÑAS",
    "VILLASEÐOR": "VILLASEÑOR",
    "SANTIBAÐEZ": "SANTIBAÑEZ",
    "SANTIVAÐEZ": "SANTIVAÑEZ",
    "PEÐABRONCE": "PEÑABRONCE",
    "MASCAREÐAS": "MASCAREÑAS",
    "QUECHULEÐO": "QUECHULEÑO",
    "PEÐARRIETA": "PEÑARRIETA",
    "PACHUQUEÐO": "PACHUQUEÑO",
    "VILLAFAÐEZ": "VILLAFAÑEZ",
    "CASTAÐUELA": "CASTAÑUELA",
    "ATLIXQUEÐO": "ATLIXQUEÑO",
    "CASTELLAÐO": "CASTELLANO",
    "TRASLAVIÐA": "TRASLAVIÑA",
    "VILLACEÐOR": "VILLACEÑOR",
    "CASTAÐARES": "CASTAÑARES",
    "PEÐAFLORES": "PEÑAFLORES",
    "SANTIBAÐEA": "SANTIBAÑEA",
    "VALLASEÐOR": "VALLASEÑOR",
    "BILLAFAÐEZ": "BILLAFAÑEZ",
    "CASTAÐEDA": "CASTAÑEDA",
    "VILLAFAÐA": "VILLAFAÑA",
    "TISCAREÐO": "TISCAREÑO",
    "VILLAFAÐE": "VILLAFAÑE",
    "VALDEPEÐA": "VALDEPEÑA",
    "VILLICAÐA": "VILLICAÑA",
    "VICENTEÐO": "VICENTEÑO",
    "MASCAREÐO": "MASCAREÑO",
    "CAÐAVERAL": "CAÑAVERAL",
    "MARCELEÐO": "MARCELEÑO",
    "CHARQUEÐO": "CHARQUEÑO",
    "VENTUREÐO": "VENTUREÑO",
    "SERRITEÐO": "SERRITEÑO",
    "ESTUPIÐAN": "ESTUPIÑAN",
    "SANTOVEÐA": "SANTOVEÑA",
    "VILLACAÐA": "VILLACAÑA",
    "CASTEÐEDA": "CASTEÑEDA",
    "MUÐOZCANO": "MUÑOZCANO",
    "LARRAÐAGA": "LARRAÑAGA",
    "MARFILEÐO": "MARFILEÑO",
    "CERRITEÐO": "CERRITEÑO",
    "HERMITAÐO": "HERMITAÑO",
    "CASTAÐADA": "CASTAÑADA",
    "ENRIQUEÐO": "ENRIQUEÑO",
    "CAÐEVERAL": "CAÑEVERAL",
    "MALDEPEÐA": "MALDEPEÑA",
    "CAZTAÐEDA": "CAZTAÑEDA",
    "FISCALEÐO": "FISCALEÑO",
    "FILLAFAÐA": "FILLAFAÑA",
    "QUIIÐONEZ": "QUIIÑONEZ",
    "CHAÐICUEN": "CHAÑICUEN",
    "ALBELDAÐO": "ALBELDAÑO",
    "VALLAFAÐA": "VALLAFAÑA",
    "CADEÐANES": "CADEÑANES",
    "PEREZPEÐA": "PEREZPEÑA",
    "VIÐANUEVA": "VIÑANUEVA",
    "JOSIEDIÐO": "JOSIEDIÑO",
    "MUÐOZCANA": "MUÑOZCANA",
    "PEÐARANDA": "PEÑARANDA",
    "AVENDAÐO": "AVENDAÑO",
    "BAÐUELOS": "BAÑUELOS",
    "PEÐALOZA": "PEÑALOZA",
    "QUIÐONES": "QUIÑONES",
    "QUIÐONEZ": "QUIÑONEZ",
    "CASTAÐON": "CASTAÑON",
    "MONTAÐEZ": "MONTAÑEZ",
    "AGUIÐAGA": "AGUIÑAGA",
    "AGUIÐIGA": "AGUIÑIGA",
    "ESCAREÐO": "ESCAREÑO",
    "PEÐUELAS": "PEÑUELAS",
    "PEÐAFIEL": "PEÑAFIEL",
    "SARIÐANA": "SARIÑANA",
    "PERIAÐEZ": "PERIAÑEZ",
    "PEÐAFLOR": "PEÑAFLOR",
    "TRASVIÐA": "TRASVIÑA",
    "BURGUEÐO": "BURGUEÑO",
    "PEÐUÐURI": "PEÑUÑURI",
    "SACHIÐAS": "SACHIÑAS",
    "PIÐUELAS": "PIÑUELAS",
    "MARTIÐON": "MARTIÑON",
    "ABENDAÐO": "ABENDAÑO",
    "CASTAÐOS": "CASTAÑOS",
    "PEÐAFORT": "PEÑAFORT",
    "MAGARIÐO": "MAGARIÑO",
    "ESTUPIÐA": "ESTUPIÑA",
    "SARDIÐAS": "SARDIÑAS",
    "CAÐADERO": "CAÑADERO",
    "MARQUEÐO": "MARQUEÑO",
    "PEÐALOSA": "PEÑALOSA",
    "VERSAÐEZ": "VERSAÑEZ",
    "MARDUEÐO": "MARDUEÑO",
    "AVERTAÐO": "AVERTAÑO",
    "LEGIDEÐO": "LEGIDEÑO",
    "PEÐALBER": "PEÑALBER",
    "BARAGAÐO": "BARAGAÑO",
    "MADRUEÐO": "MADRUEÑO",
    "CAPULEÐO": "CAPULEÑO",
    "MONTAÐES": "MONTAÑES",
    "AVELDAÐO": "AVELDAÑO",
    "CHALPEÐO": "CHALPEÑO",
    "CATAÐEDA": "CATAÑEDA",
    "MARITOÐA": "MARITOÑA",
    "QUIÐOÐEZ": "QUIÑOÑEZ",
    "GONZAÐEZ": "GONZAÑEZ",
    "QUIÐOÐES": "QUIÑOÑES",
    "PERYAÐEZ": "PERYAÑEZ",
    "ANTUÐANO": "ANTUÑANO",
    "ORODOÐEZ": "ORODOÑEZ",
    "JARALEÐO": "JARALEÑO",
    "AMENDAÐO": "AMENDAÑO",
    "UBALDAÐO": "UBALDAÑO",
    "BARRAÐON": "BARRAÑON",
    "SELEDOÐA": "SELEDOÑA",
    "ORDEÐANA": "ORDEÑANA",
    "BOLOAÐOS": "BOLOAÑOS",
    "ESACREÐO": "ESACREÑO",
    "GRANDEÐO": "GRANDEÑO",
    "ARRIBEÐO": "ARRIBEÑO",
    "BALGAÐON": "BALGAÑON",
    "ZARIÐANA": "ZARIÑANA",
    "PEREAÐEZ": "PEREAÑEZ",
    "VILAFAÐA": "VILAFAÑA",
    "TACUBEÐO": "TACUBEÑO",
    "ORDDOÐEZ": "ORDDOÑEZ",
    "EVENDAÐO": "EVENDAÑO",
    "BARQUEÐA": "BARQUEÑA",
    "URUÐUELA": "URUÑUELA",
    "PAÐALOZA": "PAÑALOZA",
    "GARDUÐO": "GARDUÑO",
    "SALDAÐA": "SALDAÑA",
    "ORDOÐEZ": "ORDOÑEZ",
    "MONTAÐO": "MONTAÑO",
    "BOLAÐOS": "BOLAÑOS",
    "CARREÐO": "CARREÑO",
    "CABAÐAS": "CABAÑAS",
    "BRISEÐO": "BRISEÑO",
    "COUTIÐO": "COUTIÑO",
    "TREVIÐO": "TREVIÑO",
    "BRICEÐO": "BRICEÑO",
    "IÐIGUEZ": "IÑIGUEZ",
    "CARCAÐO": "CARCAÑO",
    "ZERMEÐO": "ZERMEÑO",
    "CARDEÐA": "CARDEÑA",
    "CASTAÐO": "CASTAÑO",
    "MARAÐON": "MARAÑON",
    "COSTEÐO": "COSTEÑO",
    "PESTAÐA": "PESTAÑA",
    "BAÐALES": "BAÑALES",
    "CASAÐAS": "CASAÑAS",
    "RUBIÐOS": "RUBIÑOS",
    "SAVIÐON": "SAVIÑON",
    "LUQUEÐO": "LUQUEÑO",
    "ORDOÐES": "ORDOÑES",
    "PIÐEIRO": "PIÑEIRO",
    "RANCAÐO": "RANCAÑO",
    "CAAMAÐO": "CAAMAÑO",
    "PEÐUELA": "PEÑUELA",
    "CAMPAÐA": "CAMPAÑA",
    "ZARIÐAN": "ZARIÑAN",
    "PEÐALTA": "PEÑALTA",
    "MOCIÐOS": "MOCIÑOS",
    "VENTEÐO": "VENTEÑO",
    "FELEÐOS": "FELEÑOS",
    "MARTEÐO": "MARTEÑO",
    "ESTAÐOL": "ESTAÑOL",
    "ALBAÐIL": "ALBAÑIL",
    "MONDOÐO": "MONDOÑO",
    "CRUCEÐO": "CRUCEÑO",
    "ORDUÐEZ": "ORDUÑEZ",
    "AVEDAÐO": "AVEDAÑO",
    "PEÐARAN": "PEÑARAN",
    "ESPAÐOL": "ESPAÑOL",
    "PEÐAIRA": "PEÑAIRA",
    "CAZAÐAS": "CAZAÑAS",
    "RIQUEÐO": "RIQUEÑO",
    "CHOREÐO": "CHOREÑO",
    "CALDIÐO": "CALDIÑO",
    "FANDIÐO": "FANDIÑO",
    "BIÐUELO": "BIÑUELO",
    "BALLEÐO": "BALLEÑO",
    "MUÐETON": "MUÑETON",
    "CECEÐAS": "CECEÑAS",
    "MAURIÐO": "MAURIÑO",
    "ESTAÐON": "ESTAÑON",
    "CARMIÐA": "CARMIÑA",
    "PEÐAFOR": "PEÑAFOR",
    "PEÐALES": "PEÑALES",
    "CARDEÐO": "CARDEÑO",
    "TUXPEÐO": "TUXPEÑO",
    "PEQUEÐO": "PEQUEÑO",
    "CARMEÐO": "CARMEÑO",
    "PARDIÐO": "PARDIÑO",
    "CAÐONGO": "CAÑONGO",
    "PALMEÐO": "PALMEÑO",
    "CARPIÐA": "CARPIÑA",
    "SOÐANES": "SOÑANES",
    "PEQUEÐA": "PEQUEÑA",
    "MADUEÐA": "MADUEÑA",
    "CASTOÐO": "CASTOÑO",
    "SACHIÐA": "SACHIÑA",
    "PIÐONES": "PIÑONES",
    "MADUEÐO": "MADUEÑO",
    "MARMAÐA": "MARMAÑA",
    "CARRIÐO": "CARRIÑO",
    "ORDUÐES": "ORDUÑES",
    "CHAVIÐA": "CHAVIÑA",
    "MAÐUECO": "MAÑUECO",
    "SHESEÐA": "SHESEÑA",
    "VRISEÐO": "VRISEÑO",
    "SALVAÐO": "SALVAÑO",
    "CAÐAMAR": "CAÑAMAR",
    "CENTEÐO": "CENTEÑO",
    "LONDOÐO": "LONDOÑO",
    "RUBIÐOZ": "RUBIÑOZ",
    "SALDEÐA": "SALDEÑA",
    "IÐIQUEZ": "IÑIQUEZ",
    "COPTIÐO": "COPTIÑO",
    "VIDAÐOS": "VIDAÑOS",
    "CAÐEROS": "CAÑEROS",
    "ZALDAÐA": "ZALDAÑA",
    "BIBAÐOS": "BIBAÑOS",
    "CASAÐOS": "CASAÑOS",
    "PEÐAGIO": "PEÑAGIO",
    "ALBAÐEZ": "ALBAÑEZ",
    "CABAÐEZ": "CABAÑEZ",
    "YÐIGUEZ": "YÑIGUEZ",
    "SABIÐON": "SABIÑON",
    "CERMEÐO": "CERMEÑO",
    "TOTOÐHO": "TOTOÑHO",
    "VIRUEÐA": "VIRUEÑA",
    "GORRIÐO": "GORRIÑO",
    "CAMPIÐA": "CAMPIÑA",
    "BOLAÐOZ": "BOLAÑOZ",
    "CRECEÐO": "CRECEÑO",
    "CABAÐAZ": "CABAÑAZ",
    "MARDOÐA": "MARDOÑA",
    "GALDUÐO": "GALDUÑO",
    "OTOÐIEL": "OTOÑIEL",
    "CHAPEÐA": "CHAPEÑA",
    "MENDAÐO": "MENDAÑO",
    "PIÐEIRA": "PIÑEIRA",
    "ARMEÐIA": "ARMEÑIA",
    "ÐURINDA": "ÑURINDA",
    "MONTAÐA": "MONTAÑA",
    "VIÐALES": "VIÑALES",
    "PEÐAGOS": "PEÑAGOS",
    "SALDAÐO": "SALDAÑO",
    "ANTUÐEZ": "ANTUÑEZ",
    "LACHEÐO": "LACHEÑO",
    "PARDIÐA": "PARDIÑA",
    "GARDOÐO": "GARDOÑO",
    "PEÐALVA": "PEÑALVA",
    "RIGÐACK": "RIGÑACK",
    "MUÐOZ": "MUÑOZ",
    "NUÐEZ": "NUÑEZ",
    "YAÐEZ": "YAÑEZ",
    "MUÐIZ": "MUÑIZ",
    "ACUÐA": "ACUÑA",
    "BAÐOS": "BAÑOS",
    "OCAÐA": "OCAÑA",
    "AVIÐA": "AVIÑA",
    "PIÐON": "PIÑON",
    "UREÐA": "UREÑA",
    "NIÐOS": "NIÑOS",
    "MUÐOS": "MUÑOS",
    "OMAÐA": "OMAÑA",
    "CAÐAS": "CAÑAS",
    "RIAÐO": "RIAÑO",
    "MAÐON": "MAÑON",
    "NUÐES": "NUÑES",
    "BREÐA": "BREÑA",
    "IPIÐA": "IPIÑA",
    "CAÐEZ": "CAÑEZ",
    "OÐATE": "OÑATE",
    "MIÐON": "MIÑON",
    "YAÐES": "YAÑES",
    "ADOÐO": "ADOÑO",
    "LIÐAN": "LIÑAN",
    "NAÐEZ": "NAÑEZ",
    "UREÐO": "UREÑO",
    "MUÐOA": "MUÑOA",
    "IÐAKI": "IÑAKI",
    "CAÐAL": "CAÑAL",
    "VIÐAS": "VIÑAS",
    "REAÐO": "REAÑO",
    "DOÐAN": "DOÑAN",
    "PAÐOL": "PAÑOL",
    "OTUÐO": "OTUÑO",
    "NAÐES": "NAÑES",
    "NIÐEZ": "NIÑEZ",
    "UVIÐA": "UVIÑA",
    "UMAÐA": "UMAÑA",
    "ÐAÐEZ": "ÑAÑEZ",
    "OLOÐO": "OLOÑO",
    "PIÐAS": "PIÑAS",
    "SEÐOR": "SEÑOR",
    "NUÐOZ": "NUÑOZ",
    "MAÐOZ": "MAÑOZ",
    "ÐORBE": "ÑORBE",
    "IÐIGO": "IÑIGO",
    "PIÐAL": "PIÑAL",
    "ABIÐA": "ABIÑA",
    "UBIÐA": "UBIÑA",
    "NIÐON": "NIÑON",
    "YPIÐA": "YPIÑA",
    "BAEÐA": "BAEÑA",
    "YÐIGO": "YÑIGO",
    "ARIÐO": "ARIÑO",
    "OCAÐO": "OCAÑO",
    "PEÐA": "PEÑA",
    "PIÐA": "PIÑA",
    "NIÐO": "NIÑO",
    "NUÐO": "NUÑO",
    "CAÐA": "CAÑA",
    "DOÐA": "DOÑA",
    "RAÐO": "RAÑO",
    "CAÐO": "CAÑO",
    "ÐECO": "ÑECO",
    "ÐOMA": "ÑOMA",
    "PAÐA": "PAÑA",
    "GEÐA": "GEÑA",
    "VIÐA": "VIÑA",
    "AÐAS": "AÑAS",
    "FAÐA": "FAÑA",
    "DOÐU": "DOÑU",
    "TOÐA": "TOÑA",
    "DAÐU": "DAÑU",
    "UÐA": "UÑA",
    "OÐA": "OÑA",

    # 1.3 Correcciones con secuencias UTF-8 rotas (Ã‘, ÃA, Ã?, etc.)
    "VILLASEÃ‘OR": "VILLASEÑOR",
    "SANTIBAÃ‘EZ": "SANTIBAÑEZ",
    "CASTAÃ‘EDA": "CASTAÑEDA",
    "HERNÃ\x8dNDEZ": "HERNANDEZ", # Á corregida a código exacto
    "VILLASEÃ‘OR": "VILLASEÑOR",
    "GUTIÃ\x89RREZ": "GUTIERREZ", # É corregida a código exacto
    "VILLAFAÃ‘A": "VILLAFAÑA",
    "VILLICAÃ‘A": "VILLICAÑA",
    "QUIÃ‘ONES": "QUIÑONES",
    "AVENDAÃ‘O": "AVENDAÑO",
    "MONTAÃ‘EZ": "MONTAÑEZ",
    "BAÃ‘UELOS": "BAÑUELOS",
    "QUIÃ‘ONEZ": "QUIÑONEZ",
    "CASTAÃ‘EDA": "CASTAÑEDA",
    "VILLICAÃ‘A": "VILLICAÑA",
    "GONZÃ\x81LEZ": "GONZALEZ", # Á corregida a código exacto
    "MARTÃ\x8dNEZ": "MARTINEZ", # Í corregida a código exacto
    "PEÃ‘ALOZA": "PEÑALOZA",
    "CASTAÃ‘ON": "CASTAÑON",
    "ORDOÃ‘EZ": "ORDOÑEZ",
    "MARAÃ‘ON": "MARAÑON",
    "QUIÃ‘ONEZ": "QUIÑONEZ",
    "MONTAÃ‘EZ": "MONTAÑEZ",
    "CARCAÃ‘O": "CARCAÑO",
    "CARREÃ‘O": "CARREÑO",
    "BOLAÃ‘OS": "BOLAÑOS",
    "MONTAÃ‘O": "MONTAÑO",
    "COUTIÃ‘O": "COUTIÑO",
    "GARDUÃ‘O": "GARDUÑO",
    "IÃ‘IGUEZ": "IÑIGUEZ",
    "BRISEÃ‘O": "BRISEÑO",
    "CASTAÃ‘ON": "CASTAÑON",
    "ESCAREÃ‘O": "ESCAREÑO",
    "BRICEÃ‘O": "BRICEÑO",
    "SALDAÃ‘A": "SALDAÑA",
    "SÃ\x81NCHEZ": "SANCHEZ", # Á corregida a código exacto
    "CARDEÃ‘A": "CARDEÑA",
    "MUÃ‘OZ": "MUÑOZ",
    "NUÃ‘EZ": "NUÑEZ",
    "ZUÃ‘IGA": "ZUÑIGA",
    "YAÃ‘EZ": "YAÑEZ",
    "OCAÃ‘A": "OCAÑA",
    "ACUÃ‘A": "ACUÑA",
    "MAGAÃ‘A": "MAGAÑA",
    "\ufffdNGEL": "ANGEL",
    "MUÃ‘IZ": "MUÑIZ",
    "CECEÃ‘A": "CECEÑA",
    "MARÃ\x8dA": "MARIA", # Í corregida a código exacto
    "PIÃ‘ON": "PIÑON",
    "PEÃ‘A": "PEÑA",
    "PIÃ‘A": "PIÑA",
    "NIÃ‘O": "NIÑO",

    # 1.4 Correcciones con comodines inversos (¿)
    # ¡PRECAUCIÓN! Estas palabras estaban así en el CSV, pero el \ufffd es más seguro
    # Las dejo porque si el sistema fuente mandó textualmente el caracter '¿', esto lo arregla.
    "SANTIBA¿EZ": "SANTIBAÑEZ",
    "HERIBERTO¿": "HERIBERTOÑ", # (Curioso nombre)
    "CASTA¿EDA": "CASTAÑEDA",
    "PE¿ALOZA": "PEÑALOZA",
    "PATI¿O": "PATIÑO",
    "MAGA¿A": "MAGAÑA",
    "TREVI¿O": "TREVIÑO",
    "YA¿EZ": "YAÑEZ",
    "NU¿EZ": "NUÑEZ",
    "BA¿OS": "BAÑOS",
    "TU¿ON": "TUÑON",
    "PE¿A": "PEÑA",
    "NI¿O": "NIÑO",
    "PI¿A": "PIÑA",
    "MA¿": "MAÑ",

    # ==========================================================================
    # NIVEL 2: PATRONES COMPLEJOS (Validación Histórica)
    # ==========================================================================
    "A¯ ¿ ¿": "Ñ",
    "AƑ˜": "Ñ",

    # ==========================================================================
    # NIVEL 3: DOUBLE ENCODING (UTF-8 bytes interpretados como Latin-1)
    # Mapeo exacto de bytes. Ordenados de mayor a menor longitud para evitar colisiones.
    # ==========================================================================
    "ÃƒÂ±": "Ñ",
    "ÃƒÂ‘": "Ñ",
    "Ã\x8d": "I", 
    "Ã\x81": "A", 
    "Ã‘": "Ñ",
    "Ã±": "Ñ",
    "Ã‰": "E",
    "Ã“": "O",
    "Ã”": "O",
    "Ã…": "A",
    "Ã¡": "A",
    "Ã©": "E",
    "Ã­": "I",    
    "Ã³": "O",
    "Ãº": "U",
    "Ãš": "U",
    "ÃŒ": "U",
    "Ã‡": " ",    

    # ==========================================================================
    # NIVEL 4: SÍMBOLOS Y BASURA (Fallback de Seguridad)
    # Solo limpieza de basura invisible y caracteres de escape.
    # ==========================================================================
    "CIA “N": "CION",
    "CIA“N": "CION",
    "ARÑR": "O",
    "Ð": "Ñ",
    "ð": "ñ",
    "Ƒ˜": "Ñ",
    "â€¦": "",   
    "Â·": "",    
    "˜": "",     
    "Ƒ": "",
    "¨": "",     
    "´": "",     
    "™": "",     
    "&AMP;": "&",
    "&QUOT;": '"',  
    "&APOS;": "'",
    "&LT;": "<",
    "&GT;": ">"
}