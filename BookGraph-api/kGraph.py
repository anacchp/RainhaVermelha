from rdflib import Graph, URIRef, Literal ,Namespace
from rdflib.namespace import RDF,RDFS,DC,XSD
from SPARQLWrapper import SPARQLWrapper, JSON

g = Graph()
g.parse(data = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rv: <http://example.org/rainhavermelha#> .

        
# Relacionamentos
rv:followedBy rdf:type rdf:Property .
rv:hasPower rdf:type rdf:Property .
rv:hasBlood rdf:type rdf:Property .
rv:family rdf:type rdf:Property .
rv:tricked rdf:type rv:Character .
rv:marriedTo rdf:type rv:Character .
rv:wasMarriedTo rdf:type rv:Character .
rv:sonOf rdf:type rv:Character .
rv:daughterOf rdf:type rv:Character .
rv:fatherOf rdf:type rv:Character .
rv:motherOf rdf:type rv:Character .
rv:sisterOf rdf:type rv:Character .
rv:brotherOf rdf:type rv:Character .
rv:bestfriendOf rdf:type rv:Character .


# Sangue
rv:Vermelho rdf:type rv:Blood ;
    rv:name "Sangue Vermelho" .

rv:Prateado rdf:type rv:Blood ;
    rv:name "Sangue Prateado" .
        
rv:SangueNovo rdf:type rv:Blood ; 
    rv:name "Sangue novo" .

        
# Poderes
rv:Eletricidade rdf:type rv:Power ;
    rv:name "Eletricidade" ;
    rv:description "Manipular Eletricidade" .

rv:Fogo rdf:type rv:Power ;
    rv:name "Fogo" ;
    rv:description "Manipular Fogo" .
        
rv:Murmurio rdf:type rv:Power ;
    rv:name "Murmurio" ;
    rv:description "Ler e Controlar a mente atraves de sussurros" . 

rv:Metal rdf:type rv:Power ;
    rv:name "Metal" ;
    rv:description "Manipular Metal" .

rv:Cura rdf:type rv:Power ;
    rv:name "Cura" ;
    rv:description "Curar feridas e machucados pelo toque" .
        
rv:Canto rdf:type rv:Power ;
    rv:name "Canto" ;
    rv:description "Hipnose atraves do canto" .

rv:Teletransporte rdf:type rv:Power ;
    rv:name "Teletransporte" ;
    rv:description "Se teletransportar" .
        

# Personagens
rv:MareBarrow rdf:type rv:Character ;
    rv:name "Mare Barrow" ;
    rv:family "Barrow" ;
    rv:hasBlood rv:SangueNovo ;
    rv:hasPower rv:Eletricidade ;
    rv:daughterOf rv:DanielBarrow, rv:RuthBarrow ;
    rv:sisterOf rv:GisaBarrow, rv:BreeBarrow, rv:TramyBarrow, rv:ShadeBarrow ;
    rv:bestfriendOf rv:KilornWarren .

rv:TiberiasCalore rdf:type rv:Character ;
    rv:name "Tiberias Calore" ;
    rv:family "Calore" ;
    rv:hasBlood rv:Prateado ;
    rv:hasPower rv:Fogo ;
    rv:sonOf rv:ReiTiberiasCalore, rv:CorianeJacos ;
    rv:brotherOf rv:MavenCalore .

rv:MavenCalore rdf:type rv:Character ;
    rv:name "Maven Calore" ;
    rv:family "Calore" ;
    rv:hasBlood rv:Prateado ;
    rv:hasPower rv:Fogo ;
    rv:tricked rv:MareBarrow ;
    rv:sonOf rv:ReiTiberiasCalore, rv:RainhaElara;
    rv:brotherOf rv:TiberiasCalore .

rv:KilornWarren rdf:type rv:Character ;
    rv:name "Kilorn Warren" ;
    rv:hasBlood rv:Vermelho ;
    rv:bestfriendOf rv:MareBarrow .
        
rv:DanielBarrow rdf:type rv:Character ;
    rv:name "Daniel Barrow" ;
    rv:family "Barrow" ;
    rv:hasBlood rv:Vermelho ;
    rv:marriedTo rv:RuthBarrow ;
    rv:fatherOf rv:MareBarrow, rv:BreeBarrow, rv:TramyBarrow, rv:ShadeBarrow , rv:GisaBarrow .

rv:RuthBarrow rdf:type rv:Character ;
    rv:name "Ruth Barrow" ;
    rv:family "Barrow" ;
    rv:hasBlood rv:Vermelho ;
    rv:marriedTo rv:DanielBarrow ;
    rv:motherOf rv:MareBarrow, rv:BreeBarrow, rv:TramyBarrow, rv:ShadeBarrow , rv:GisaBarrow .

rv:GisaBarrow rdf:type rv:Character ;
    rv:name "Gisa Barrow" ;
    rv:family "Barrow" ;
    rv:hasBlood rv:Vermelho ;
    rv:daughterOf rv:DanielBarrow, rv:RuthBarrow ;
    rv:sisterOf rv:MareBarrow, rv:BreeBarrow, rv:TramyBarrow, rv:ShadeBarrow .

rv:BreeBarrow rdf:type rv:Character ;
    rv:name "Bree Barrow" ;
    rv:family "Barrow" ;
    rv:hasBlood rv:Vermelho ;
    rv:sonOf rv:DanielBarrow, rv:RuthBarrow ;
    rv:brotherOf rv:MareBarrow, rv:GisaBarrow, rv:TramyBarrow, rv:ShadeBarrow .
        
rv:TramyBarrow rdf:type rv:Character ;
    rv:name "Tramy Barrow" ;
    rv:family "Barrow" ;
    rv:hasBlood rv:Vermelho ;
    rv:sonOf rv:DanielBarrow, rv:RuthBarrow ;
    rv:brotherOf rv:MareBarrow, rv:GisaBarrow, rv:BreeBarrow, rv:ShadeBarrow .
        
rv:ShadeBarrow rdf:type rv:Character ;
    rv:name "Shade Barrow" ;
    rv:family "Barrow" ;
    rv:hasBlood rv:SangueNovo ;
    rv:hasPower rv:Teletransporte ;
    rv:sonOf rv:DanielBarrow, rv:RuthBarrow ;
    rv:brotherOf rv:MareBarrow, rv:GisaBarrow, rv:TramyBarrow, rv:BreeBarrow .

rv:EvangelineSamos rdf:type rv:Character ;
    rv:name "Evangeline Samos" ;
    rv:family "Samos" ;
    rv:hasBlood rv:Prateado ;
    rv:hasPower rv:Metal .

rv:RainhaElara rdf:type rv:Character ;
    rv:name "Rainha Elara" ;
    rv:family "Merandus" ;
    rv:hasBlood rv:Prateado ;
    rv:hasPower rv:Murmurio ;
    rv:marriedTo rv:ReiTiberiasCalore ;
    rv:motherOf rv:MavenCalore .
        
rv:ReiTiberiasCalore rdf:type rv:Character ;
    rv:name "Rei Tiberias Calore" ;
    rv:family "Calore" ;
    rv:hasBlood rv:Prateado ;
    rv:hasPower rv:Fogo ;
    rv:wasMarriedTo rv:CorianeJacos ;
    rv:marriedTo rv:RainhaElara ;
    rv:fatherOf rv:MavenCalore, rv:TiberiasCalore .
        
rv:CorianeJacos rdf:type rv:Character ;
    rv:name "Coriane Jacos" ;
    rv:family "Jacos" ;
    rv:hasBlood rv:Prateado ;
    rv:wasMarriedTo rv:ReiTiberiasCalore ;
    rv:motherOf rv:TiberiasCalore ;
    rv:sisterOf rv:JulianJacos ;
    rv:hasPower rv:Canto .
        
rv:JulianJacos rdf:type rv:Character ;
    rv:name "Julian Jacos" ;
    rv:family "Jacos" ;
    rv:hasBlood rv:Prateado ;
    rv:hasPower rv:Canto ;
    rv:brotherOf rv:CorianeJacos .
        
rv:SaraSkonos rdf:type rv:Character ;
    rv:name "Sara Skonos" ;
    rv:family "Skonos" ;
    rv:hasBlood rv:Prateado ;
    rv:hasPower rv:Cura .


""", format="ttl")

xml_data = g.serialize(format="xml")

queries = ["""SELECT ?resposta WHERE { ?personagem rv:hasBlood rv:SangueNovo. ?personagem rv:name ?resposta }""", """SELECT distinct ?resposta WHERE { {?personagem rv:name ?resposta. ?personagem rv:sisterOf ?irmaos} UNION { ?personagem rv:name ?resposta. ?personagem rv:brotherOf ?irmaosS }}""","""SELECT (COUNT( DISTINCT ?s) as ?resposta) WHERE { ?s  rv:hasBlood ?b }""","""SELECT ?resposta WHERE { ?poder rdf:type rv:Power. ?poder rv:name ?resposta }""","""SELECT ?resposta WHERE { ?personagem rdf:type rv:Character. ?personagem rv:name "Rei Tiberias Calore". ?personagem rv:hasPower ?poder. ?poder rv:name ?resposta }""","""SELECT ?resposta WHERE { rv:EvangelineSamos rv:family ?resposta }""","""SELECT ?resposta (count( ?personagem ) as ?count) WHERE { ?personagem rdf:type rv:Character. ?personagem rv:family ?resposta } GROUP BY ?resposta ORDER BY DESC(?count) LIMIT 1""","""SELECT ?resposta WHERE { ?personagem rdf:type rv:Character. ?personagem rv:name "Mare Barrow". ?personagem rv:hasPower ?poder. ?poder rv:name ?resposta }""","""SELECT ?resposta WHERE { ?personagem rv:name "Rei Tiberias Calore". ?personagem rv:fatherOf ?filhos. ?filhos rv:name ?resposta }""","""SELECT ?resposta WHERE { ?sangue rdf:type rv:Blood. ?sangue rv:name ?resposta }"""]

def get_data():
    dict={}
    list = []
    i = 1

    for q in queries:
        qres = g.query(q)
        for row in qres:
            list.append(row.asdict()['resposta'].toPython())
            #list.append(row.asdict()['resposta'].toPython())
        dict[i] = list
        list = []
        i+=1
    print(dict)
    return dict

