begin work;
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('_NA_',NULL,NULL,'Not Applicable','2023-07-13 23:14:34.887+05:30','2023-07-13 23:14:34.887+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SYNCHRONIZE_STATUS',NULL,'N','Synchronize','2023-07-13 23:14:35.299+05:30','2023-07-13 23:14:35.299+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('KEYWORD_STATUS',NULL,'N','Keyword','2023-07-13 23:14:36.239+05:30','2023-07-13 23:14:36.239+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SERVICE_STATUS',NULL,'N','Scheduled Service','2023-07-13 23:14:50.241+05:30','2023-07-13 23:14:50.241+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('ENTSYNC_RUN',NULL,'N','Entity Sync Run','2023-07-13 23:14:50.846+05:30','2023-07-13 23:14:50.846+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PARTY_STATUS',NULL,'N','Party','2023-07-13 23:14:52.813+05:30','2023-07-13 23:14:52.813+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('CASE_STATUS',NULL,'N','Case','2023-07-13 23:14:52.825+05:30','2023-07-13 23:14:52.825+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('COM_EVENT_STATUS',NULL,'N','Communication Event','2023-07-13 23:14:52.827+05:30','2023-07-13 23:14:52.827+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('COM_EVENT_ROL_STATUS','COM_EVENT_STATUS','N','Communication Event Role','2023-07-13 23:14:52.911+05:30','2023-07-13 23:14:52.911+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PARTY_REL_STATUS',NULL,'N','Party Relationship','2023-07-13 23:14:52.932+05:30','2023-07-13 23:14:52.932+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PARTY_INV_STATUS',NULL,'N','Party Invitation','2023-07-13 23:14:52.941+05:30','2023-07-13 23:14:52.941+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('CNTNTAPPR_STATUS',NULL,'N','Content Approval Status','2023-07-13 23:14:53.811+05:30','2023-07-13 23:14:53.811+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SERVER_HIT_STATUS',NULL,'N','Server Hit','2023-07-13 23:14:56.053+05:30','2023-07-13 23:14:56.053+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WEB_CONTENT_STATUS',NULL,'N','Web Content','2023-07-13 23:14:56.054+05:30','2023-07-13 23:14:56.054+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('CONTENT_STATUS',NULL,'N','Content','2023-07-13 23:14:56.059+05:30','2023-07-13 23:14:56.059+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WORK_EFF_ASSET_STTS',NULL,'N','WorkEffort Asset','2023-07-13 23:15:00.548+05:30','2023-07-13 23:15:00.548+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WORK_EFFORT_ASSIGN',NULL,'N','WorkEffort Assignment','2023-07-13 23:15:00.551+05:30','2023-07-13 23:15:00.551+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WORK_EFFORT_STATUS',NULL,'N','Workeffort','2023-07-13 23:15:00.553+05:30','2023-07-13 23:15:00.553+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('CALENDAR_STATUS','WORK_EFFORT_STATUS','N','Calendar','2023-07-13 23:15:00.554+05:30','2023-07-13 23:15:00.554+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('TASK_STATUS','CALENDAR_STATUS','N','Task','2023-07-13 23:15:00.589+05:30','2023-07-13 23:15:00.589+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('EVENT_STATUS','CALENDAR_STATUS','N','Event','2023-07-13 23:15:00.603+05:30','2023-07-13 23:15:00.603+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('TIMESHEET_STATUS',NULL,'N','Timesheet','2023-07-13 23:15:00.626+05:30','2023-07-13 23:15:00.626+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WE_PROJECT_STATUS','WORK_EFFORT_STATUS','N','Project','2023-07-13 23:15:00.645+05:30','2023-07-13 23:15:00.645+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PRTYASGN_STATUS','WORK_EFFORT_STATUS','N','Party Assignment Status','2023-07-13 23:15:00.665+05:30','2023-07-13 23:15:00.665+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WEPA_AVAILABILITY',NULL,'N','Work Effort Party Availability','2023-07-13 23:15:00.676+05:30','2023-07-13 23:15:00.676+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('FA_ASGN_STATUS',NULL,'N','Fixed Asset Assignment Status','2023-07-13 23:15:00.684+05:30','2023-07-13 23:15:00.684+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WEFA_AVAILABILITY',NULL,'N','Work Effort Fixed Asset Availability','2023-07-13 23:15:00.692+05:30','2023-07-13 23:15:00.692+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('ROUTING_STATUS','WORK_EFFORT_STATUS','N','Manufacturing Task and Routing status','2023-07-13 23:15:00.828+05:30','2023-07-13 23:15:00.828+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PRODUCTION_RUN','WORK_EFFORT_STATUS','N','Production Run Status','2023-07-13 23:15:00.834+05:30','2023-07-13 23:15:00.834+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WEFG_STATUS',NULL,'N','Work Effort Good Standard Status','2023-07-13 23:15:00.872+05:30','2023-07-13 23:15:00.872+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('WEFF_REVIEW_STTS',NULL,'N','WorkEffort Review','2023-07-13 23:15:00.877+05:30','2023-07-13 23:15:00.877+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('INVENTORY_ITEM_STTS',NULL,'N','Inventory Item','2023-07-13 23:15:02.305+05:30','2023-07-13 23:15:02.305+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('INV_SERIALIZED_STTS','INVENTORY_ITEM_STTS','N','Serialized Inventory Item','2023-07-13 23:15:02.307+05:30','2023-07-13 23:15:02.307+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('INV_NON_SER_STTS','INVENTORY_ITEM_STTS','N','Non-Serialized Inventory Item','2023-07-13 23:15:02.309+05:30','2023-07-13 23:15:02.309+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('INVENTORY_XFER_STTS',NULL,'N','Inventory Transfer','2023-07-13 23:15:02.419+05:30','2023-07-13 23:15:02.419+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PRODUCT_REVIEW_STTS',NULL,'N','Product Review','2023-07-13 23:15:02.479+05:30','2023-07-13 23:15:02.479+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('IMAGE_MANAGEMENT_ST',NULL,'N','Image Management','2023-07-13 23:15:02.589+05:30','2023-07-13 23:15:02.589+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('GROUP_ORDER_STATUS',NULL,'N','Group Order Status','2023-07-13 23:15:02.669+05:30','2023-07-13 23:15:02.669+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SHIPMENT_STATUS',NULL,'N','Shipment','2023-07-13 23:15:03.41+05:30','2023-07-13 23:15:03.41+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PURCH_SHIP_STATUS',NULL,'N','Purchase Shipment','2023-07-13 23:15:03.47+05:30','2023-07-13 23:15:03.47+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SHPRTSG_CS_STATUS',NULL,'N','ShipmentRouteSegment:CarrierService','2023-07-13 23:15:03.512+05:30','2023-07-13 23:15:03.512+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PICKLIST_STATUS',NULL,'N','Picklist','2023-07-13 23:15:03.581+05:30','2023-07-13 23:15:03.581+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PICKITEM_STATUS',NULL,'N','Picklist Item','2023-07-13 23:15:03.651+05:30','2023-07-13 23:15:03.651+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('ACCTG_ENREC_STATUS',NULL,'N','Acctg Entry Reconcile','2023-07-13 23:15:14.811+05:30','2023-07-13 23:15:14.811+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('FINACCT_STATUS',NULL,'N','Financial Account Status','2023-07-13 23:15:14.94+05:30','2023-07-13 23:15:14.94+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('FINACT_TRNS_STATUS',NULL,'N','Financial Account Trans Status','2023-07-13 23:15:14.964+05:30','2023-07-13 23:15:14.964+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('FIXEDAST_MNT_STATUS',NULL,'N','Fixed Asset Maintenance','2023-07-13 23:15:15.079+05:30','2023-07-13 23:15:15.079+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('BUDGET_STATUS',NULL,'N','Budget','2023-07-13 23:15:16.448+05:30','2023-07-13 23:15:16.448+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PARTY_ASSET_STATUS',NULL,'N','Party Asset','2023-07-13 23:15:16.449+05:30','2023-07-13 23:15:16.449+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('INVOICE_STATUS',NULL,'N','Invoice Status','2023-07-13 23:15:16.452+05:30','2023-07-13 23:15:16.452+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PMNT_STATUS',NULL,'N','Payment Status','2023-07-13 23:15:16.529+05:30','2023-07-13 23:15:16.529+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('GLREC_STATUS',NULL,'N','Gl Reconciliation Status','2023-07-13 23:15:17.164+05:30','2023-07-13 23:15:17.164+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('EMPLOYMENT_APP_STTS',NULL,'N','Employment Application','2023-07-13 23:15:26.211+05:30','2023-07-13 23:15:26.211+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('EMPL_POSITION_STATUS',NULL,'N','Employee Position Status','2023-07-13 23:15:26.213+05:30','2023-07-13 23:15:26.213+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('UNEMPL_CLAIM_STATUS',NULL,'N','Unemployment Claim','2023-07-13 23:15:26.227+05:30','2023-07-13 23:15:26.227+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('HR_DEGREE_STATUS',NULL,'N','Degree status','2023-07-13 23:15:26.23+05:30','2023-07-13 23:15:26.23+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('HR_JOB_STATUS',NULL,'N','Job status','2023-07-13 23:15:26.242+05:30','2023-07-13 23:15:26.242+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PARTYQUAL_VERIFY',NULL,'N','PartyQual verification status','2023-07-13 23:15:26.26+05:30','2023-07-13 23:15:26.26+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('IJP_STATUS',NULL,NULL,'Internal Job Posting Status','2023-07-13 23:15:26.275+05:30','2023-07-13 23:15:26.275+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('RELOCATION_STATUS',NULL,NULL,'Relocation Status','2023-07-13 23:15:26.286+05:30','2023-07-13 23:15:26.286+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('TRAINING_STATUS',NULL,NULL,'Training Status','2023-07-13 23:15:26.293+05:30','2023-07-13 23:15:26.293+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('LEAVE_STATUS',NULL,NULL,'Employee Leave Status','2023-07-13 23:15:26.319+05:30','2023-07-13 23:15:26.319+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('ORDER_STATUS',NULL,'N','Order','2023-07-13 23:15:28.484+05:30','2023-07-13 23:15:28.484+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('ORDER_ITEM_STATUS','ORDER_STATUS','N','Order Item','2023-07-13 23:15:28.52+05:30','2023-07-13 23:15:28.52+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PAYMENT_PREF_STATUS',NULL,'N','Payment Preference','2023-07-13 23:15:28.641+05:30','2023-07-13 23:15:28.641+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('ORDER_DEL_SCH',NULL,'N','Order Delivery Schedule','2023-07-13 23:15:28.694+05:30','2023-07-13 23:15:28.694+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('ORDER_RETURN_STTS',NULL,'N','Order Return Status For Customer Returns','2023-07-13 23:15:28.747+05:30','2023-07-13 23:15:28.747+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PORDER_RETURN_STTS',NULL,'N','Order Return Status For Supplier Returns','2023-07-13 23:15:28.791+05:30','2023-07-13 23:15:28.791+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('CUSTREQ_STTS',NULL,'N','Custom Request Status','2023-07-13 23:15:28.829+05:30','2023-07-13 23:15:28.829+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('REQUIREMENT_STATUS',NULL,'N','Requirement Status','2023-07-13 23:15:28.923+05:30','2023-07-13 23:15:28.923+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('QUOTE_STATUS',NULL,'N','Quote Status','2023-07-13 23:15:28.966+05:30','2023-07-13 23:15:28.966+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('MKTG_CAMP_STATUS',NULL,'N','Marketing Campaign','2023-07-13 23:15:30.123+05:30','2023-07-13 23:15:30.123+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('CONTACTLST_PARTY',NULL,'N','Contact List Party','2023-07-13 23:15:30.167+05:30','2023-07-13 23:15:30.167+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('LEAD_STATUS','PARTY_STATUS',NULL,'Lead Status','2023-07-13 23:15:30.3+05:30','2023-07-13 23:15:30.3+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PROJECT',NULL,'N','Project','2023-07-13 23:15:33.686+05:30','2023-07-13 23:15:33.686+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PROJECT_STATUS','PROJECT','N','Project status','2023-07-13 23:15:33.687+05:30','2023-07-13 23:15:33.687+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PROJECT_TASK_STATUS','PROJECT','N','Project Task','2023-07-13 23:15:33.689+05:30','2023-07-13 23:15:33.689+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PROJECT_ASSGN_STATUS','PROJECT','N','Project Assignment','2023-07-13 23:15:33.691+05:30','2023-07-13 23:15:33.691+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SCRUM_PROJECT_STATUS',NULL,'N','Scrum Project status','2023-07-13 23:15:34.806+05:30','2023-07-13 23:15:34.806+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SPRINT_STATUS',NULL,'N','Sprint Status','2023-07-13 23:15:34.808+05:30','2023-07-13 23:15:34.808+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SCRUM_TASK_STATUS',NULL,'N','Scrum Task','2023-07-13 23:15:34.81+05:30','2023-07-13 23:15:34.81+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('PRODUCT_STATUS',NULL,'N','Product Status','2023-07-13 23:15:34.811+05:30','2023-07-13 23:15:34.811+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('SCRUM_ASSGN_STATUS',NULL,'N','Scrum Assignment','2023-07-13 23:15:34.84+05:30','2023-07-13 23:15:34.84+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('POSTX_STATUS',NULL,'N','Pos Transaction','2023-07-13 23:15:38.488+05:30','2023-07-13 23:15:38.488+05:30');
INSERT INTO hrms.status_type (status_type_id,parent_type_id,has_table,description,created_stamp,updated_stamp) values('EXAMPLE_STATUS',NULL,'N','Example','2023-07-13 23:17:24.49+05:30','2023-07-13 23:17:24.49+05:30');
commit;
