CREATE DATABASE nationalRoad;

CREATE TABLE type(
    id SERIAL PRIMARY KEY,
    nom VARCHAR,
    cout FLOAT8,
    duree FLOAT8
);

CREATE TABLE road(
    id SERIAL PRIMARY KEY,
    nom VARCHAR,
    pk_start INT,
    pk_end INT,
    geom GEOMETRY(LINESTRING),
    idtype INT,
    FOREIGN KEY (idtype) REFERENCES type(id)
);

CREATE TABLE hole(
    id SERIAL PRIMARY KEY,
    pk_start INT,
    pk_end INT,
    geom GEOMETRY(LINESTRING),
    note INT,
    id_road INT,
    FOREIGN KEY (id_road) REFERENCES road(id)
);

CREATE TABLE ecole(
    id SERIAL PRIMARY KEY,
    nom VARCHAR,
    geom GEOMETRY(LINESTRING)
);

CREATE TABLE hopital(
    id SERIAL PRIMARY KEY,
    nom VARCHAR,
    geom GEOMETRY(LINESTRING)
);

CREATE TABLE village(
    id SERIAL PRIMARY KEY,
    nb VARCHAR,
    geom GEOMETRY(LINESTRING)
);


INSERT INTO road VALUES(nextval('route'), 'RN2');
INSERT INTO road VALUES(nextval('route'), 'RN7');


INSERT INTO ecole VALUES(default, 'Sekoly1', 'point(47.9995262 -18.8921933)');
INSERT INTO ecole VALUES(default, 'Sekoly2', 'point(47.989484 -18.8878385)');
INSERT INTO ecole VALUES(default, 'Sekoly3', 'point(48.1631291 -18.9107643)');
INSERT INTO ecole VALUES(default, 'Sekoly4', 'point(47.0606723 -19.9156356)');
INSERT INTO ecole VALUES(default, 'Sekoly5', 'point(47.0605435 -19.9255611)');
INSERT INTO ecole VALUES(default, 'Sekoly6', 'point(47.0789636 -20.0647593)');
INSERT INTO ecole VALUES(default, 'Sekoly7', 'point(47.081796 -20.0755622)');
INSERT INTO ecole VALUES(default, 'Sekoly8', 'point(47.0966332 -19.7966552)');
INSERT INTO ecole VALUES(default, 'Sekoly9', 'point(47.1104734 -19.7966148)');


-- UPDATE ROAD SET LONGUEUR = 'LINESTRING(47.48613 -18.86552,47.55752 -18.78943,47.72855 -18.76153,47.71514 -18.89343)' WHERE ID = 1;
-- UPDATE ROAD SET LONGUEUR = 'LINESTRING(47.71514 -18.89343,47.84088 -18.82313,47.77638 -18.72312)' WHERE ID = 2;

INSERT INTO HOLE VALUES(default, 2, 8,'LINESTRING(48.0467218 -18.8768764, 48.0519575 -18.8725314)',15,1,5);
INSERT INTO HOLE VALUES(default, 15, 28,'LINESTRING(47.9894283 -18.8873931, 47.9991486 -18.8915144)',45,1,5);
INSERT INTO HOLE VALUES(default, 65, 85,'LINESTRING(48.1629958 -18.9085121, 48.1721582 -18.9155357)',26,1,5);

INSERT INTO HOLE VALUES(default, 152, 256,'LINESTRING(47.0975661 -19.7917772, 47.0953075 -19.7959843)',28,2,5);
INSERT INTO HOLE VALUES(default, 425, 488,'LINESTRING(47.0587143 -20.0669718, 47.0626196 -20.0775529)',35,2,5);
INSERT INTO HOLE VALUES(default, 521, 528,'LINESTRING(47.0450248 -19.9137168, 47.045116 -19.9268152)',10,2,5);


-- INSERT INTO HOLE VALUES(default, 15, 23, 16, 1, 'LINESTRING(47.69309 -18.76671,47.72663 -18.76208, 47.72605 -18.78406)');

--lalana akaiky hopitaly

SELECT hopital.id, hole.id, ST_Distance(hopital.geom, hole.geom) AS distance
FROM hopital, hole
ORDER BY distance;

--prix et volume

select hole.id, hole.pk_start, hole.pk_end, hole.note, hole.largeur, ((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100 as volume, (((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100)*type.cout as price  from hole, type order by price;

--lalana be hopitaly manodidina

SELECT hole.id,count(*) AS nbhopital FROM hopital,hole 
WHERE  (st_distancesphere(hole.geom,hopital.geom))<=2000 group by hole.id;

--lalana be ecole manodidina

SELECT count(*) AS nbecole FROM ecole,hole 
WHERE  (st_distancesphere(hole.geom,ecole.geom))<=2000 and hole.id=1;

--lalana be population manodidina

SELECT sum(village.nb) AS nbpopulation FROM village,hole 
WHERE  (st_distancesphere(hole.geom,village.geom))<=2000 and hole.id=1;

select road.id, sum(((((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100)*type.cout)) as price,sum(((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100) as volume, sum(((hole.pk_end-hole.pk_start)*1000)*hole.largeur*hole.note*0.1/100*type.duree) as duree from road join hole on hole.id_road = road.id join type on road.idtype = type.id group by road.id;

delete from road;
delete from hole;
delete from hopital;
delete from ecole;
delete from village;



alter sequence road_id_seq restart with 1;
alter sequence hole_id_seq restart with 1;
alter sequence hopital_id_seq restart with 1;
alter sequence ecole_id_seq restart with 1;
alter sequence village_id_seq restart with 1;

