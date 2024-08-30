begin work;
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('AUTOMATED_AGENT',NULL,'N','Automated Agent','2023-07-13 23:14:52.791+05:30','2023-07-13 23:14:52.791+05:30');
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PERSON',NULL,'Y','Person','2023-07-13 23:14:52.795+05:30','2023-07-13 23:14:52.795+05:30');
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PARTY_GROUP',NULL,'Y','Party Group','2023-07-13 23:14:52.797+05:30','2023-07-13 23:14:52.797+05:30');
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('INFORMAL_GROUP','PARTY_GROUP','N','Informal Group','2023-07-13 23:14:52.799+05:30','2023-07-13 23:14:52.799+05:30');
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('FAMILY','INFORMAL_GROUP','N','Family','2023-07-13 23:14:52.802+05:30','2023-07-13 23:14:52.802+05:30');
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('TEAM','INFORMAL_GROUP','N','Team','2023-07-13 23:14:52.805+05:30','2023-07-13 23:14:52.805+05:30');
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('LEGAL_ORGANIZATION','PARTY_GROUP','N','Legal Organization','2023-07-13 23:14:52.807+05:30','2023-07-13 23:14:52.807+05:30');
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('CORPORATION','LEGAL_ORGANIZATION','N','Corporation','2023-07-13 23:14:52.809+05:30','2023-07-13 23:14:52.809+05:30');
INSERT INTO hrms.party_type (party_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('GOVERNMENT_AGENCY','LEGAL_ORGANIZATION','N','Government Agency','2023-07-13 23:14:52.811+05:30','2023-07-13 23:14:52.811+05:30');
INSERT INTO hrms.party (party_id,party_type_id,external_id,description,status_id, created_date , created_stamp,updated_stamp) values('Company','PARTY_GROUP',NULL,'Party Id of the company','PARTY_ENABLED','2023-07-13 23:14:52.811+05:30','2023-07-13 23:14:52.811+05:30','2023-07-13 23:14:52.811+05:30');

commit;
