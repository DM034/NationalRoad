from django.db import models
import psycopg2

# Create your models here.

class Postgre:
    def connexion():
        con = psycopg2.connect(
            host = "localhost",
            database = "natroad",
            user = "postgres",
            password = "366325"
        )

        # cur = con.cursor()

        # cur.execute("""
        #     CREATE TABLE personne(
        #     id INT,
        #     prenom VARCHAR,
        #     nom VARCHAR,
        #     date_naissance DATE
        #     )
        # """)

        # liste = [
        #     ('DM','Michael','1945-02-06'),
        #     ('Maroussia','Malala','1945-02-06'),
        #     ('Damian','Marley','1945-02-06')
        # ]
        # cur.executemany("""
        #     INSERT INTO personne VALUES(NULL,%s,%s,%s)
        # """, liste)

        # cur.execute("SELECT * FROM personne order by nom")

        # print(cur.fetchone())

        # for e in cur.fetchall():
        #     print(e[1])

        # for e in cur.fetchmany():
        #     print(e[1])


        # cur.close()

        # con.commit()

        # con.close()
        return con

class ecole:
    def __init__(self, id=0, nom='', geom=''):
        self.id = id
        self.nom = nom
        self.geom = geom

class Type:
    def __init__(self, id=0, nom='', cout=0, duree=0):
        self.id = id
        self.nom = nom
        self.cout = cout
        self.duree = duree

    def getPrix(self, quantite):
        return self.cout * quantite

    def calcDuree(self, quantite):
        return self.duree * quantite
    
class Hole:
    def __init__(self, id=0, pk_start=0, pk_end=0, geom='', note=0, id_road=0):
        self.id = id
        self.pk_start = pk_start
        self.pk_end = pk_end
        self.geom = geom
        self.note = note
        self.id_road = id_road

    def quantite(self):
        distance = self.pk_end - self.pk_start
        val = (distance * 1000) * 5 * self.note * 0.1 / 100
        return val 

    @staticmethod
    def insertHole(pk_start,pk_end,L1,l1,L2,l2,note,id_road,largeur):
        con = Postgre.connexion()
        cur = con.cursor()
        sql="INSERT INTO hole VALUES(default,{},{},'Linestring({} {},{} {})',{},{},{})".format(pk_start,pk_end,L1,l1,L2,l2,note,id_road,largeur)
        cur.execute(sql)
        con.commit()
        con.close()
    
    @staticmethod
    def getHopital(dist):
        con = Postgre.connexion()
        cur = con.cursor()
        cur.execute("SELECT ROAD.id,ROAD.NOM, count(*) AS nbhopital FROM hopital,ROAD WHERE  (st_distancesphere(ROAD.geom,hopital.geom))<='"+str(dist)+"' group by ROAD.id, ROAD.NOM order by nbhopital desc")
        rows = cur.fetchall()
        con.close()
        return rows
    
    @staticmethod
    def getEcole(dist):
        con = Postgre.connexion()
        cur = con.cursor()
        cur.execute("SELECT ROAD.id,ROAD.NOM, count(*) AS nbecole FROM ecole,ROAD WHERE  (st_distancesphere(ROAD.geom,ecole.geom))<='"+str(dist)+"' group by ROAD.id, ROAD.NOM order by nbecole desc")
        rows = cur.fetchall()
        con.close()
        return rows

    @staticmethod
    def getPopulation(dist):
        con = Postgre.connexion()
        cur = con.cursor()
        cur.execute("SELECT ROAD.id,ROAD.NOM, sum(village.nb) AS nbpop FROM village,ROAD WHERE  (st_distancesphere(ROAD.geom,village.geom))<='"+str(dist)+"' group by ROAD.id, ROAD.NOM order by nbpop desc")
        rows = cur.fetchall()
        con.close()
        return rows

class hopital:
    def __init__(self, id=0, nom='', geom=''):
        self.id = id
        self.nom = nom
        self.geom = geom

class infohole:
    def __init__(self, id=0, pk_start=0, pk_end=0, note=0, geom='', idtype=0):
        self.id = id
        self.pk_start = pk_start
        self.pk_end = pk_end
        self.note = note
        self.geom = geom
        self.idtype = idtype

    def quantite(self):
        distance = self.pk_end - self.pk_start
        val = (distance * 1000) * 5 * self.note * 0.1 / 100
        return val 
    

class Road:
    def __init__(self, id=0, nom='', pk_start=0, pk_end=0, geom='', idtype=0):       #construct
        self.id = id
        self.nom = nom
        self.pk_start = pk_start
        self.pk_end = pk_end
        self.geom = geom
        self.idtype = idtype

    @staticmethod
    def getRoadName():
        con = Postgre.connexion()
        cur = con.cursor()
        cur.execute("select road.id, road.nom, sum(((((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100)*type.cout)) as price,sum(((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100) as volume, sum(((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100*type.duree) as duree from road join hole on hole.id_road = road.id join type on road.idtype = type.id group by road.id order by road.id desc")
        rows = cur.fetchall()
        con.close()
        return rows
    
    def getAllHole(self):
        con = Postgre.connexion()
        cur = con.cursor()
        cur.execute("select road.id, road.nom, sum(((((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100)*type.cout)) as price,sum(((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100) as volume, sum(((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100*type.duree) as duree from road join hole on hole.id_road = road.id join type on road.idtype = type.id group by road.id order by road.id asc")
        rows = cur.fetchall()
        con.close()
        return rows

    def difference(pk_start, pk_end):
        return pk_end - pk_start

class village:
    def __init__(self, id=0, nb=0, geom=''):
        self.id = id
        self.nb = nb
        self.geom = geom
