# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from .models import UserLogin

class AccommodationClass(models.Model):
    accommodation_class_id = models.CharField(primary_key=True, max_length=20)
    parent_class = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accommodation_class'


class AccommodationMap(models.Model):
    accommodation_map_id = models.CharField(primary_key=True, max_length=20)
    accommodation_class = models.ForeignKey(AccommodationClass, models.DO_NOTHING, blank=True, null=True)
    fixed_asset = models.ForeignKey('FixedAsset', models.DO_NOTHING, blank=True, null=True)
    accommodation_map_type = models.ForeignKey('AccommodationMapType', models.DO_NOTHING, blank=True, null=True)
    number_of_spaces = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accommodation_map'


class AccommodationMapType(models.Model):
    accommodation_map_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accommodation_map_type'


class AccommodationSpot(models.Model):
    accommodation_spot_id = models.CharField(primary_key=True, max_length=20)
    accommodation_class = models.ForeignKey(AccommodationClass, models.DO_NOTHING, blank=True, null=True)
    fixed_asset = models.ForeignKey('FixedAsset', models.DO_NOTHING, blank=True, null=True)
    number_of_spaces = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accommodation_spot'


class AcctgTrans(models.Model):
    acctg_trans_id = models.CharField(primary_key=True, max_length=20)
    acctg_trans_type = models.ForeignKey('AcctgTransType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    is_posted = models.CharField(max_length=1, blank=True, null=True)
    posted_date = models.DateTimeField(blank=True, null=True)
    scheduled_posting_date = models.DateTimeField(blank=True, null=True)
    gl_journal = models.ForeignKey('GlJournal', models.DO_NOTHING, blank=True, null=True)
    gl_fiscal_type = models.ForeignKey('GlFiscalType', models.DO_NOTHING, blank=True, null=True)
    voucher_ref = models.CharField(max_length=60, blank=True, null=True)
    voucher_date = models.DateTimeField(blank=True, null=True)
    group_status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    fixed_asset = models.ForeignKey('FixedAsset', models.DO_NOTHING, blank=True, null=True)
    inventory_item = models.ForeignKey('InventoryItemVariance', models.DO_NOTHING, blank=True, null=True)
    physical_inventory = models.ForeignKey('PhysicalInventory', models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey('Invoice', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('Payment', models.DO_NOTHING, blank=True, null=True)
    fin_account_trans = models.ForeignKey('FinAccountTrans', models.DO_NOTHING, blank=True, null=True)
    shipment = models.ForeignKey('Shipment', models.DO_NOTHING, blank=True, null=True)
    receipt = models.ForeignKey('ShipmentReceipt', models.DO_NOTHING, blank=True, null=True)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    their_acctg_trans_id = models.CharField(max_length=60, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acctg_trans'


class AcctgTransAttribute(models.Model):
    acctg_trans = models.OneToOneField(AcctgTrans, models.DO_NOTHING, primary_key=True)  # The composite primary key (acctg_trans_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acctg_trans_attribute'
        unique_together = (('acctg_trans', 'attr_name'),)


class AcctgTransEntry(models.Model):
    acctg_trans = models.OneToOneField(AcctgTrans, models.DO_NOTHING, primary_key=True)  # The composite primary key (acctg_trans_id, acctg_trans_entry_seq_id) found, that is not supported. The first column is selected.
    acctg_trans_entry_seq_id = models.CharField(max_length=20)
    acctg_trans_entry_type = models.ForeignKey('AcctgTransEntryType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    voucher_ref = models.CharField(max_length=60, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING, blank=True, null=True)
    their_party_id = models.CharField(max_length=20, blank=True, null=True)
    product_id = models.CharField(max_length=20, blank=True, null=True)
    their_product_id = models.CharField(max_length=20, blank=True, null=True)
    inventory_item = models.ForeignKey('InventoryItem', models.DO_NOTHING, blank=True, null=True)
    gl_account_type = models.ForeignKey('GlAccountType', models.DO_NOTHING, blank=True, null=True)
    gl_account = models.ForeignKey('GlAccount', models.DO_NOTHING, blank=True, null=True)
    organization_party_id = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    orig_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    orig_currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='acctgtransentry_orig_currency_uom_set', blank=True, null=True)
    debit_credit_flag = models.CharField(max_length=1, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    group_id = models.CharField(max_length=20, blank=True, null=True)
    tax_id = models.CharField(max_length=20, blank=True, null=True)
    reconcile_status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    settlement_term = models.ForeignKey('SettlementTerm', models.DO_NOTHING, blank=True, null=True)
    is_summary = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acctg_trans_entry'
        unique_together = (('acctg_trans', 'acctg_trans_entry_seq_id'),)


class AcctgTransEntryType(models.Model):
    acctg_trans_entry_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acctg_trans_entry_type'


class AcctgTransType(models.Model):
    acctg_trans_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acctg_trans_type'


class AcctgTransTypeAttr(models.Model):
    acctg_trans_type = models.OneToOneField(AcctgTransType, models.DO_NOTHING, primary_key=True)  # The composite primary key (acctg_trans_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acctg_trans_type_attr'
        unique_together = (('acctg_trans_type', 'attr_name'),)


class Addendum(models.Model):
    addendum_id = models.CharField(primary_key=True, max_length=20)
    agreement = models.ForeignKey('AgreementItem', models.DO_NOTHING, blank=True, null=True)
    agreement_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    addendum_creation_date = models.DateTimeField(blank=True, null=True)
    addendum_effective_date = models.DateTimeField(blank=True, null=True)
    addendum_text = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addendum'


class AddressMatchMap(models.Model):
    map_key = models.CharField(primary_key=True, max_length=255)  # The composite primary key (map_key, map_value) found, that is not supported. The first column is selected.
    map_value = models.CharField(max_length=255)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_match_map'
        unique_together = (('map_key', 'map_value'),)


class Affiliate(models.Model):
    party = models.OneToOneField('PartyGroup', models.DO_NOTHING, primary_key=True)
    affiliate_name = models.CharField(max_length=100, blank=True, null=True)
    affiliate_description = models.CharField(max_length=255, blank=True, null=True)
    year_established = models.CharField(max_length=10, blank=True, null=True)
    site_type = models.CharField(max_length=255, blank=True, null=True)
    site_page_views = models.CharField(max_length=255, blank=True, null=True)
    site_visitors = models.CharField(max_length=255, blank=True, null=True)
    date_time_created = models.DateTimeField(blank=True, null=True)
    date_time_approved = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'affiliate'


class Agreement(models.Model):
    agreement_id = models.CharField(primary_key=True, max_length=20)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    party_id_from = models.ForeignKey('PartyRole', models.DO_NOTHING, db_column='party_id_from', blank=True, null=True)
    party_id_to = models.ForeignKey('PartyRole', models.DO_NOTHING, db_column='party_id_to', related_name='agreement_party_id_to_set', blank=True, null=True)
    role_type_id_from = models.CharField(max_length=20, blank=True, null=True)
    role_type_id_to = models.CharField(max_length=20, blank=True, null=True)
    agreement_type = models.ForeignKey('AgreementType', models.DO_NOTHING, blank=True, null=True)
    agreement_date = models.DateTimeField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    text_data = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement'


class AgreementAttribute(models.Model):
    agreement = models.OneToOneField(Agreement, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_attribute'
        unique_together = (('agreement', 'attr_name'),)


class AgreementContent(models.Model):
    agreement = models.ForeignKey(Agreement, models.DO_NOTHING)
    agreement_item_seq_id = models.CharField(max_length=20)
    agreement_content_type = models.ForeignKey('AgreementContentType', models.DO_NOTHING)
    content = models.OneToOneField('Content', models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, agreement_id, agreement_item_seq_id, agreement_content_type_id, from_date) found, that is not supported. The first column is selected.
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_content'
        unique_together = (('content', 'agreement', 'agreement_item_seq_id', 'agreement_content_type', 'from_date'),)


class AgreementContentType(models.Model):
    agreement_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_content_type'


class AgreementEmploymentAppl(models.Model):
    agreement = models.OneToOneField('AgreementItem', models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, party_id_to, party_id_from, role_type_id_to, role_type_id_from, from_date) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    party_id_from = models.CharField(max_length=20)
    party_id_to = models.CharField(max_length=20)
    role_type_id_from = models.ForeignKey('Employment', models.DO_NOTHING, db_column='role_type_id_from')
    role_type_id_to = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    agreement_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_employment_appl'
        unique_together = (('agreement', 'agreement_item_seq_id', 'party_id_to', 'party_id_from', 'role_type_id_to', 'role_type_id_from', 'from_date'),)


class AgreementFacilityAppl(models.Model):
    agreement = models.OneToOneField('AgreementItem', models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, facility_id) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    facility = models.ForeignKey('Facility', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_facility_appl'
        unique_together = (('agreement', 'agreement_item_seq_id', 'facility'),)


class AgreementGeographicalApplic(models.Model):
    agreement = models.OneToOneField('AgreementItem', models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, geo_id) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    geo = models.ForeignKey('Geo', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_geographical_applic'
        unique_together = (('agreement', 'agreement_item_seq_id', 'geo'),)


class AgreementItem(models.Model):
    agreement = models.OneToOneField(Agreement, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    agreement_item_type = models.ForeignKey('AgreementItemType', models.DO_NOTHING, blank=True, null=True)
    currency_uom_id = models.CharField(max_length=20, blank=True, null=True)
    agreement_text = models.TextField(blank=True, null=True)
    agreement_image = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_item'
        unique_together = (('agreement', 'agreement_item_seq_id'),)


class AgreementItemAttribute(models.Model):
    agreement = models.OneToOneField(AgreementItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, attr_name) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_item_attribute'
        unique_together = (('agreement', 'agreement_item_seq_id', 'attr_name'),)


class AgreementItemType(models.Model):
    agreement_item_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_item_type'


class AgreementItemTypeAttr(models.Model):
    agreement_item_type = models.OneToOneField(AgreementItemType, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_item_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_item_type_attr'
        unique_together = (('agreement_item_type', 'attr_name'),)


class AgreementPartyApplic(models.Model):
    agreement = models.OneToOneField(Agreement, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, party_id) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    party = models.ForeignKey('Party', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_party_applic'
        unique_together = (('agreement', 'agreement_item_seq_id', 'party'),)


class AgreementProductAppl(models.Model):
    agreement = models.OneToOneField(AgreementItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, product_id) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_product_appl'
        unique_together = (('agreement', 'agreement_item_seq_id', 'product'),)


class AgreementPromoAppl(models.Model):
    agreement = models.OneToOneField(AgreementItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, product_promo_id, from_date) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    product_promo = models.ForeignKey('ProductPromo', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_promo_appl'
        unique_together = (('agreement', 'agreement_item_seq_id', 'product_promo', 'from_date'),)


class AgreementRole(models.Model):
    agreement = models.OneToOneField(Agreement, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_role'
        unique_together = (('agreement', 'party', 'role_type_id'),)


class AgreementTerm(models.Model):
    agreement_term_id = models.CharField(primary_key=True, max_length=20)
    term_type = models.ForeignKey('TermType', models.DO_NOTHING, blank=True, null=True)
    agreement = models.ForeignKey(AgreementItem, models.DO_NOTHING, blank=True, null=True)
    agreement_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    invoice_item_type = models.ForeignKey('InvoiceItemType', models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    term_value = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    term_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    text_value = models.CharField(max_length=255, blank=True, null=True)
    min_quantity = models.FloatField(blank=True, null=True)
    max_quantity = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_term'


class AgreementTermAttribute(models.Model):
    agreement_term = models.OneToOneField(AgreementTerm, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_term_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_term_attribute'
        unique_together = (('agreement_term', 'attr_name'),)


class AgreementType(models.Model):
    agreement_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_type'


class AgreementTypeAttr(models.Model):
    agreement_type = models.OneToOneField(AgreementType, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_type_attr'
        unique_together = (('agreement_type', 'attr_name'),)


class AgreementWorkEffortApplic(models.Model):
    agreement = models.OneToOneField(Agreement, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, work_effort_id) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_work_effort_applic'
        unique_together = (('agreement', 'agreement_item_seq_id', 'work_effort'),)


class AgreementWorkeffortAppl(models.Model):
    agreement = models.OneToOneField(AgreementItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (agreement_id, agreement_item_seq_id, work_effort_id) found, that is not supported. The first column is selected.
    agreement_item_seq_id = models.CharField(max_length=20)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreement_workeffort_appl'
        unique_together = (('agreement', 'agreement_item_seq_id', 'work_effort'),)


class ApplicationSandbox(models.Model):
    application_id = models.CharField(primary_key=True, max_length=20)
    work_effort = models.ForeignKey('WorkEffortPartyAssignment', models.DO_NOTHING, blank=True, null=True)
    party_id = models.CharField(max_length=20, blank=True, null=True)
    role_type_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    runtime_data = models.ForeignKey('RuntimeData', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_sandbox'


class AudioDataResource(models.Model):
    data_resource = models.OneToOneField('DataResource', models.DO_NOTHING, primary_key=True)
    audio_data = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audio_data_resource'


class BenefitType(models.Model):
    benefit_type_id = models.CharField(primary_key=True, max_length=20)
    benefit_name = models.CharField(max_length=100, blank=True, null=True)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    employer_paid_percentage = models.FloatField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'benefit_type'


class BillingAccount(models.Model):
    billing_account_id = models.CharField(primary_key=True, max_length=20)
    account_limit = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    account_currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    contact_mech = models.ForeignKey('PostalAddress', models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    external_account_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_account'


class BillingAccountRole(models.Model):
    billing_account = models.OneToOneField(BillingAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (billing_account_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_account_role'
        unique_together = (('billing_account', 'party', 'role_type_id', 'from_date'),)


class BillingAccountTerm(models.Model):
    billing_account_term_id = models.CharField(primary_key=True, max_length=20)
    billing_account = models.ForeignKey(BillingAccount, models.DO_NOTHING, blank=True, null=True)
    term_type = models.ForeignKey('TermType', models.DO_NOTHING, blank=True, null=True)
    term_value = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    term_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_account_term'


class BillingAccountTermAttr(models.Model):
    billing_account_term = models.OneToOneField(BillingAccountTerm, models.DO_NOTHING, primary_key=True)  # The composite primary key (billing_account_term_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_account_term_attr'
        unique_together = (('billing_account_term', 'attr_name'),)


class BrowserType(models.Model):
    browser_type_id = models.CharField(primary_key=True, max_length=20)
    browser_name = models.CharField(max_length=100, blank=True, null=True)
    browser_version = models.CharField(max_length=10, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'browser_type'


class Budget(models.Model):
    budget_id = models.CharField(primary_key=True, max_length=20)
    budget_type = models.ForeignKey('BudgetType', models.DO_NOTHING, blank=True, null=True)
    custom_time_period = models.ForeignKey('CustomTimePeriod', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget'


class BudgetAttribute(models.Model):
    budget = models.OneToOneField(Budget, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_attribute'
        unique_together = (('budget', 'attr_name'),)


class BudgetItem(models.Model):
    budget = models.OneToOneField(Budget, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, budget_item_seq_id) found, that is not supported. The first column is selected.
    budget_item_seq_id = models.CharField(max_length=20)
    budget_item_type = models.ForeignKey('BudgetItemType', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    justification = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_item'
        unique_together = (('budget', 'budget_item_seq_id'),)


class BudgetItemAttribute(models.Model):
    budget = models.OneToOneField(BudgetItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, budget_item_seq_id, attr_name) found, that is not supported. The first column is selected.
    budget_item_seq_id = models.CharField(max_length=20)
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_item_attribute'
        unique_together = (('budget', 'budget_item_seq_id', 'attr_name'),)


class BudgetItemType(models.Model):
    budget_item_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_item_type'


class BudgetItemTypeAttr(models.Model):
    budget_item_type = models.OneToOneField(BudgetItemType, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_item_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_item_type_attr'
        unique_together = (('budget_item_type', 'attr_name'),)


class BudgetReview(models.Model):
    budget = models.OneToOneField(Budget, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, budget_review_id, party_id, budget_review_result_type_id) found, that is not supported. The first column is selected.
    budget_review_id = models.CharField(max_length=20)
    party = models.ForeignKey('Party', models.DO_NOTHING)
    budget_review_result_type = models.ForeignKey('BudgetReviewResultType', models.DO_NOTHING)
    review_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_review'
        unique_together = (('budget', 'budget_review_id', 'party', 'budget_review_result_type'),)


class BudgetReviewResultType(models.Model):
    budget_review_result_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_review_result_type'


class BudgetRevision(models.Model):
    budget = models.OneToOneField(Budget, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, revision_seq_id) found, that is not supported. The first column is selected.
    revision_seq_id = models.CharField(max_length=20)
    date_revised = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_revision'
        unique_together = (('budget', 'revision_seq_id'),)


class BudgetRevisionImpact(models.Model):
    budget = models.OneToOneField(BudgetRevision, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, budget_item_seq_id, revision_seq_id) found, that is not supported. The first column is selected.
    budget_item_seq_id = models.CharField(max_length=20)
    revision_seq_id = models.CharField(max_length=20)
    revised_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    add_delete_flag = models.CharField(max_length=1, blank=True, null=True)
    revision_reason = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_revision_impact'
        unique_together = (('budget', 'budget_item_seq_id', 'revision_seq_id'),)


class BudgetRole(models.Model):
    budget = models.OneToOneField(Budget, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_role'
        unique_together = (('budget', 'party', 'role_type_id'),)


class BudgetScenario(models.Model):
    budget_scenario_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_scenario'


class BudgetScenarioApplication(models.Model):
    budget_scenario_applic_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (budget_scenario_applic_id, budget_scenario_id) found, that is not supported. The first column is selected.
    budget_scenario = models.ForeignKey(BudgetScenario, models.DO_NOTHING)
    budget = models.ForeignKey(BudgetItem, models.DO_NOTHING, blank=True, null=True)
    budget_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    amount_change = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    percentage_change = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_scenario_application'
        unique_together = (('budget_scenario_applic_id', 'budget_scenario'),)


class BudgetScenarioRule(models.Model):
    budget_scenario = models.OneToOneField(BudgetScenario, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_scenario_id, budget_item_type_id) found, that is not supported. The first column is selected.
    budget_item_type = models.ForeignKey(BudgetItemType, models.DO_NOTHING)
    amount_change = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    percentage_change = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_scenario_rule'
        unique_together = (('budget_scenario', 'budget_item_type'),)


class BudgetStatus(models.Model):
    budget = models.OneToOneField(Budget, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, status_id) found, that is not supported. The first column is selected.
    status = models.ForeignKey('StatusItem', models.DO_NOTHING)
    status_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_status'
        unique_together = (('budget', 'status'),)


class BudgetType(models.Model):
    budget_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_type'


class BudgetTypeAttr(models.Model):
    budget_type = models.OneToOneField(BudgetType, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_type_attr'
        unique_together = (('budget_type', 'attr_name'),)


class CarrierShipmentBoxType(models.Model):
    shipment_box_type = models.OneToOneField('ShipmentBoxType', models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_box_type_id, party_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    packaging_type_code = models.CharField(max_length=20, blank=True, null=True)
    oversize_code = models.CharField(max_length=10, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrier_shipment_box_type'
        unique_together = (('shipment_box_type', 'party'),)


class CarrierShipmentMethod(models.Model):
    shipment_method_type = models.OneToOneField('ShipmentMethodType', models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_method_type_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    sequence_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    carrier_service_code = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrier_shipment_method'
        unique_together = (('shipment_method_type', 'party', 'role_type_id'),)


class CartAbandonedLine(models.Model):
    visit_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (visit_id, cart_abandoned_line_seq_id) found, that is not supported. The first column is selected.
    cart_abandoned_line_seq_id = models.CharField(max_length=20)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    prod_catalog = models.ForeignKey('ProdCatalog', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_start = models.DateTimeField(blank=True, null=True)
    reserv_length = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_persons = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    reserv2nd_p_p_perc = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_nth_p_p_perc = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    config_id = models.CharField(max_length=20, blank=True, null=True)
    total_with_adjustments = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    was_reserved = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart_abandoned_line'
        unique_together = (('visit_id', 'cart_abandoned_line_seq_id'),)


class CatalinaSession(models.Model):
    session_id = models.CharField(primary_key=True, max_length=60)
    session_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    session_info = models.BinaryField(blank=True, null=True)
    is_valid = models.CharField(max_length=1, blank=True, null=True)
    max_idle = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_accessed = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalina_session'


class CharacterSet(models.Model):
    character_set_id = models.CharField(primary_key=True, max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_set'


class CheckAccount(models.Model):
    payment_method = models.OneToOneField('PaymentMethod', models.DO_NOTHING, primary_key=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    routing_number = models.CharField(max_length=60, blank=True, null=True)
    account_type = models.CharField(max_length=60, blank=True, null=True)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    name_on_account = models.CharField(max_length=100, blank=True, null=True)
    company_name_on_account = models.CharField(max_length=100, blank=True, null=True)
    contact_mech = models.ForeignKey('PostalAddress', models.DO_NOTHING, blank=True, null=True)
    branch_code = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'check_account'


class CommContentAssocType(models.Model):
    comm_content_assoc_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_content_assoc_type'


class CommEventContentAssoc(models.Model):
    content = models.OneToOneField('Content', models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, communication_event_id, from_date) found, that is not supported. The first column is selected.
    communication_event = models.ForeignKey('CommunicationEvent', models.DO_NOTHING)
    comm_content_assoc_type = models.ForeignKey(CommContentAssocType, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comm_event_content_assoc'
        unique_together = (('content', 'communication_event', 'from_date'),)


class CommunicationEvent(models.Model):
    communication_event_id = models.CharField(primary_key=True, max_length=20)
    communication_event_type = models.ForeignKey('CommunicationEventType', models.DO_NOTHING, blank=True, null=True)
    orig_comm_event_id = models.CharField(max_length=20, blank=True, null=True)
    parent_comm_event_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    contact_mech_type = models.ForeignKey('ContactMechType', models.DO_NOTHING, blank=True, null=True)
    contact_mech_id_from = models.ForeignKey('ContactMech', models.DO_NOTHING, db_column='contact_mech_id_from', blank=True, null=True)
    contact_mech_id_to = models.ForeignKey('ContactMech', models.DO_NOTHING, db_column='contact_mech_id_to', related_name='communicationevent_contact_mech_id_to_set', blank=True, null=True)
    role_type_id_from = models.ForeignKey('RoleType', models.DO_NOTHING, db_column='role_type_id_from', blank=True, null=True)
    role_type_id_to = models.ForeignKey('RoleType', models.DO_NOTHING, db_column='role_type_id_to', related_name='communicationevent_role_type_id_to_set', blank=True, null=True)
    party_id_from = models.ForeignKey('Party', models.DO_NOTHING, db_column='party_id_from', blank=True, null=True)
    party_id_to = models.ForeignKey('Party', models.DO_NOTHING, db_column='party_id_to', related_name='communicationevent_party_id_to_set', blank=True, null=True)
    entry_date = models.DateTimeField(blank=True, null=True)
    datetime_started = models.DateTimeField(blank=True, null=True)
    datetime_ended = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    content_mime_type = models.ForeignKey('MimeType', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    reason_enum = models.ForeignKey('Enumeration', models.DO_NOTHING, blank=True, null=True)
    contact_list = models.ForeignKey('ContactList', models.DO_NOTHING, blank=True, null=True)
    header_string = models.TextField(blank=True, null=True)
    from_string = models.TextField(blank=True, null=True)
    to_string = models.TextField(blank=True, null=True)
    cc_string = models.TextField(blank=True, null=True)
    bcc_string = models.TextField(blank=True, null=True)
    message_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_event'


class CommunicationEventOrder(models.Model):
    order = models.OneToOneField('OrderHeader', models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, communication_event_id) found, that is not supported. The first column is selected.
    communication_event = models.ForeignKey(CommunicationEvent, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_event_order'
        unique_together = (('order', 'communication_event'),)


class CommunicationEventProduct(models.Model):
    product = models.OneToOneField('Product', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, communication_event_id) found, that is not supported. The first column is selected.
    communication_event = models.ForeignKey(CommunicationEvent, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_event_product'
        unique_together = (('product', 'communication_event'),)


class CommunicationEventPrpTyp(models.Model):
    communication_event_prp_typ_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_event_prp_typ'


class CommunicationEventPurpose(models.Model):
    communication_event_prp_typ = models.OneToOneField(CommunicationEventPrpTyp, models.DO_NOTHING, primary_key=True)  # The composite primary key (communication_event_prp_typ_id, communication_event_id) found, that is not supported. The first column is selected.
    communication_event = models.ForeignKey(CommunicationEvent, models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_event_purpose'
        unique_together = (('communication_event_prp_typ', 'communication_event'),)


class CommunicationEventRole(models.Model):
    communication_event = models.OneToOneField(CommunicationEvent, models.DO_NOTHING, primary_key=True)  # The composite primary key (communication_event_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    contact_mech = models.ForeignKey('ContactMech', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_event_role'
        unique_together = (('communication_event', 'party', 'role_type_id'),)


class CommunicationEventType(models.Model):
    communication_event_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    contact_mech_type = models.ForeignKey('ContactMechType', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_event_type'


class CommunicationEventWorkEff(models.Model):
    work_effort = models.OneToOneField('WorkEffort', models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, communication_event_id) found, that is not supported. The first column is selected.
    communication_event = models.ForeignKey(CommunicationEvent, models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_event_work_eff'
        unique_together = (('work_effort', 'communication_event'),)


class ConfigOptionProductOption(models.Model):
    config = models.OneToOneField('ProductConfigConfig', models.DO_NOTHING, primary_key=True)  # The composite primary key (config_id, config_item_id, config_option_id, sequence_num, product_id) found, that is not supported. The first column is selected.
    config_item = models.ForeignKey('ProductConfigProduct', models.DO_NOTHING)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0)
    config_option_id = models.CharField(max_length=20)
    product_id = models.CharField(max_length=20)
    product_option_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_option_product_option'
        unique_together = (('config', 'config_item', 'config_option_id', 'sequence_num', 'product_id'),)


class ContactList(models.Model):
    contact_list_id = models.CharField(primary_key=True, max_length=20)
    contact_list_type = models.ForeignKey('ContactListType', models.DO_NOTHING, blank=True, null=True)
    contact_mech_type = models.ForeignKey('ContactMechType', models.DO_NOTHING, blank=True, null=True)
    marketing_campaign = models.ForeignKey('MarketingCampaign', models.DO_NOTHING, blank=True, null=True)
    contact_list_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.CharField(max_length=1, blank=True, null=True)
    single_use = models.CharField(max_length=1, blank=True, null=True)
    owner_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    verify_email_from = models.CharField(max_length=255, blank=True, null=True)
    verify_email_screen = models.CharField(max_length=255, blank=True, null=True)
    verify_email_subject = models.CharField(max_length=255, blank=True, null=True)
    verify_email_web_site_id = models.CharField(max_length=20, blank=True, null=True)
    opt_out_screen = models.CharField(max_length=255, blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='contactlist_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_list'


class ContactListCommStatus(models.Model):
    contact_list = models.OneToOneField(ContactList, models.DO_NOTHING, primary_key=True)  # The composite primary key (contact_list_id, communication_event_id, contact_mech_id) found, that is not supported. The first column is selected.
    communication_event = models.ForeignKey(CommunicationEvent, models.DO_NOTHING)
    contact_mech = models.ForeignKey('ContactMech', models.DO_NOTHING)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    message_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_list_comm_status'
        unique_together = (('contact_list', 'communication_event', 'contact_mech'),)


class ContactListParty(models.Model):
    contact_list = models.OneToOneField(ContactList, models.DO_NOTHING, primary_key=True)  # The composite primary key (contact_list_id, party_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    preferred_contact_mech = models.ForeignKey('ContactMech', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_list_party'
        unique_together = (('contact_list', 'party', 'from_date'),)


class ContactListPartyStatus(models.Model):
    contact_list = models.OneToOneField(ContactListParty, models.DO_NOTHING, primary_key=True)  # The composite primary key (contact_list_id, party_id, from_date, status_date) found, that is not supported. The first column is selected.
    party_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    status_date = models.DateTimeField()
    status_id = models.CharField(max_length=20, blank=True, null=True)
    set_by_user_login_id = models.CharField(max_length=255, blank=True, null=True)
    opt_in_verify_code = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_list_party_status'
        unique_together = (('contact_list', 'party_id', 'from_date', 'status_date'),)


class ContactListType(models.Model):
    contact_list_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_list_type'


class ContactMech(models.Model):
    contact_mech_id = models.CharField(primary_key=True, max_length=20)
    contact_mech_type = models.ForeignKey('ContactMechType', models.DO_NOTHING, blank=True, null=True)
    info_string = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_mech'


class ContactMechAttribute(models.Model):
    contact_mech = models.OneToOneField(ContactMech, models.DO_NOTHING, primary_key=True)  # The composite primary key (contact_mech_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_mech_attribute'
        unique_together = (('contact_mech', 'attr_name'),)


class ContactMechLink(models.Model):
    contact_mech_id_from = models.OneToOneField(ContactMech, models.DO_NOTHING, db_column='contact_mech_id_from', primary_key=True)  # The composite primary key (contact_mech_id_from, contact_mech_id_to) found, that is not supported. The first column is selected.
    contact_mech_id_to = models.ForeignKey(ContactMech, models.DO_NOTHING, db_column='contact_mech_id_to', related_name='contactmechlink_contact_mech_id_to_set')
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_mech_link'
        unique_together = (('contact_mech_id_from', 'contact_mech_id_to'),)


class ContactMechPurposeType(models.Model):
    contact_mech_purpose_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_mech_purpose_type'


class ContactMechType(models.Model):
    contact_mech_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_mech_type'


class ContactMechTypeAttr(models.Model):
    contact_mech_type = models.OneToOneField(ContactMechType, models.DO_NOTHING, primary_key=True)  # The composite primary key (contact_mech_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_mech_type_attr'
        unique_together = (('contact_mech_type', 'attr_name'),)


class ContactMechTypePurpose(models.Model):
    contact_mech_type = models.OneToOneField(ContactMechType, models.DO_NOTHING, primary_key=True)  # The composite primary key (contact_mech_type_id, contact_mech_purpose_type_id) found, that is not supported. The first column is selected.
    contact_mech_purpose_type = models.ForeignKey(ContactMechPurposeType, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_mech_type_purpose'
        unique_together = (('contact_mech_type', 'contact_mech_purpose_type'),)


class Container(models.Model):
    container_id = models.CharField(primary_key=True, max_length=20)
    container_type = models.ForeignKey('ContainerType', models.DO_NOTHING, blank=True, null=True)
    facility = models.ForeignKey('Facility', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'container'


class ContainerGeoPoint(models.Model):
    container = models.OneToOneField(Container, models.DO_NOTHING, primary_key=True)  # The composite primary key (container_id, geo_point_id, from_date) found, that is not supported. The first column is selected.
    geo_point = models.ForeignKey('GeoPoint', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'container_geo_point'
        unique_together = (('container', 'geo_point', 'from_date'),)


class ContainerType(models.Model):
    container_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'container_type'


class Content(models.Model):
    content_id = models.CharField(primary_key=True, max_length=20)
    content_type = models.ForeignKey('ContentType', models.DO_NOTHING, blank=True, null=True)
    owner_content = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    decorator_content = models.ForeignKey('self', models.DO_NOTHING, related_name='content_decorator_content_set', blank=True, null=True)
    instance_of_content = models.ForeignKey('self', models.DO_NOTHING, related_name='content_instance_of_content_set', blank=True, null=True)
    data_resource = models.ForeignKey('DataResource', models.DO_NOTHING, blank=True, null=True)
    template_data_resource = models.ForeignKey('DataResource', models.DO_NOTHING, related_name='content_template_data_resource_set', blank=True, null=True)
    data_source = models.ForeignKey('DataSource', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    privilege_enum = models.ForeignKey('Enumeration', models.DO_NOTHING, blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    custom_method = models.ForeignKey('CustomMethod', models.DO_NOTHING, blank=True, null=True)
    content_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    locale_string = models.CharField(max_length=10, blank=True, null=True)
    mime_type_id = models.CharField(max_length=255, blank=True, null=True)
    character_set = models.ForeignKey(CharacterSet, models.DO_NOTHING, blank=True, null=True)
    child_leaf_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    child_branch_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='content_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content'


class ContentApproval(models.Model):
    content_approval_id = models.CharField(primary_key=True, max_length=20)
    content = models.ForeignKey(Content, models.DO_NOTHING, blank=True, null=True)
    content_revision_seq_id = models.CharField(max_length=20, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING, blank=True, null=True)
    approval_status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_approval'


class ContentAssoc(models.Model):
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, content_id_to, content_assoc_type_id, from_date) found, that is not supported. The first column is selected.
    content_id_to = models.ForeignKey(Content, models.DO_NOTHING, db_column='content_id_to', related_name='contentassoc_content_id_to_set')
    content_assoc_type = models.ForeignKey('ContentAssocType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    content_assoc_predicate = models.ForeignKey('ContentAssocPredicate', models.DO_NOTHING, blank=True, null=True)
    data_source = models.ForeignKey('DataSource', models.DO_NOTHING, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    map_key = models.CharField(max_length=100, blank=True, null=True)
    upper_coordinate = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    left_coordinate = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='contentassoc_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_assoc'
        unique_together = (('content', 'content_id_to', 'content_assoc_type', 'from_date'),)


class ContentAssocPredicate(models.Model):
    content_assoc_predicate_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_assoc_predicate'


class ContentAssocType(models.Model):
    content_assoc_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_assoc_type'


class ContentAttribute(models.Model):
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_attribute'
        unique_together = (('content', 'attr_name'),)


class ContentKeyword(models.Model):
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, keyword) found, that is not supported. The first column is selected.
    keyword = models.CharField(max_length=60)
    relevancy_weight = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_keyword'
        unique_together = (('content', 'keyword'),)


class ContentMetaData(models.Model):
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, meta_data_predicate_id) found, that is not supported. The first column is selected.
    meta_data_predicate = models.ForeignKey('MetaDataPredicate', models.DO_NOTHING)
    meta_data_value = models.CharField(max_length=255, blank=True, null=True)
    data_source = models.ForeignKey('DataSource', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_meta_data'
        unique_together = (('content', 'meta_data_predicate'),)


class ContentOperation(models.Model):
    content_operation_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_operation'


class ContentPurpose(models.Model):
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, content_purpose_type_id) found, that is not supported. The first column is selected.
    content_purpose_type = models.ForeignKey('ContentPurposeType', models.DO_NOTHING)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_purpose'
        unique_together = (('content', 'content_purpose_type'),)


class ContentPurposeOperation(models.Model):
    content_purpose_type = models.OneToOneField('ContentPurposeType', models.DO_NOTHING, primary_key=True)  # The composite primary key (content_purpose_type_id, content_operation_id, role_type_id, status_id, privilege_enum_id) found, that is not supported. The first column is selected.
    content_operation = models.ForeignKey(ContentOperation, models.DO_NOTHING)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING)
    privilege_enum = models.ForeignKey('Enumeration', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_purpose_operation'
        unique_together = (('content_purpose_type', 'content_operation', 'role_type', 'status', 'privilege_enum'),)


class ContentPurposeType(models.Model):
    content_purpose_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_purpose_type'


class ContentRevision(models.Model):
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, content_revision_seq_id) found, that is not supported. The first column is selected.
    content_revision_seq_id = models.CharField(max_length=20)
    committed_by_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_revision'
        unique_together = (('content', 'content_revision_seq_id'),)


class ContentRevisionItem(models.Model):
    content = models.OneToOneField(ContentRevision, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, content_revision_seq_id, item_content_id) found, that is not supported. The first column is selected.
    content_revision_seq_id = models.CharField(max_length=20)
    item_content_id = models.CharField(max_length=20)
    old_data_resource = models.ForeignKey('DataResource', models.DO_NOTHING, blank=True, null=True)
    new_data_resource = models.ForeignKey('DataResource', models.DO_NOTHING, related_name='contentrevisionitem_new_data_resource_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_revision_item'
        unique_together = (('content', 'content_revision_seq_id', 'item_content_id'),)


class ContentRole(models.Model):
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_role'
        unique_together = (('content', 'party', 'role_type_id', 'from_date'),)


class ContentSearchConstraint(models.Model):
    content_search_result = models.OneToOneField('ContentSearchResult', models.DO_NOTHING, primary_key=True)  # The composite primary key (content_search_result_id, constraint_seq_id) found, that is not supported. The first column is selected.
    constraint_seq_id = models.CharField(max_length=20)
    constraint_name = models.CharField(max_length=255, blank=True, null=True)
    info_string = models.CharField(max_length=255, blank=True, null=True)
    include_sub_categories = models.CharField(max_length=1, blank=True, null=True)
    is_and = models.CharField(max_length=1, blank=True, null=True)
    any_prefix = models.CharField(max_length=1, blank=True, null=True)
    any_suffix = models.CharField(max_length=1, blank=True, null=True)
    remove_stems = models.CharField(max_length=1, blank=True, null=True)
    low_value = models.CharField(max_length=60, blank=True, null=True)
    high_value = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_search_constraint'
        unique_together = (('content_search_result', 'constraint_seq_id'),)


class ContentSearchResult(models.Model):
    content_search_result_id = models.CharField(primary_key=True, max_length=20)
    visit_id = models.CharField(max_length=20, blank=True, null=True)
    order_by_name = models.CharField(max_length=255, blank=True, null=True)
    is_ascending = models.CharField(max_length=1, blank=True, null=True)
    num_results = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    seconds_total = models.FloatField(blank=True, null=True)
    search_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_search_result'


class ContentType(models.Model):
    content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_type'


class ContentTypeAttr(models.Model):
    content_type = models.OneToOneField(ContentType, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_type_attr'
        unique_together = (('content_type', 'attr_name'),)


class CostComponent(models.Model):
    cost_component_id = models.CharField(primary_key=True, max_length=20)
    cost_component_type = models.ForeignKey('CostComponentType', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    product_feature = models.ForeignKey('ProductFeature', models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    geo = models.ForeignKey('Geo', models.DO_NOTHING, blank=True, null=True)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    fixed_asset = models.ForeignKey('FixedAsset', models.DO_NOTHING, blank=True, null=True)
    cost_component_calc = models.ForeignKey('CostComponentCalc', models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    cost = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cost_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_component'


class CostComponentAttribute(models.Model):
    cost_component = models.OneToOneField(CostComponent, models.DO_NOTHING, primary_key=True)  # The composite primary key (cost_component_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_component_attribute'
        unique_together = (('cost_component', 'attr_name'),)


class CostComponentCalc(models.Model):
    cost_component_calc_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    cost_gl_account_type = models.ForeignKey('GlAccountType', models.DO_NOTHING, blank=True, null=True)
    offsetting_gl_account_type = models.ForeignKey('GlAccountType', models.DO_NOTHING, related_name='costcomponentcalc_offsetting_gl_account_type_set', blank=True, null=True)
    fixed_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    variable_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    per_milli_second = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    cost_custom_method = models.ForeignKey('CustomMethod', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_component_calc'


class CostComponentType(models.Model):
    cost_component_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_component_type'


class CostComponentTypeAttr(models.Model):
    cost_component_type = models.OneToOneField(CostComponentType, models.DO_NOTHING, primary_key=True)  # The composite primary key (cost_component_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_component_type_attr'
        unique_together = (('cost_component_type', 'attr_name'),)


class CountryAddressFormat(models.Model):
    geo = models.OneToOneField('Geo', models.DO_NOTHING, primary_key=True)
    geo_assoc_type = models.ForeignKey('GeoAssocType', models.DO_NOTHING, blank=True, null=True)
    require_state_province_id = models.CharField(max_length=20, blank=True, null=True)
    require_postal_code = models.CharField(max_length=1, blank=True, null=True)
    postal_code_regex = models.CharField(max_length=255, blank=True, null=True)
    has_postal_code_ext = models.CharField(max_length=1, blank=True, null=True)
    require_postal_code_ext = models.CharField(max_length=1, blank=True, null=True)
    address_format = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_address_format'


class CountryCapital(models.Model):
    country_code = models.OneToOneField('CountryCode', models.DO_NOTHING, db_column='country_code', primary_key=True)
    country_capital = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_capital'


class CountryCode(models.Model):
    country_code = models.CharField(primary_key=True, max_length=20)
    country_abbr = models.CharField(max_length=60, blank=True, null=True)
    country_number = models.CharField(max_length=60, blank=True, null=True)
    country_name = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_code'


class CountryTeleCode(models.Model):
    country_code = models.OneToOneField(CountryCode, models.DO_NOTHING, db_column='country_code', primary_key=True)
    tele_code = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_tele_code'


class CreditCard(models.Model):
    payment_method = models.OneToOneField('PaymentMethod', models.DO_NOTHING, primary_key=True)
    card_type = models.CharField(max_length=60, blank=True, null=True)
    card_number = models.CharField(max_length=255, blank=True, null=True)
    valid_from_date = models.CharField(max_length=7, blank=True, null=True)
    expire_date = models.CharField(max_length=7, blank=True, null=True)
    issue_number = models.CharField(max_length=7, blank=True, null=True)
    company_name_on_card = models.CharField(max_length=100, blank=True, null=True)
    title_on_card = models.CharField(max_length=100, blank=True, null=True)
    first_name_on_card = models.CharField(max_length=100, blank=True, null=True)
    middle_name_on_card = models.CharField(max_length=100, blank=True, null=True)
    last_name_on_card = models.CharField(max_length=100, blank=True, null=True)
    suffix_on_card = models.CharField(max_length=100, blank=True, null=True)
    contact_mech = models.ForeignKey('PostalAddress', models.DO_NOTHING, blank=True, null=True)
    consecutive_failed_auths = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_failed_auth_date = models.DateTimeField(blank=True, null=True)
    consecutive_failed_nsf = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_failed_nsf_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_card'


class CreditCardTypeGlAccount(models.Model):
    card_type = models.CharField(primary_key=True, max_length=60)  # The composite primary key (card_type, organization_party_id) found, that is not supported. The first column is selected.
    organization_party_id = models.CharField(max_length=20)
    gl_account_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_card_type_gl_account'
        unique_together = (('card_type', 'organization_party_id'),)


class CustRequest(models.Model):
    cust_request_id = models.CharField(primary_key=True, max_length=20)
    cust_request_type = models.ForeignKey('CustRequestType', models.DO_NOTHING, blank=True, null=True)
    cust_request_category = models.ForeignKey('CustRequestCategory', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    from_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    priority = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    cust_request_date = models.DateTimeField(blank=True, null=True)
    response_required_date = models.DateTimeField(blank=True, null=True)
    cust_request_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    maximum_amount_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    product_store = models.ForeignKey('ProductStore', models.DO_NOTHING, blank=True, null=True)
    sales_channel_enum = models.ForeignKey('Enumeration', models.DO_NOTHING, blank=True, null=True)
    fulfill_contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='custrequest_currency_uom_set', blank=True, null=True)
    open_date_time = models.DateTimeField(blank=True, null=True)
    closed_date_time = models.DateTimeField(blank=True, null=True)
    internal_comment = models.CharField(max_length=255, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    cust_estimated_milli_seconds = models.FloatField(blank=True, null=True)
    cust_sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    parent_cust_request = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    billed = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request'


class CustRequestAttribute(models.Model):
    cust_request = models.OneToOneField(CustRequest, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_attribute'
        unique_together = (('cust_request', 'attr_name'),)


class CustRequestCategory(models.Model):
    cust_request_category_id = models.CharField(primary_key=True, max_length=20)
    cust_request_type = models.ForeignKey('CustRequestType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_category'


class CustRequestCommEvent(models.Model):
    cust_request = models.OneToOneField(CustRequest, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, communication_event_id) found, that is not supported. The first column is selected.
    communication_event = models.ForeignKey(CommunicationEvent, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_comm_event'
        unique_together = (('cust_request', 'communication_event'),)


class CustRequestContent(models.Model):
    cust_request = models.OneToOneField(CustRequest, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, content_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_content'
        unique_together = (('cust_request', 'content', 'from_date'),)


class CustRequestItem(models.Model):
    cust_request = models.OneToOneField(CustRequest, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, cust_request_item_seq_id) found, that is not supported. The first column is selected.
    cust_request_item_seq_id = models.CharField(max_length=20)
    cust_request_resolution = models.ForeignKey('CustRequestResolution', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    priority = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    required_by_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    selected_amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    maximum_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    reserv_start = models.DateTimeField(blank=True, null=True)
    reserv_length = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_persons = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    config_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_item'
        unique_together = (('cust_request', 'cust_request_item_seq_id'),)


class CustRequestItemNote(models.Model):
    cust_request = models.OneToOneField(CustRequestItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, cust_request_item_seq_id, note_id) found, that is not supported. The first column is selected.
    cust_request_item_seq_id = models.CharField(max_length=20)
    note = models.ForeignKey('NoteData', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_item_note'
        unique_together = (('cust_request', 'cust_request_item_seq_id', 'note'),)


class CustRequestItemWorkEffort(models.Model):
    cust_request = models.OneToOneField(CustRequestItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, cust_request_item_seq_id, work_effort_id) found, that is not supported. The first column is selected.
    cust_request_item_seq_id = models.CharField(max_length=20)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_item_work_effort'
        unique_together = (('cust_request', 'cust_request_item_seq_id', 'work_effort'),)


class CustRequestNote(models.Model):
    cust_request = models.OneToOneField(CustRequest, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, note_id) found, that is not supported. The first column is selected.
    note = models.ForeignKey('NoteData', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_note'
        unique_together = (('cust_request', 'note'),)


class CustRequestParty(models.Model):
    cust_request = models.OneToOneField(CustRequest, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_party'
        unique_together = (('cust_request', 'party', 'role_type_id', 'from_date'),)


class CustRequestResolution(models.Model):
    cust_request_resolution_id = models.CharField(primary_key=True, max_length=20)
    cust_request_type = models.ForeignKey('CustRequestType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_resolution'


class CustRequestRole(models.Model):
    cust_request = models.OneToOneField(CustRequest, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_role'
        unique_together = (('cust_request', 'party', 'role_type_id'),)


class CustRequestStatus(models.Model):
    cust_request_status_id = models.CharField(primary_key=True, max_length=20)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    cust_request = models.ForeignKey(CustRequest, models.DO_NOTHING, blank=True, null=True)
    cust_request_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    status_date = models.DateTimeField(blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_status'


class CustRequestType(models.Model):
    cust_request_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_type'


class CustRequestTypeAttr(models.Model):
    cust_request_type = models.OneToOneField(CustRequestType, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_type_attr'
        unique_together = (('cust_request_type', 'attr_name'),)


class CustRequestWorkEffort(models.Model):
    cust_request = models.OneToOneField(CustRequest, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, work_effort_id) found, that is not supported. The first column is selected.
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cust_request_work_effort'
        unique_together = (('cust_request', 'work_effort'),)


class CustomMethod(models.Model):
    custom_method_id = models.CharField(primary_key=True, max_length=20)
    custom_method_type = models.ForeignKey('CustomMethodType', models.DO_NOTHING, blank=True, null=True)
    custom_method_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_method'


class CustomMethodType(models.Model):
    custom_method_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_method_type'


class CustomTimePeriod(models.Model):
    custom_time_period_id = models.CharField(primary_key=True, max_length=20)
    parent_period = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    period_type = models.ForeignKey('PeriodType', models.DO_NOTHING, blank=True, null=True)
    period_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    period_name = models.CharField(max_length=100, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    is_closed = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    organization_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_time_period'


class DataCategory(models.Model):
    data_category_id = models.CharField(primary_key=True, max_length=20)
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_category'


class DataResource(models.Model):
    data_resource_id = models.CharField(primary_key=True, max_length=20)
    data_resource_type = models.ForeignKey('DataResourceType', models.DO_NOTHING, blank=True, null=True)
    data_template_type = models.ForeignKey('DataTemplateType', models.DO_NOTHING, blank=True, null=True)
    data_category = models.ForeignKey(DataCategory, models.DO_NOTHING, blank=True, null=True)
    data_source = models.ForeignKey('DataSource', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    data_resource_name = models.CharField(max_length=255, blank=True, null=True)
    locale_string = models.CharField(max_length=10, blank=True, null=True)
    mime_type_id = models.CharField(max_length=255, blank=True, null=True)
    character_set = models.ForeignKey(CharacterSet, models.DO_NOTHING, blank=True, null=True)
    object_info = models.CharField(max_length=255, blank=True, null=True)
    survey = models.ForeignKey('Survey', models.DO_NOTHING, blank=True, null=True)
    survey_response = models.ForeignKey('SurveyResponse', models.DO_NOTHING, blank=True, null=True)
    related_detail_id = models.CharField(max_length=20, blank=True, null=True)
    is_public = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='dataresource_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_resource'


class DataResourceAttribute(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)  # The composite primary key (data_resource_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_resource_attribute'
        unique_together = (('data_resource', 'attr_name'),)


class DataResourceMetaData(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)  # The composite primary key (data_resource_id, meta_data_predicate_id) found, that is not supported. The first column is selected.
    meta_data_predicate = models.ForeignKey('MetaDataPredicate', models.DO_NOTHING)
    meta_data_value = models.CharField(max_length=255, blank=True, null=True)
    data_source = models.ForeignKey('DataSource', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_resource_meta_data'
        unique_together = (('data_resource', 'meta_data_predicate'),)


class DataResourcePurpose(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)  # The composite primary key (data_resource_id, content_purpose_type_id) found, that is not supported. The first column is selected.
    content_purpose_type = models.ForeignKey(ContentPurposeType, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_resource_purpose'
        unique_together = (('data_resource', 'content_purpose_type'),)


class DataResourceRole(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)  # The composite primary key (data_resource_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_resource_role'
        unique_together = (('data_resource', 'party', 'role_type_id', 'from_date'),)


class DataResourceType(models.Model):
    data_resource_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_resource_type'


class DataResourceTypeAttr(models.Model):
    data_resource_type = models.OneToOneField(DataResourceType, models.DO_NOTHING, primary_key=True)  # The composite primary key (data_resource_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_resource_type_attr'
        unique_together = (('data_resource_type', 'attr_name'),)


class DataSource(models.Model):
    data_source_id = models.CharField(primary_key=True, max_length=20)
    data_source_type = models.ForeignKey('DataSourceType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_source'


class DataSourceType(models.Model):
    data_source_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_source_type'


class DataTemplateType(models.Model):
    data_template_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    extension = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_template_type'


class Deduction(models.Model):
    deduction_id = models.CharField(primary_key=True, max_length=20)
    deduction_type = models.ForeignKey('DeductionType', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('Payment', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deduction'


class DeductionType(models.Model):
    deduction_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deduction_type'


class Deliverable(models.Model):
    deliverable_id = models.CharField(primary_key=True, max_length=20)
    deliverable_type = models.ForeignKey('DeliverableType', models.DO_NOTHING, blank=True, null=True)
    deliverable_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deliverable'


class DeliverableType(models.Model):
    deliverable_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deliverable_type'


class Delivery(models.Model):
    delivery_id = models.CharField(primary_key=True, max_length=20)
    origin_facility = models.ForeignKey('Facility', models.DO_NOTHING, blank=True, null=True)
    dest_facility = models.ForeignKey('Facility', models.DO_NOTHING, related_name='delivery_dest_facility_set', blank=True, null=True)
    actual_start_date = models.DateTimeField(blank=True, null=True)
    actual_arrival_date = models.DateTimeField(blank=True, null=True)
    estimated_start_date = models.DateTimeField(blank=True, null=True)
    estimated_arrival_date = models.DateTimeField(blank=True, null=True)
    fixed_asset = models.ForeignKey('FixedAsset', models.DO_NOTHING, blank=True, null=True)
    start_mileage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    end_mileage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    fuel_used = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class DesiredFeature(models.Model):
    desired_feature_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (desired_feature_id, requirement_id) found, that is not supported. The first column is selected.
    requirement = models.ForeignKey('Requirement', models.DO_NOTHING)
    product_feature = models.ForeignKey('ProductFeature', models.DO_NOTHING, blank=True, null=True)
    optional_ind = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'desired_feature'
        unique_together = (('desired_feature_id', 'requirement'),)


class Document(models.Model):
    document_id = models.CharField(primary_key=True, max_length=20)
    document_type = models.ForeignKey('DocumentType', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    document_location = models.CharField(max_length=255, blank=True, null=True)
    document_text = models.CharField(max_length=255, blank=True, null=True)
    image_data = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document'


class DocumentAttribute(models.Model):
    document = models.OneToOneField(Document, models.DO_NOTHING, primary_key=True)  # The composite primary key (document_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_attribute'
        unique_together = (('document', 'attr_name'),)


class DocumentType(models.Model):
    document_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_type'


class DocumentTypeAttr(models.Model):
    document_type = models.OneToOneField(DocumentType, models.DO_NOTHING, primary_key=True)  # The composite primary key (document_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_type_attr'
        unique_together = (('document_type', 'attr_name'),)


class EbayConfig(models.Model):
    product_store = models.OneToOneField('ProductStore', models.DO_NOTHING, primary_key=True)
    dev_id = models.CharField(max_length=255, blank=True, null=True)
    app_id = models.CharField(max_length=255, blank=True, null=True)
    cert_id = models.CharField(max_length=255, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    compatibility_level = models.CharField(max_length=20, blank=True, null=True)
    site_id = models.CharField(max_length=20, blank=True, null=True)
    xml_gateway_uri = models.CharField(max_length=255, blank=True, null=True)
    custom_xml = models.TextField(blank=True, null=True)
    web_site = models.ForeignKey('WebSite', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebay_config'


class EbayShippingMethod(models.Model):
    shipment_method_name = models.CharField(primary_key=True, max_length=60)  # The composite primary key (shipment_method_name, product_store_id) found, that is not supported. The first column is selected.
    product_store = models.ForeignKey('ProductStore', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    additional_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    additional_percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    method_type_enum = models.ForeignKey('Enumeration', models.DO_NOTHING, blank=True, null=True)
    carrier_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    shipment_method_type = models.ForeignKey('ShipmentMethodType', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebay_shipping_method'
        unique_together = (('shipment_method_name', 'product_store'),)


class EftAccount(models.Model):
    payment_method = models.OneToOneField('PaymentMethod', models.DO_NOTHING, primary_key=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    routing_number = models.CharField(max_length=60, blank=True, null=True)
    account_type = models.CharField(max_length=60, blank=True, null=True)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    name_on_account = models.CharField(max_length=100, blank=True, null=True)
    company_name_on_account = models.CharField(max_length=100, blank=True, null=True)
    contact_mech = models.ForeignKey('PostalAddress', models.DO_NOTHING, blank=True, null=True)
    years_at_bank = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eft_account'


class ElectronicText(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)
    text_data = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'electronic_text'


class EmailAddressVerification(models.Model):
    email_address = models.CharField(primary_key=True, max_length=255)
    verify_hash = models.CharField(unique=True, max_length=255, blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_address_verification'


class EmailTemplateSetting(models.Model):
    email_template_setting_id = models.CharField(primary_key=True, max_length=20)
    email_type = models.ForeignKey('Enumeration', models.DO_NOTHING, db_column='email_type', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    body_screen_location = models.CharField(max_length=255, blank=True, null=True)
    xslfo_attach_screen_location = models.CharField(max_length=255, blank=True, null=True)
    from_address = models.CharField(max_length=320, blank=True, null=True)
    cc_address = models.CharField(max_length=320, blank=True, null=True)
    bcc_address = models.CharField(max_length=320, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template_setting'


class EmplLeave(models.Model):
    party = models.OneToOneField('Party', models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, leave_type_id, from_date) found, that is not supported. The first column is selected.
    leave_type = models.ForeignKey('EmplLeaveType', models.DO_NOTHING)
    empl_leave_reason_type = models.ForeignKey('EmplLeaveReasonType', models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    approver_party = models.ForeignKey('Party', models.DO_NOTHING, related_name='emplleave_approver_party_set', blank=True, null=True)
    leave_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='leave_status', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_leave'
        unique_together = (('party', 'leave_type', 'from_date'),)


class EmplLeaveReasonType(models.Model):
    empl_leave_reason_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_leave_reason_type'


class EmplLeaveType(models.Model):
    leave_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_leave_type'


class EmplPosition(models.Model):
    empl_position_id = models.CharField(primary_key=True, max_length=20)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    budget_id = models.CharField(max_length=20, blank=True, null=True)
    budget_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    empl_position_type_id = models.CharField(max_length=20, blank=True, null=True)
    estimated_from_date = models.DateTimeField(blank=True, null=True)
    estimated_thru_date = models.DateTimeField(blank=True, null=True)
    salary_flag = models.CharField(max_length=1, blank=True, null=True)
    exempt_flag = models.CharField(max_length=1, blank=True, null=True)
    fulltime_flag = models.CharField(max_length=1, blank=True, null=True)
    temporary_flag = models.CharField(max_length=1, blank=True, null=True)
    actual_from_date = models.DateTimeField(blank=True, null=True)
    actual_thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position'


class EmplPositionClassType(models.Model):
    empl_position_class_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position_class_type'


class EmplPositionFulfillment(models.Model):
    empl_position = models.OneToOneField(EmplPosition, models.DO_NOTHING, primary_key=True)  # The composite primary key (empl_position_id, party_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position_fulfillment'
        unique_together = (('empl_position', 'party', 'from_date'),)


class EmplPositionReportingStruct(models.Model):
    empl_position_id_reporting_to = models.OneToOneField(EmplPosition, models.DO_NOTHING, db_column='empl_position_id_reporting_to', primary_key=True)  # The composite primary key (empl_position_id_reporting_to, empl_position_id_managed_by, from_date) found, that is not supported. The first column is selected.
    empl_position_id_managed_by = models.ForeignKey(EmplPosition, models.DO_NOTHING, db_column='empl_position_id_managed_by', related_name='emplpositionreportingstruct_empl_position_id_managed_by_set')
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    primary_flag = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position_reporting_struct'
        unique_together = (('empl_position_id_reporting_to', 'empl_position_id_managed_by', 'from_date'),)


class EmplPositionResponsibility(models.Model):
    empl_position = models.OneToOneField(EmplPosition, models.DO_NOTHING, primary_key=True)  # The composite primary key (empl_position_id, responsibility_type_id, from_date) found, that is not supported. The first column is selected.
    responsibility_type = models.ForeignKey('ResponsibilityType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position_responsibility'
        unique_together = (('empl_position', 'responsibility_type', 'from_date'),)


class EmplPositionType(models.Model):
    empl_position_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position_type'


class EmplPositionTypeClass(models.Model):
    empl_position_type = models.OneToOneField(EmplPositionType, models.DO_NOTHING, primary_key=True)  # The composite primary key (empl_position_type_id, empl_position_class_type_id, from_date) found, that is not supported. The first column is selected.
    empl_position_class_type = models.ForeignKey(EmplPositionClassType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    standard_hours_per_week = models.FloatField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position_type_class'
        unique_together = (('empl_position_type', 'empl_position_class_type', 'from_date'),)


class EmplPositionTypeRate(models.Model):
    empl_position_type = models.OneToOneField(EmplPositionType, models.DO_NOTHING, primary_key=True)  # The composite primary key (empl_position_type_id, period_type_id, from_date) found, that is not supported. The first column is selected.
    period_type = models.ForeignKey('PeriodType', models.DO_NOTHING)
    pay_grade_id = models.CharField(max_length=20, blank=True, null=True)
    salary_step_seq_id = models.CharField(max_length=20, blank=True, null=True)
    rate_type_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position_type_rate'
        unique_together = (('empl_position_type', 'period_type', 'from_date'),)


class EmplPositionTypeRateNew(models.Model):
    empl_position_type = models.OneToOneField(EmplPositionType, models.DO_NOTHING, primary_key=True)  # The composite primary key (empl_position_type_id, rate_type_id, from_date) found, that is not supported. The first column is selected.
    rate_type_id = models.CharField(max_length=20)
    pay_grade_id = models.CharField(max_length=20, blank=True, null=True)
    salary_step_seq_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empl_position_type_rate_new'
        unique_together = (('empl_position_type', 'rate_type_id', 'from_date'),)


class Employment(models.Model):
    role_type_id_from = models.CharField(primary_key=True, max_length=20)  # The composite primary key (role_type_id_from, role_type_id_to, party_id_from, party_id_to, from_date) found, that is not supported. The first column is selected.
    role_type_id_to = models.CharField(max_length=20)
    party_id_from = models.ForeignKey('Party', models.DO_NOTHING, db_column='party_id_from')
    party_id_to = models.ForeignKey('Party', models.DO_NOTHING, db_column='party_id_to', related_name='employment_party_id_to_set')
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    termination_reason_id = models.CharField(max_length=20, blank=True, null=True)
    termination_type_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employment'
        unique_together = (('role_type_id_from', 'role_type_id_to', 'party_id_from', 'party_id_to', 'from_date'),)


class EmploymentApp(models.Model):
    application_id = models.CharField(primary_key=True, max_length=20)
    empl_position_id = models.CharField(max_length=20, blank=True, null=True)
    status_id = models.CharField(max_length=20, blank=True, null=True)
    employment_app_source_type_id = models.CharField(max_length=20, blank=True, null=True)
    applying_party_id = models.CharField(max_length=20, blank=True, null=True)
    referred_by_party_id = models.CharField(max_length=20, blank=True, null=True)
    application_date = models.DateTimeField(blank=True, null=True)
    approver_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    job_requisition = models.ForeignKey('JobRequisition', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employment_app'


class EmploymentAppSourceType(models.Model):
    employment_app_source_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employment_app_source_type'


class EntityAuditLog(models.Model):
    audit_history_seq_id = models.CharField(primary_key=True, max_length=20)
    changed_entity_name = models.CharField(max_length=255, blank=True, null=True)
    changed_field_name = models.CharField(max_length=255, blank=True, null=True)
    pk_combined_value_text = models.CharField(max_length=255, blank=True, null=True)
    old_value_text = models.CharField(max_length=255, blank=True, null=True)
    new_value_text = models.CharField(max_length=255, blank=True, null=True)
    changed_date = models.DateTimeField(blank=True, null=True)
    changed_by_info = models.CharField(max_length=255, blank=True, null=True)
    changed_session_info = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_audit_log'


class EntityGroup(models.Model):
    entity_group_id = models.CharField(primary_key=True, max_length=20)
    entity_group_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_group'


class EntityGroupEntry(models.Model):
    entity_group = models.OneToOneField(EntityGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (entity_group_id, entity_or_package) found, that is not supported. The first column is selected.
    entity_or_package = models.CharField(max_length=255)
    appl_enum_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_group_entry'
        unique_together = (('entity_group', 'entity_or_package'),)


class EntityKeyStore(models.Model):
    key_name = models.CharField(primary_key=True, max_length=255)
    key_text = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_key_store'


class EntitySync(models.Model):
    entity_sync_id = models.CharField(primary_key=True, max_length=20)
    run_status_id = models.CharField(max_length=20, blank=True, null=True)
    last_successful_synch_time = models.DateTimeField(blank=True, null=True)
    last_history_start_date = models.DateTimeField(blank=True, null=True)
    pre_offline_synch_time = models.DateTimeField(blank=True, null=True)
    offline_sync_split_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sync_split_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sync_end_buffer_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_running_no_update_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    target_service_name = models.CharField(max_length=255, blank=True, null=True)
    target_delegator_name = models.CharField(max_length=255, blank=True, null=True)
    keep_remove_info_hours = models.FloatField(blank=True, null=True)
    for_pull_only = models.CharField(max_length=1, blank=True, null=True)
    for_push_only = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_sync'


class EntitySyncHistory(models.Model):
    entity_sync = models.OneToOneField(EntitySync, models.DO_NOTHING, primary_key=True)  # The composite primary key (entity_sync_id, start_date) found, that is not supported. The first column is selected.
    start_date = models.DateTimeField()
    run_status_id = models.CharField(max_length=20, blank=True, null=True)
    beginning_synch_time = models.DateTimeField(blank=True, null=True)
    last_successful_synch_time = models.DateTimeField(blank=True, null=True)
    last_candidate_end_time = models.DateTimeField(blank=True, null=True)
    last_split_start_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    to_create_inserted = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    to_create_updated = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    to_create_not_updated = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    to_store_inserted = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    to_store_updated = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    to_store_not_updated = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    to_remove_deleted = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    to_remove_already_deleted = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    total_rows_exported = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    total_rows_to_create = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    total_rows_to_store = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    total_rows_to_remove = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    total_splits = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    total_store_calls = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    running_time_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    per_split_min_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    per_split_max_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    per_split_min_items = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    per_split_max_items = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_sync_history'
        unique_together = (('entity_sync', 'start_date'),)


class EntitySyncInclude(models.Model):
    entity_sync = models.OneToOneField(EntitySync, models.DO_NOTHING, primary_key=True)  # The composite primary key (entity_sync_id, entity_or_package) found, that is not supported. The first column is selected.
    entity_or_package = models.CharField(max_length=255)
    appl_enum_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_sync_include'
        unique_together = (('entity_sync', 'entity_or_package'),)


class EntitySyncIncludeGroup(models.Model):
    entity_sync = models.OneToOneField(EntitySync, models.DO_NOTHING, primary_key=True)  # The composite primary key (entity_sync_id, entity_group_id) found, that is not supported. The first column is selected.
    entity_group = models.ForeignKey(EntityGroup, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_sync_include_group'
        unique_together = (('entity_sync', 'entity_group'),)


class EntitySyncRemove(models.Model):
    entity_sync_remove_id = models.CharField(primary_key=True, max_length=20)
    primary_key_removed = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity_sync_remove'


class Enumeration(models.Model):
    enum_id = models.CharField(primary_key=True, max_length=20)
    enum_type = models.ForeignKey('EnumerationType', models.DO_NOTHING, blank=True, null=True)
    enum_code = models.CharField(max_length=60, blank=True, null=True)
    sequence_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enumeration'


class EnumerationType(models.Model):
    enum_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enumeration_type'


class Example(models.Model):
    example_id = models.CharField(primary_key=True, max_length=20)
    example_type = models.ForeignKey('ExampleType', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    example_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    example_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    example_date = models.DateTimeField(blank=True, null=True)
    another_date = models.DateTimeField(blank=True, null=True)
    another_text = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'example'


class ExampleFeature(models.Model):
    example_feature_id = models.CharField(primary_key=True, max_length=20)
    feature_source_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'example_feature'


class ExampleFeatureAppl(models.Model):
    example = models.OneToOneField(Example, models.DO_NOTHING, primary_key=True)  # The composite primary key (example_id, example_feature_id, from_date) found, that is not supported. The first column is selected.
    example_feature = models.ForeignKey(ExampleFeature, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    example_feature_appl_type = models.ForeignKey('ExampleFeatureApplType', models.DO_NOTHING, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'example_feature_appl'
        unique_together = (('example', 'example_feature', 'from_date'),)


class ExampleFeatureApplType(models.Model):
    example_feature_appl_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'example_feature_appl_type'


class ExampleItem(models.Model):
    example = models.OneToOneField(Example, models.DO_NOTHING, primary_key=True)  # The composite primary key (example_id, example_item_seq_id) found, that is not supported. The first column is selected.
    example_item_seq_id = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amount_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'example_item'
        unique_together = (('example', 'example_item_seq_id'),)


class ExampleStatus(models.Model):
    example = models.OneToOneField(Example, models.DO_NOTHING, primary_key=True)  # The composite primary key (example_id, status_date) found, that is not supported. The first column is selected.
    status_date = models.DateTimeField()
    status_end_date = models.DateTimeField(blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'example_status'
        unique_together = (('example', 'status_date'),)


class ExampleType(models.Model):
    example_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'example_type'


class Facility(models.Model):
    facility_id = models.CharField(primary_key=True, max_length=20)
    facility_type = models.ForeignKey('FacilityType', models.DO_NOTHING, blank=True, null=True)
    parent_facility = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    owner_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    default_inventory_item_type = models.ForeignKey('InventoryItemType', models.DO_NOTHING, blank=True, null=True)
    facility_name = models.CharField(max_length=100, blank=True, null=True)
    primary_facility_group = models.ForeignKey('FacilityGroup', models.DO_NOTHING, blank=True, null=True)
    square_footage = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    facility_size = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    facility_size_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    product_store_id = models.CharField(max_length=20, blank=True, null=True)
    default_days_to_ship = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    opened_date = models.DateTimeField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    default_dimension_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='facility_default_dimension_uom_set', blank=True, null=True)
    default_weight_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='facility_default_weight_uom_set', blank=True, null=True)
    geo_point = models.ForeignKey('GeoPoint', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility'


class FacilityAttribute(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_attribute'
        unique_together = (('facility', 'attr_name'),)


class FacilityCarrierShipment(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, party_id, role_type_id, shipment_method_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    shipment_method_type = models.ForeignKey('ShipmentMethodType', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_carrier_shipment'
        unique_together = (('facility', 'party', 'role_type_id', 'shipment_method_type'),)


class FacilityContactMech(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, contact_mech_id, from_date) found, that is not supported. The first column is selected.
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_contact_mech'
        unique_together = (('facility', 'contact_mech', 'from_date'),)


class FacilityContactMechPurpose(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, contact_mech_id, contact_mech_purpose_type_id, from_date) found, that is not supported. The first column is selected.
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    contact_mech_purpose_type = models.ForeignKey(ContactMechPurposeType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_contact_mech_purpose'
        unique_together = (('facility', 'contact_mech', 'contact_mech_purpose_type', 'from_date'),)


class FacilityContent(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, content_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_content'
        unique_together = (('facility', 'content', 'from_date'),)


class FacilityGroup(models.Model):
    facility_group_id = models.CharField(primary_key=True, max_length=20)
    facility_group_type = models.ForeignKey('FacilityGroupType', models.DO_NOTHING, blank=True, null=True)
    primary_parent_group = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    facility_group_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_group'


class FacilityGroupMember(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, facility_group_id, from_date) found, that is not supported. The first column is selected.
    facility_group = models.ForeignKey(FacilityGroup, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_group_member'
        unique_together = (('facility', 'facility_group', 'from_date'),)


class FacilityGroupRole(models.Model):
    facility_group = models.OneToOneField(FacilityGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_group_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_group_role'
        unique_together = (('facility_group', 'party', 'role_type_id'),)


class FacilityGroupRollup(models.Model):
    facility_group = models.OneToOneField(FacilityGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_group_id, parent_facility_group_id, from_date) found, that is not supported. The first column is selected.
    parent_facility_group = models.ForeignKey(FacilityGroup, models.DO_NOTHING, related_name='facilitygrouprollup_parent_facility_group_set')
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_group_rollup'
        unique_together = (('facility_group', 'parent_facility_group', 'from_date'),)


class FacilityGroupType(models.Model):
    facility_group_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_group_type'


class FacilityLocation(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, location_seq_id) found, that is not supported. The first column is selected.
    location_seq_id = models.CharField(max_length=20)
    location_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    area_id = models.CharField(max_length=20, blank=True, null=True)
    aisle_id = models.CharField(max_length=20, blank=True, null=True)
    section_id = models.CharField(max_length=20, blank=True, null=True)
    level_id = models.CharField(max_length=20, blank=True, null=True)
    position_id = models.CharField(max_length=20, blank=True, null=True)
    geo_point = models.ForeignKey('GeoPoint', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_location'
        unique_together = (('facility', 'location_seq_id'),)


class FacilityLocationGeoPoint(models.Model):
    facility = models.OneToOneField(FacilityLocation, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, location_seq_id, geo_point_id, from_date) found, that is not supported. The first column is selected.
    location_seq_id = models.CharField(max_length=20)
    geo_point = models.ForeignKey('GeoPoint', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_location_geo_point'
        unique_together = (('facility', 'location_seq_id', 'geo_point', 'from_date'),)


class FacilityParty(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_party'
        unique_together = (('facility', 'party', 'role_type', 'from_date'),)


class FacilityRole(models.Model):
    facility = models.OneToOneField(Facility, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_role'
        unique_together = (('facility', 'party', 'role_type_id'),)


class FacilityType(models.Model):
    facility_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_type'


class FacilityTypeAttr(models.Model):
    facility_type = models.OneToOneField(FacilityType, models.DO_NOTHING, primary_key=True)  # The composite primary key (facility_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_type_attr'
        unique_together = (('facility_type', 'attr_name'),)


class FileExtension(models.Model):
    file_extension_id = models.CharField(primary_key=True, max_length=60)
    mime_type = models.ForeignKey('MimeType', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_extension'


class FinAccount(models.Model):
    fin_account_id = models.CharField(primary_key=True, max_length=20)
    fin_account_type = models.ForeignKey('FinAccountType', models.DO_NOTHING, blank=True, null=True)
    status_id = models.CharField(max_length=20, blank=True, null=True)
    fin_account_name = models.CharField(max_length=100, blank=True, null=True)
    fin_account_code = models.CharField(max_length=255, blank=True, null=True)
    fin_account_pin = models.CharField(max_length=255, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    organization_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    owner_party = models.ForeignKey('Party', models.DO_NOTHING, related_name='finaccount_owner_party_set', blank=True, null=True)
    post_to_gl_account = models.ForeignKey('GlAccount', models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    is_refundable = models.CharField(max_length=1, blank=True, null=True)
    replenish_payment = models.ForeignKey('PaymentMethod', models.DO_NOTHING, blank=True, null=True)
    replenish_level = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    available_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account'


class FinAccountAttribute(models.Model):
    fin_account = models.OneToOneField(FinAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (fin_account_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_attribute'
        unique_together = (('fin_account', 'attr_name'),)


class FinAccountAuth(models.Model):
    fin_account_auth_id = models.CharField(primary_key=True, max_length=20)
    fin_account = models.ForeignKey(FinAccount, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    currency_uom_id = models.CharField(max_length=20, blank=True, null=True)
    authorization_date = models.DateTimeField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_auth'


class FinAccountRole(models.Model):
    fin_account = models.OneToOneField(FinAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (fin_account_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_role'
        unique_together = (('fin_account', 'party', 'role_type_id', 'from_date'),)


class FinAccountStatus(models.Model):
    fin_account = models.OneToOneField(FinAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (fin_account_id, status_id, status_date) found, that is not supported. The first column is selected.
    status = models.ForeignKey('StatusItem', models.DO_NOTHING)
    status_date = models.DateTimeField()
    status_end_date = models.DateTimeField(blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_status'
        unique_together = (('fin_account', 'status', 'status_date'),)


class FinAccountTrans(models.Model):
    fin_account_trans_id = models.CharField(primary_key=True, max_length=20)
    fin_account_trans_type = models.ForeignKey('FinAccountTransType', models.DO_NOTHING, blank=True, null=True)
    fin_account = models.ForeignKey(FinAccount, models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    gl_reconciliation = models.ForeignKey('GlReconciliation', models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    entry_date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    payment = models.ForeignKey('Payment', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('OrderItem', models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    performed_by_party = models.ForeignKey('Party', models.DO_NOTHING, related_name='finaccounttrans_performed_by_party_set', blank=True, null=True)
    reason_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_trans'


class FinAccountTransAttribute(models.Model):
    fin_account_trans = models.OneToOneField(FinAccountTrans, models.DO_NOTHING, primary_key=True)  # The composite primary key (fin_account_trans_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_trans_attribute'
        unique_together = (('fin_account_trans', 'attr_name'),)


class FinAccountTransType(models.Model):
    fin_account_trans_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_trans_type'


class FinAccountTransTypeAttr(models.Model):
    fin_account_trans_type = models.OneToOneField(FinAccountTransType, models.DO_NOTHING, primary_key=True)  # The composite primary key (fin_account_trans_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_trans_type_attr'
        unique_together = (('fin_account_trans_type', 'attr_name'),)


class FinAccountType(models.Model):
    fin_account_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    replenish_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    is_refundable = models.CharField(max_length=1, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_type'


class FinAccountTypeAttr(models.Model):
    fin_account_type = models.OneToOneField(FinAccountType, models.DO_NOTHING, primary_key=True)  # The composite primary key (fin_account_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_type_attr'
        unique_together = (('fin_account_type', 'attr_name'),)


class FinAccountTypeGlAccount(models.Model):
    fin_account_type = models.OneToOneField(FinAccountType, models.DO_NOTHING, primary_key=True)  # The composite primary key (fin_account_type_id, organization_party_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey('Party', models.DO_NOTHING)
    gl_account = models.ForeignKey('GlAccount', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fin_account_type_gl_account'
        unique_together = (('fin_account_type', 'organization_party'),)


class FixedAsset(models.Model):
    fixed_asset_id = models.CharField(primary_key=True, max_length=20)
    fixed_asset_type = models.ForeignKey('FixedAssetType', models.DO_NOTHING, blank=True, null=True)
    parent_fixed_asset = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    instance_of_product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    class_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING, blank=True, null=True)
    fixed_asset_name = models.CharField(max_length=100, blank=True, null=True)
    acquire_order = models.ForeignKey('OrderItem', models.DO_NOTHING, blank=True, null=True)
    acquire_order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    date_acquired = models.DateTimeField(blank=True, null=True)
    date_last_serviced = models.DateTimeField(blank=True, null=True)
    date_next_service = models.DateTimeField(blank=True, null=True)
    expected_end_of_life = models.DateField(blank=True, null=True)
    actual_end_of_life = models.DateField(blank=True, null=True)
    production_capacity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    calendar = models.ForeignKey('TechDataCalendar', models.DO_NOTHING, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    located_at_facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    located_at_location_seq_id = models.CharField(max_length=20, blank=True, null=True)
    salvage_value = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    depreciation = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    purchase_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    purchase_cost_uom_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset'


class FixedAssetAttribute(models.Model):
    fixed_asset = models.OneToOneField(FixedAsset, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_attribute'
        unique_together = (('fixed_asset', 'attr_name'),)


class FixedAssetDepMethod(models.Model):
    depreciation_custom_method = models.OneToOneField(CustomMethod, models.DO_NOTHING, primary_key=True)  # The composite primary key (depreciation_custom_method_id, fixed_asset_id) found, that is not supported. The first column is selected.
    fixed_asset = models.ForeignKey(FixedAsset, models.DO_NOTHING)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_dep_method'
        unique_together = (('depreciation_custom_method', 'fixed_asset'),)


class FixedAssetGeoPoint(models.Model):
    fixed_asset = models.OneToOneField(FixedAsset, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, geo_point_id, from_date) found, that is not supported. The first column is selected.
    geo_point = models.ForeignKey('GeoPoint', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_geo_point'
        unique_together = (('fixed_asset', 'geo_point', 'from_date'),)


class FixedAssetIdent(models.Model):
    fixed_asset = models.OneToOneField(FixedAsset, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, fixed_asset_ident_type_id) found, that is not supported. The first column is selected.
    fixed_asset_ident_type = models.ForeignKey('FixedAssetIdentType', models.DO_NOTHING)
    id_value = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_ident'
        unique_together = (('fixed_asset', 'fixed_asset_ident_type'),)


class FixedAssetIdentType(models.Model):
    fixed_asset_ident_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_ident_type'


class FixedAssetMaint(models.Model):
    fixed_asset = models.OneToOneField(FixedAsset, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, maint_hist_seq_id) found, that is not supported. The first column is selected.
    maint_hist_seq_id = models.CharField(max_length=20)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    product_maint_type = models.ForeignKey('ProductMaintType', models.DO_NOTHING, blank=True, null=True)
    product_maint_seq_id = models.CharField(max_length=20, blank=True, null=True)
    schedule_work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    interval_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    interval_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    interval_meter_type = models.ForeignKey('ProductMeterType', models.DO_NOTHING, blank=True, null=True)
    purchase_order = models.ForeignKey('OrderHeader', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_maint'
        unique_together = (('fixed_asset', 'maint_hist_seq_id'),)


class FixedAssetMaintMeter(models.Model):
    fixed_asset = models.OneToOneField(FixedAssetMaint, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, maint_hist_seq_id, product_meter_type_id) found, that is not supported. The first column is selected.
    maint_hist_seq_id = models.CharField(max_length=20)
    product_meter_type = models.ForeignKey('ProductMeterType', models.DO_NOTHING)
    meter_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_maint_meter'
        unique_together = (('fixed_asset', 'maint_hist_seq_id', 'product_meter_type'),)


class FixedAssetMaintOrder(models.Model):
    fixed_asset = models.OneToOneField(FixedAsset, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, maint_hist_seq_id, order_id, order_item_seq_id) found, that is not supported. The first column is selected.
    maint_hist_seq_id = models.CharField(max_length=20)
    order = models.ForeignKey('OrderHeader', models.DO_NOTHING)
    order_item_seq_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_maint_order'
        unique_together = (('fixed_asset', 'maint_hist_seq_id', 'order', 'order_item_seq_id'),)


class FixedAssetMeter(models.Model):
    fixed_asset = models.OneToOneField(FixedAssetMaint, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, product_meter_type_id, reading_date) found, that is not supported. The first column is selected.
    product_meter_type = models.ForeignKey('ProductMeterType', models.DO_NOTHING)
    reading_date = models.DateTimeField()
    meter_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reading_reason_enum_id = models.CharField(max_length=20, blank=True, null=True)
    maint_hist_seq_id = models.CharField(max_length=20, blank=True, null=True)
    work_effort_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_meter'
        unique_together = (('fixed_asset', 'product_meter_type', 'reading_date'),)


class FixedAssetProduct(models.Model):
    fixed_asset = models.OneToOneField(FixedAsset, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, product_id, fixed_asset_product_type_id, from_date) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    fixed_asset_product_type = models.ForeignKey('FixedAssetProductType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_product'
        unique_together = (('fixed_asset', 'product', 'fixed_asset_product_type', 'from_date'),)


class FixedAssetProductType(models.Model):
    fixed_asset_product_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_product_type'


class FixedAssetRegistration(models.Model):
    fixed_asset = models.OneToOneField(FixedAsset, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, from_date) found, that is not supported. The first column is selected.
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    registration_date = models.DateTimeField(blank=True, null=True)
    gov_agency_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    license_number = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_registration'
        unique_together = (('fixed_asset', 'from_date'),)


class FixedAssetStdCost(models.Model):
    fixed_asset = models.OneToOneField(FixedAsset, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_id, fixed_asset_std_cost_type_id, from_date) found, that is not supported. The first column is selected.
    fixed_asset_std_cost_type = models.ForeignKey('FixedAssetStdCostType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    amount_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_std_cost'
        unique_together = (('fixed_asset', 'fixed_asset_std_cost_type', 'from_date'),)


class FixedAssetStdCostType(models.Model):
    fixed_asset_std_cost_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_std_cost_type'


class FixedAssetType(models.Model):
    fixed_asset_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_type'


class FixedAssetTypeAttr(models.Model):
    fixed_asset_type = models.OneToOneField(FixedAssetType, models.DO_NOTHING, primary_key=True)  # The composite primary key (fixed_asset_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_type_attr'
        unique_together = (('fixed_asset_type', 'attr_name'),)


class FixedAssetTypeGlAccount(models.Model):
    fixed_asset_type_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (fixed_asset_type_id, fixed_asset_id, organization_party_id) found, that is not supported. The first column is selected.
    fixed_asset_id = models.CharField(max_length=20)
    organization_party = models.ForeignKey('Party', models.DO_NOTHING)
    asset_gl_account = models.ForeignKey('GlAccount', models.DO_NOTHING, blank=True, null=True)
    acc_dep_gl_account = models.ForeignKey('GlAccount', models.DO_NOTHING, related_name='fixedassettypeglaccount_acc_dep_gl_account_set', blank=True, null=True)
    dep_gl_account = models.ForeignKey('GlAccount', models.DO_NOTHING, related_name='fixedassettypeglaccount_dep_gl_account_set', blank=True, null=True)
    profit_gl_account = models.ForeignKey('GlAccount', models.DO_NOTHING, related_name='fixedassettypeglaccount_profit_gl_account_set', blank=True, null=True)
    loss_gl_account = models.ForeignKey('GlAccount', models.DO_NOTHING, related_name='fixedassettypeglaccount_loss_gl_account_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_asset_type_gl_account'
        unique_together = (('fixed_asset_type_id', 'fixed_asset_id', 'organization_party'),)


class Geo(models.Model):
    geo_id = models.CharField(primary_key=True, max_length=20)
    geo_type = models.ForeignKey('GeoType', models.DO_NOTHING, blank=True, null=True)
    geo_name = models.CharField(max_length=100, blank=True, null=True)
    geo_code = models.CharField(max_length=60, blank=True, null=True)
    geo_sec_code = models.CharField(max_length=60, blank=True, null=True)
    abbreviation = models.CharField(max_length=60, blank=True, null=True)
    well_known_text = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo'


class GeoAssoc(models.Model):
    geo = models.OneToOneField(Geo, models.DO_NOTHING, primary_key=True)  # The composite primary key (geo_id, geo_id_to) found, that is not supported. The first column is selected.
    geo_id_to = models.ForeignKey(Geo, models.DO_NOTHING, db_column='geo_id_to', related_name='geoassoc_geo_id_to_set')
    geo_assoc_type = models.ForeignKey('GeoAssocType', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_assoc'
        unique_together = (('geo', 'geo_id_to'),)


class GeoAssocType(models.Model):
    geo_assoc_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_assoc_type'


class GeoPoint(models.Model):
    geo_point_id = models.CharField(primary_key=True, max_length=20)
    geo_point_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    data_source = models.ForeignKey(DataSource, models.DO_NOTHING, blank=True, null=True)
    latitude = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)
    elevation = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    elevation_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_point'


class GeoType(models.Model):
    geo_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_type'


class GiftCard(models.Model):
    payment_method = models.OneToOneField('PaymentMethod', models.DO_NOTHING, primary_key=True)
    card_number = models.CharField(max_length=255, blank=True, null=True)
    pin_number = models.CharField(max_length=255, blank=True, null=True)
    expire_date = models.CharField(max_length=7, blank=True, null=True)
    contact_mech = models.ForeignKey('PostalAddress', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gift_card'


class GiftCardFulfillment(models.Model):
    fulfillment_id = models.CharField(primary_key=True, max_length=20)
    type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('OrderItem', models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    survey_response = models.ForeignKey('SurveyResponse', models.DO_NOTHING, blank=True, null=True)
    card_number = models.CharField(max_length=255, blank=True, null=True)
    pin_number = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    response_code = models.CharField(max_length=60, blank=True, null=True)
    reference_num = models.CharField(max_length=60, blank=True, null=True)
    auth_code = models.CharField(max_length=60, blank=True, null=True)
    fulfillment_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gift_card_fulfillment'


class GitHubUser(models.Model):
    git_hub_user_id = models.CharField(primary_key=True, max_length=255)
    product_store = models.ForeignKey('ProductStore', models.DO_NOTHING, blank=True, null=True)
    env_prefix = models.CharField(max_length=60, blank=True, null=True)
    token_type = models.CharField(max_length=60, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'git_hub_user'


class GlAccount(models.Model):
    gl_account_id = models.CharField(primary_key=True, max_length=20)
    gl_account_type = models.ForeignKey('GlAccountType', models.DO_NOTHING, blank=True, null=True)
    gl_account_class = models.ForeignKey('GlAccountClass', models.DO_NOTHING, blank=True, null=True)
    gl_resource_type = models.ForeignKey('GlResourceType', models.DO_NOTHING, blank=True, null=True)
    gl_xbrl_class = models.ForeignKey('GlXbrlClass', models.DO_NOTHING, blank=True, null=True)
    parent_gl_account = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    account_code = models.CharField(unique=True, max_length=100, blank=True, null=True)
    account_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    product_id = models.CharField(max_length=20, blank=True, null=True)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account'


class GlAccountCategory(models.Model):
    gl_account_category_id = models.CharField(primary_key=True, max_length=20)
    gl_account_category_type = models.ForeignKey('GlAccountCategoryType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_category'


class GlAccountCategoryMember(models.Model):
    gl_account = models.OneToOneField(GlAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (gl_account_id, gl_account_category_id, from_date) found, that is not supported. The first column is selected.
    gl_account_category = models.ForeignKey(GlAccountCategory, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    amount_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_category_member'
        unique_together = (('gl_account', 'gl_account_category', 'from_date'),)


class GlAccountCategoryType(models.Model):
    gl_account_category_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_category_type'


class GlAccountClass(models.Model):
    gl_account_class_id = models.CharField(primary_key=True, max_length=20)
    parent_class = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_asset_class = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_class'


class GlAccountGroup(models.Model):
    gl_account_group_id = models.CharField(primary_key=True, max_length=20)
    gl_account_group_type = models.ForeignKey('GlAccountGroupType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_group'


class GlAccountGroupMember(models.Model):
    gl_account = models.OneToOneField(GlAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (gl_account_id, gl_account_group_type_id) found, that is not supported. The first column is selected.
    gl_account_group_type = models.ForeignKey('GlAccountGroupType', models.DO_NOTHING)
    gl_account_group = models.ForeignKey(GlAccountGroup, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_group_member'
        unique_together = (('gl_account', 'gl_account_group_type'),)


class GlAccountGroupType(models.Model):
    gl_account_group_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_group_type'


class GlAccountHistory(models.Model):
    gl_account = models.OneToOneField(GlAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (gl_account_id, organization_party_id, custom_time_period_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey('Party', models.DO_NOTHING)
    custom_time_period = models.ForeignKey(CustomTimePeriod, models.DO_NOTHING)
    opening_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    posted_debits = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    posted_credits = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ending_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_history'
        unique_together = (('gl_account', 'organization_party', 'custom_time_period'),)


class GlAccountOrganization(models.Model):
    gl_account = models.OneToOneField(GlAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (gl_account_id, organization_party_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey('Party', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_organization'
        unique_together = (('gl_account', 'organization_party'),)


class GlAccountRole(models.Model):
    gl_account = models.OneToOneField(GlAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (gl_account_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_role'
        unique_together = (('gl_account', 'party', 'role_type_id', 'from_date'),)


class GlAccountType(models.Model):
    gl_account_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_type'


class GlAccountTypeDefault(models.Model):
    gl_account_type = models.OneToOneField(GlAccountType, models.DO_NOTHING, primary_key=True)  # The composite primary key (gl_account_type_id, organization_party_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey('Party', models.DO_NOTHING)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_account_type_default'
        unique_together = (('gl_account_type', 'organization_party'),)


class GlBudgetXref(models.Model):
    gl_account = models.OneToOneField(GlAccount, models.DO_NOTHING, primary_key=True)  # The composite primary key (gl_account_id, budget_item_type_id, from_date) found, that is not supported. The first column is selected.
    budget_item_type = models.ForeignKey(BudgetItemType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    allocation_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_budget_xref'
        unique_together = (('gl_account', 'budget_item_type', 'from_date'),)


class GlFiscalType(models.Model):
    gl_fiscal_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_fiscal_type'


class GlJournal(models.Model):
    gl_journal_id = models.CharField(primary_key=True, max_length=20)
    gl_journal_name = models.CharField(max_length=100, blank=True, null=True)
    organization_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    is_posted = models.CharField(max_length=1, blank=True, null=True)
    posted_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_journal'


class GlReconciliation(models.Model):
    gl_reconciliation_id = models.CharField(primary_key=True, max_length=20)
    gl_reconciliation_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    organization_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    reconciled_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    reconciled_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_reconciliation'


class GlReconciliationEntry(models.Model):
    gl_reconciliation = models.OneToOneField(GlReconciliation, models.DO_NOTHING, primary_key=True)  # The composite primary key (gl_reconciliation_id, acctg_trans_id, acctg_trans_entry_seq_id) found, that is not supported. The first column is selected.
    acctg_trans = models.ForeignKey(AcctgTransEntry, models.DO_NOTHING)
    acctg_trans_entry_seq_id = models.CharField(max_length=20)
    reconciled_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_reconciliation_entry'
        unique_together = (('gl_reconciliation', 'acctg_trans', 'acctg_trans_entry_seq_id'),)


class GlResourceType(models.Model):
    gl_resource_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_resource_type'


class GlXbrlClass(models.Model):
    gl_xbrl_class_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gl_xbrl_class'


class GoodIdentification(models.Model):
    good_identification_type = models.OneToOneField('GoodIdentificationType', models.DO_NOTHING, primary_key=True)  # The composite primary key (good_identification_type_id, product_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    id_value = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'good_identification'
        unique_together = (('good_identification_type', 'product'),)


class GoodIdentificationType(models.Model):
    good_identification_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'good_identification_type'


class ImageDataResource(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)
    image_data = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_data_resource'


class InventoryItem(models.Model):
    inventory_item_id = models.CharField(primary_key=True, max_length=20)
    inventory_item_type = models.ForeignKey('InventoryItemType', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    owner_party = models.ForeignKey('Party', models.DO_NOTHING, related_name='inventoryitem_owner_party_set', blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    datetime_received = models.DateTimeField(blank=True, null=True)
    datetime_manufactured = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    container = models.ForeignKey(Container, models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey('Lot', models.DO_NOTHING, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    bin_number = models.CharField(max_length=20, blank=True, null=True)
    location_seq_id = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    quantity_on_hand_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    available_to_promise_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    accounting_quantity_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_on_hand = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    available_to_promise = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    soft_identifier = models.CharField(unique=True, max_length=255, blank=True, null=True)
    activation_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    activation_valid_thru = models.DateTimeField(blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='inventoryitem_currency_uom_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    fixed_asset = models.ForeignKey(FixedAsset, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item'


class InventoryItemAttribute(models.Model):
    inventory_item = models.OneToOneField(InventoryItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (inventory_item_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_attribute'
        unique_together = (('inventory_item', 'attr_name'),)


class InventoryItemDetail(models.Model):
    inventory_item = models.OneToOneField(InventoryItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (inventory_item_id, inventory_item_detail_seq_id) found, that is not supported. The first column is selected.
    inventory_item_detail_seq_id = models.CharField(max_length=20)
    effective_date = models.DateTimeField(blank=True, null=True)
    quantity_on_hand_diff = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    available_to_promise_diff = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    accounting_quantity_diff = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    order_id = models.CharField(max_length=20, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    ship_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    shipment_id = models.CharField(max_length=20, blank=True, null=True)
    shipment_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    return_id = models.CharField(max_length=20, blank=True, null=True)
    return_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    fixed_asset = models.ForeignKey(FixedAssetMaint, models.DO_NOTHING, blank=True, null=True)
    maint_hist_seq_id = models.CharField(max_length=20, blank=True, null=True)
    item_issuance = models.ForeignKey('ItemIssuance', models.DO_NOTHING, blank=True, null=True)
    receipt = models.ForeignKey('ShipmentReceipt', models.DO_NOTHING, blank=True, null=True)
    physical_inventory = models.ForeignKey('PhysicalInventory', models.DO_NOTHING, blank=True, null=True)
    reason_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_detail'
        unique_together = (('inventory_item', 'inventory_item_detail_seq_id'),)


class InventoryItemLabel(models.Model):
    inventory_item_label_id = models.CharField(primary_key=True, max_length=20)
    inventory_item_label_type = models.ForeignKey('InventoryItemLabelType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_label'


class InventoryItemLabelAppl(models.Model):
    inventory_item = models.OneToOneField(InventoryItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (inventory_item_id, inventory_item_label_type_id) found, that is not supported. The first column is selected.
    inventory_item_label_type = models.ForeignKey('InventoryItemLabelType', models.DO_NOTHING)
    inventory_item_label = models.ForeignKey(InventoryItemLabel, models.DO_NOTHING, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_label_appl'
        unique_together = (('inventory_item', 'inventory_item_label_type'),)


class InventoryItemLabelType(models.Model):
    inventory_item_label_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_label_type'


class InventoryItemStatus(models.Model):
    inventory_item = models.OneToOneField(InventoryItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (inventory_item_id, status_id, status_datetime) found, that is not supported. The first column is selected.
    status = models.ForeignKey('StatusItem', models.DO_NOTHING)
    status_datetime = models.DateTimeField()
    status_end_datetime = models.DateTimeField(blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    owner_party_id = models.CharField(max_length=20, blank=True, null=True)
    product_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_status'
        unique_together = (('inventory_item', 'status', 'status_datetime'),)


class InventoryItemTempRes(models.Model):
    visit_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (visit_id, product_id, product_store_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    product_store = models.ForeignKey('ProductStore', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserved_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_temp_res'
        unique_together = (('visit_id', 'product', 'product_store'),)


class InventoryItemType(models.Model):
    inventory_item_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_type'


class InventoryItemTypeAttr(models.Model):
    inventory_item_type = models.OneToOneField(InventoryItemType, models.DO_NOTHING, primary_key=True)  # The composite primary key (inventory_item_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_type_attr'
        unique_together = (('inventory_item_type', 'attr_name'),)


class InventoryItemVariance(models.Model):
    inventory_item = models.OneToOneField(InventoryItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (inventory_item_id, physical_inventory_id) found, that is not supported. The first column is selected.
    physical_inventory = models.ForeignKey('PhysicalInventory', models.DO_NOTHING)
    variance_reason = models.ForeignKey('VarianceReason', models.DO_NOTHING, blank=True, null=True)
    available_to_promise_var = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_on_hand_var = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_item_variance'
        unique_together = (('inventory_item', 'physical_inventory'),)


class InventoryTransfer(models.Model):
    inventory_transfer_id = models.CharField(primary_key=True, max_length=20)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    location_seq_id = models.CharField(max_length=20, blank=True, null=True)
    container = models.ForeignKey(Container, models.DO_NOTHING, blank=True, null=True)
    facility_id_to = models.ForeignKey(Facility, models.DO_NOTHING, db_column='facility_id_to', related_name='inventorytransfer_facility_id_to_set', blank=True, null=True)
    location_seq_id_to = models.CharField(max_length=20, blank=True, null=True)
    container_id_to = models.ForeignKey(Container, models.DO_NOTHING, db_column='container_id_to', related_name='inventorytransfer_container_id_to_set', blank=True, null=True)
    item_issuance = models.ForeignKey('ItemIssuance', models.DO_NOTHING, blank=True, null=True)
    send_date = models.DateTimeField(blank=True, null=True)
    receive_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_transfer'


class Invoice(models.Model):
    invoice_id = models.CharField(primary_key=True, max_length=20)
    invoice_type = models.ForeignKey('InvoiceType', models.DO_NOTHING, blank=True, null=True)
    party_id_from = models.ForeignKey('Party', models.DO_NOTHING, db_column='party_id_from', blank=True, null=True)
    party = models.ForeignKey('Party', models.DO_NOTHING, related_name='invoice_party_set', blank=True, null=True)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    billing_account = models.ForeignKey(BillingAccount, models.DO_NOTHING, blank=True, null=True)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    invoice_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)
    invoice_message = models.CharField(max_length=255, blank=True, null=True)
    reference_number = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    recurrence_info = models.ForeignKey('RecurrenceInfo', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceAttribute(models.Model):
    invoice = models.OneToOneField(Invoice, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_attribute'
        unique_together = (('invoice', 'attr_name'),)


class InvoiceContactMech(models.Model):
    invoice = models.OneToOneField(Invoice, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_id, contact_mech_purpose_type_id, contact_mech_id) found, that is not supported. The first column is selected.
    contact_mech_purpose_type = models.ForeignKey(ContactMechPurposeType, models.DO_NOTHING)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_contact_mech'
        unique_together = (('invoice', 'contact_mech_purpose_type', 'contact_mech'),)


class InvoiceContent(models.Model):
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    invoice_content_type = models.ForeignKey('InvoiceContentType', models.DO_NOTHING)
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, invoice_id, invoice_content_type_id, from_date) found, that is not supported. The first column is selected.
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_content'
        unique_together = (('content', 'invoice', 'invoice_content_type', 'from_date'),)


class InvoiceContentType(models.Model):
    invoice_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_content_type'


class InvoiceItem(models.Model):
    invoice = models.OneToOneField(Invoice, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_id, invoice_item_seq_id) found, that is not supported. The first column is selected.
    invoice_item_seq_id = models.CharField(max_length=20)
    invoice_item_type = models.ForeignKey('InvoiceItemType', models.DO_NOTHING, blank=True, null=True)
    override_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    override_org_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    product_feature = models.ForeignKey('ProductFeature', models.DO_NOTHING, blank=True, null=True)
    parent_invoice = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    parent_invoice_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    taxable_flag = models.CharField(max_length=1, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    tax_auth_party = models.ForeignKey('Party', models.DO_NOTHING, related_name='invoiceitem_tax_auth_party_set', blank=True, null=True)
    tax_auth_geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    tax_authority_rate_seq = models.ForeignKey('TaxAuthorityRateProduct', models.DO_NOTHING, blank=True, null=True)
    sales_opportunity = models.ForeignKey('SalesOpportunity', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item'
        unique_together = (('invoice', 'invoice_item_seq_id'),)


class InvoiceItemAssoc(models.Model):
    invoice_id_from = models.OneToOneField(InvoiceItem, models.DO_NOTHING, db_column='invoice_id_from', primary_key=True)  # The composite primary key (invoice_id_from, invoice_item_seq_id_from, invoice_id_to, invoice_item_seq_id_to, invoice_item_assoc_type_id, from_date) found, that is not supported. The first column is selected.
    invoice_item_seq_id_from = models.CharField(max_length=20)
    invoice_id_to = models.ForeignKey(InvoiceItem, models.DO_NOTHING, db_column='invoice_id_to', related_name='invoiceitemassoc_invoice_id_to_set')
    invoice_item_seq_id_to = models.CharField(max_length=20)
    invoice_item_assoc_type = models.ForeignKey('InvoiceItemAssocType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    party_id_from = models.CharField(max_length=20, blank=True, null=True)
    party_id_to = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item_assoc'
        unique_together = (('invoice_id_from', 'invoice_item_seq_id_from', 'invoice_id_to', 'invoice_item_seq_id_to', 'invoice_item_assoc_type', 'from_date'),)


class InvoiceItemAssocType(models.Model):
    invoice_item_assoc_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item_assoc_type'


class InvoiceItemAttribute(models.Model):
    invoice = models.OneToOneField(InvoiceItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_id, invoice_item_seq_id, attr_name) found, that is not supported. The first column is selected.
    invoice_item_seq_id = models.CharField(max_length=20)
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item_attribute'
        unique_together = (('invoice', 'invoice_item_seq_id', 'attr_name'),)


class InvoiceItemType(models.Model):
    invoice_item_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    default_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item_type'


class InvoiceItemTypeAttr(models.Model):
    invoice_item_type = models.OneToOneField(InvoiceItemType, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_item_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item_type_attr'
        unique_together = (('invoice_item_type', 'attr_name'),)


class InvoiceItemTypeGlAccount(models.Model):
    invoice_item_type = models.OneToOneField(InvoiceItemType, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_item_type_id, organization_party_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey('Party', models.DO_NOTHING)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item_type_gl_account'
        unique_together = (('invoice_item_type', 'organization_party'),)


class InvoiceItemTypeMap(models.Model):
    invoice_item_map_key = models.CharField(primary_key=True, max_length=20)  # The composite primary key (invoice_item_map_key, invoice_type_id) found, that is not supported. The first column is selected.
    invoice_type = models.ForeignKey('InvoiceType', models.DO_NOTHING)
    invoice_item_type = models.ForeignKey(InvoiceItemType, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_item_type_map'
        unique_together = (('invoice_item_map_key', 'invoice_type'),)


class InvoiceNote(models.Model):
    invoice = models.OneToOneField(Invoice, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_id, note_id) found, that is not supported. The first column is selected.
    note = models.ForeignKey('NoteData', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_note'
        unique_together = (('invoice', 'note'),)


class InvoiceRole(models.Model):
    invoice = models.OneToOneField(Invoice, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    datetime_performed = models.DateTimeField(blank=True, null=True)
    percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_role'
        unique_together = (('invoice', 'party', 'role_type_id'),)


class InvoiceStatus(models.Model):
    status = models.OneToOneField('StatusItem', models.DO_NOTHING, primary_key=True)  # The composite primary key (status_id, invoice_id, status_date) found, that is not supported. The first column is selected.
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    status_date = models.DateTimeField()
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_status'
        unique_together = (('status', 'invoice', 'status_date'),)


class InvoiceTerm(models.Model):
    invoice_term_id = models.CharField(primary_key=True, max_length=20)
    term_type = models.ForeignKey('TermType', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)
    invoice_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    term_value = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    term_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    text_value = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uom_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_term'


class InvoiceTermAttribute(models.Model):
    invoice_term = models.OneToOneField(InvoiceTerm, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_term_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_term_attribute'
        unique_together = (('invoice_term', 'attr_name'),)


class InvoiceType(models.Model):
    invoice_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_type'


class InvoiceTypeAttr(models.Model):
    invoice_type = models.OneToOneField(InvoiceType, models.DO_NOTHING, primary_key=True)  # The composite primary key (invoice_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_type_attr'
        unique_together = (('invoice_type', 'attr_name'),)


class ItemIssuance(models.Model):
    item_issuance_id = models.CharField(primary_key=True, max_length=20)
    order = models.ForeignKey('OrderItem', models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    ship_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING, blank=True, null=True)
    shipment = models.ForeignKey('ShipmentItem', models.DO_NOTHING, blank=True, null=True)
    shipment_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    fixed_asset = models.ForeignKey(FixedAssetMaint, models.DO_NOTHING, blank=True, null=True)
    maint_hist_seq_id = models.CharField(max_length=20, blank=True, null=True)
    issued_date_time = models.DateTimeField(blank=True, null=True)
    issued_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cancel_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_issuance'


class ItemIssuanceRole(models.Model):
    item_issuance = models.OneToOneField(ItemIssuance, models.DO_NOTHING, primary_key=True)  # The composite primary key (item_issuance_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('Party', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_issuance_role'
        unique_together = (('item_issuance', 'party', 'role_type_id'),)


class JavaResource(models.Model):
    resource_name = models.CharField(primary_key=True, max_length=255)
    resource_value = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'java_resource'


class JobInterview(models.Model):
    job_interview_id = models.CharField(primary_key=True, max_length=20)
    job_interviewee_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    job_requisition = models.ForeignKey('JobRequisition', models.DO_NOTHING, blank=True, null=True)
    job_interviewer_party = models.ForeignKey('Party', models.DO_NOTHING, related_name='jobinterview_job_interviewer_party_set', blank=True, null=True)
    job_interview_type = models.ForeignKey('JobInterviewType', models.DO_NOTHING, blank=True, null=True)
    grade_secured_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    job_interview_result = models.CharField(max_length=20, blank=True, null=True)
    job_interview_date = models.DateField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_interview'


class JobInterviewType(models.Model):
    job_interview_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_interview_type'


class JobManagerLock(models.Model):
    instance_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (instance_id, from_date) found, that is not supported. The first column is selected.
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    reason_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_manager_lock'
        unique_together = (('instance_id', 'from_date'),)


class JobRequisition(models.Model):
    job_requisition_id = models.CharField(primary_key=True, max_length=20)
    duration_months = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    age = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    experience_months = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    experience_years = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    qualification = models.CharField(max_length=60, blank=True, null=True)
    job_location = models.CharField(max_length=20, blank=True, null=True)
    skill_type = models.ForeignKey('SkillType', models.DO_NOTHING, blank=True, null=True)
    no_of_resources = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    job_posting_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    job_requisition_date = models.DateField(blank=True, null=True)
    exam_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='jobrequisition_exam_type_enum_set', blank=True, null=True)
    required_on_date = models.DateField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_requisition'


class JobSandbox(models.Model):
    job_id = models.CharField(primary_key=True, max_length=20)
    job_name = models.CharField(max_length=100, blank=True, null=True)
    run_time = models.DateTimeField(blank=True, null=True)
    pool_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    parent_job_id = models.CharField(max_length=20, blank=True, null=True)
    previous_job_id = models.CharField(max_length=20, blank=True, null=True)
    service_name = models.CharField(max_length=100, blank=True, null=True)
    loader_name = models.CharField(max_length=100, blank=True, null=True)
    max_retry = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    current_retry_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    auth_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    run_as_user = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='run_as_user', related_name='jobsandbox_run_as_user_set', blank=True, null=True)
    runtime_data = models.ForeignKey('RuntimeData', models.DO_NOTHING, blank=True, null=True)
    recurrence_info = models.ForeignKey('RecurrenceInfo', models.DO_NOTHING, blank=True, null=True)
    temp_expr = models.ForeignKey('TemporalExpression', models.DO_NOTHING, blank=True, null=True)
    current_recurrence_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_recurrence_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    run_by_instance_id = models.CharField(max_length=20, blank=True, null=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    finish_date_time = models.DateTimeField(blank=True, null=True)
    cancel_date_time = models.DateTimeField(blank=True, null=True)
    job_result = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_sandbox'


class KeywordThesaurus(models.Model):
    entered_keyword = models.CharField(primary_key=True, max_length=255)  # The composite primary key (entered_keyword, alternate_keyword) found, that is not supported. The first column is selected.
    alternate_keyword = models.CharField(max_length=255)
    relationship_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword_thesaurus'
        unique_together = (('entered_keyword', 'alternate_keyword'),)


class LinkedInUser(models.Model):
    linked_in_user_id = models.CharField(primary_key=True, max_length=255)
    product_store = models.ForeignKey('ProductStore', models.DO_NOTHING, blank=True, null=True)
    env_prefix = models.CharField(max_length=60, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linked_in_user'


class Lot(models.Model):
    lot_id = models.CharField(primary_key=True, max_length=20)
    creation_date = models.DateTimeField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lot'


class MarketInterest(models.Model):
    product_category = models.OneToOneField('ProductCategory', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, party_classification_group_id, from_date) found, that is not supported. The first column is selected.
    party_classification_group = models.ForeignKey('PartyClassificationGroup', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'market_interest'
        unique_together = (('product_category', 'party_classification_group', 'from_date'),)


class MarketingCampaign(models.Model):
    marketing_campaign_id = models.CharField(primary_key=True, max_length=20)
    parent_campaign = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    campaign_name = models.CharField(max_length=100, blank=True, null=True)
    campaign_summary = models.TextField(blank=True, null=True)
    budgeted_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estimated_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    converted_leads = models.CharField(max_length=20, blank=True, null=True)
    expected_response_percent = models.FloatField(blank=True, null=True)
    expected_revenue = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    num_sent = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_campaign'


class MarketingCampaignNote(models.Model):
    marketing_campaign = models.OneToOneField(MarketingCampaign, models.DO_NOTHING, primary_key=True)  # The composite primary key (marketing_campaign_id, note_id) found, that is not supported. The first column is selected.
    note = models.ForeignKey('NoteData', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_campaign_note'
        unique_together = (('marketing_campaign', 'note'),)


class MarketingCampaignPrice(models.Model):
    marketing_campaign = models.OneToOneField(MarketingCampaign, models.DO_NOTHING, primary_key=True)  # The composite primary key (marketing_campaign_id, product_price_rule_id) found, that is not supported. The first column is selected.
    product_price_rule = models.ForeignKey('ProductPriceRule', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_campaign_price'
        unique_together = (('marketing_campaign', 'product_price_rule'),)


class MarketingCampaignPromo(models.Model):
    marketing_campaign = models.OneToOneField(MarketingCampaign, models.DO_NOTHING, primary_key=True)  # The composite primary key (marketing_campaign_id, product_promo_id) found, that is not supported. The first column is selected.
    product_promo = models.ForeignKey('ProductPromo', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_campaign_promo'
        unique_together = (('marketing_campaign', 'product_promo'),)


class MarketingCampaignRole(models.Model):
    marketing_campaign = models.OneToOneField(MarketingCampaign, models.DO_NOTHING, primary_key=True)  # The composite primary key (marketing_campaign_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marketing_campaign_role'
        unique_together = (('marketing_campaign', 'party', 'role_type_id'),)


class MetaDataPredicate(models.Model):
    meta_data_predicate_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta_data_predicate'


class MimeType(models.Model):
    mime_type_id = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mime_type'


class MimeTypeHtmlTemplate(models.Model):
    mime_type = models.OneToOneField(MimeType, models.DO_NOTHING, primary_key=True)
    template_location = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mime_type_html_template'


class MrpEvent(models.Model):
    mrp_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (mrp_id, product_id, event_date, mrp_event_type_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    event_date = models.DateTimeField()
    mrp_event_type = models.ForeignKey('MrpEventType', models.DO_NOTHING)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    event_name = models.TextField(blank=True, null=True)
    is_late = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_event'
        unique_together = (('mrp_id', 'product', 'event_date', 'mrp_event_type'),)


class MrpEventType(models.Model):
    mrp_event_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_event_type'


class NeedType(models.Model):
    need_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'need_type'


class NoteData(models.Model):
    note_id = models.CharField(primary_key=True, max_length=20)
    note_name = models.CharField(max_length=100, blank=True, null=True)
    note_info = models.TextField(blank=True, null=True)
    note_date_time = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    note_party = models.ForeignKey('Party', models.DO_NOTHING, db_column='note_party', blank=True, null=True)
    more_info_url = models.CharField(max_length=255, blank=True, null=True)
    more_info_item_id = models.CharField(max_length=255, blank=True, null=True)
    more_info_item_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_data'


class OAuth2GitHub(models.Model):
    product_store = models.OneToOneField('ProductStore', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, from_date) found, that is not supported. The first column is selected.
    client_id = models.CharField(max_length=60, blank=True, null=True)
    client_secret = models.CharField(max_length=60, blank=True, null=True)
    return_url = models.CharField(max_length=255, blank=True, null=True)
    local_redirect_uri = models.CharField(max_length=60, blank=True, null=True)
    icon_url = models.CharField(max_length=2000, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'o_auth2_git_hub'
        unique_together = (('product_store', 'from_date'),)


class OAuth2LinkedIn(models.Model):
    product_store = models.OneToOneField('ProductStore', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, from_date) found, that is not supported. The first column is selected.
    api_key = models.CharField(max_length=60, blank=True, null=True)
    secret_key = models.CharField(max_length=60, blank=True, null=True)
    live_return_url = models.CharField(max_length=255, blank=True, null=True)
    test_return_url = models.CharField(max_length=255, blank=True, null=True)
    local_redirect_uri = models.CharField(max_length=60, blank=True, null=True)
    icon_url = models.CharField(max_length=2000, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'o_auth2_linked_in'
        unique_together = (('product_store', 'from_date'),)


class OrderAdjustment(models.Model):
    order_adjustment_id = models.CharField(primary_key=True, max_length=20)
    order_adjustment_type = models.ForeignKey('OrderAdjustmentType', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('OrderHeader', models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    ship_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    recurring_amount = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    amount_already_included = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    product_promo = models.ForeignKey('ProductPromo', models.DO_NOTHING, blank=True, null=True)
    product_promo_rule_id = models.CharField(max_length=20, blank=True, null=True)
    product_promo_action_seq_id = models.CharField(max_length=20, blank=True, null=True)
    product_feature_id = models.CharField(max_length=20, blank=True, null=True)
    corresponding_product_id = models.CharField(max_length=20, blank=True, null=True)
    tax_authority_rate_seq = models.ForeignKey('TaxAuthorityRateProduct', models.DO_NOTHING, blank=True, null=True)
    source_reference_id = models.CharField(max_length=60, blank=True, null=True)
    source_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    customer_reference_id = models.CharField(max_length=60, blank=True, null=True)
    primary_geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    secondary_geo = models.ForeignKey(Geo, models.DO_NOTHING, related_name='orderadjustment_secondary_geo_set', blank=True, null=True)
    exempt_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tax_auth_geo = models.ForeignKey('TaxAuthority', models.DO_NOTHING, blank=True, null=True)
    tax_auth_party_id = models.CharField(max_length=20, blank=True, null=True)
    override_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    include_in_tax = models.CharField(max_length=1, blank=True, null=True)
    include_in_shipping = models.CharField(max_length=1, blank=True, null=True)
    is_manual = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    original_adjustment_id = models.CharField(max_length=20, blank=True, null=True)
    amount_per_quantity = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_adjustment'


class OrderAdjustmentAttribute(models.Model):
    order_adjustment = models.OneToOneField(OrderAdjustment, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_adjustment_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_adjustment_attribute'
        unique_together = (('order_adjustment', 'attr_name'),)


class OrderAdjustmentBilling(models.Model):
    order_adjustment = models.OneToOneField(OrderAdjustment, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_adjustment_id, invoice_id, invoice_item_seq_id) found, that is not supported. The first column is selected.
    invoice = models.ForeignKey(InvoiceItem, models.DO_NOTHING)
    invoice_item_seq_id = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_adjustment_billing'
        unique_together = (('order_adjustment', 'invoice', 'invoice_item_seq_id'),)


class OrderAdjustmentType(models.Model):
    order_adjustment_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_adjustment_type'


class OrderAdjustmentTypeAttr(models.Model):
    order_adjustment_type = models.OneToOneField(OrderAdjustmentType, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_adjustment_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_adjustment_type_attr'
        unique_together = (('order_adjustment_type', 'attr_name'),)


class OrderAttribute(models.Model):
    order = models.OneToOneField('OrderHeader', models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_attribute'
        unique_together = (('order', 'attr_name'),)


class OrderBlacklist(models.Model):
    blacklist_string = models.CharField(primary_key=True, max_length=255)  # The composite primary key (blacklist_string, order_blacklist_type_id) found, that is not supported. The first column is selected.
    order_blacklist_type = models.ForeignKey('OrderBlacklistType', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_blacklist'
        unique_together = (('blacklist_string', 'order_blacklist_type'),)


class OrderBlacklistType(models.Model):
    order_blacklist_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_blacklist_type'


class OrderContactMech(models.Model):
    order = models.OneToOneField('OrderHeader', models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, contact_mech_purpose_type_id, contact_mech_id) found, that is not supported. The first column is selected.
    contact_mech_purpose_type = models.ForeignKey(ContactMechPurposeType, models.DO_NOTHING)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_contact_mech'
        unique_together = (('order', 'contact_mech_purpose_type', 'contact_mech'),)


class OrderContent(models.Model):
    order = models.ForeignKey('OrderHeader', models.DO_NOTHING)
    order_item_seq_id = models.CharField(max_length=20)
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, order_id, order_item_seq_id, order_content_type_id, from_date) found, that is not supported. The first column is selected.
    order_content_type = models.ForeignKey('OrderContentType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_content'
        unique_together = (('content', 'order', 'order_item_seq_id', 'order_content_type', 'from_date'),)


class OrderContentType(models.Model):
    order_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_content_type'


class OrderDeliverySchedule(models.Model):
    order = models.OneToOneField('OrderHeader', models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    estimated_ready_date = models.DateTimeField(blank=True, null=True)
    cartons = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    skids_pallets = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    units_pieces = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_cubic_size = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_cubic_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    total_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_weight_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='orderdeliveryschedule_total_weight_uom_set', blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_delivery_schedule'
        unique_together = (('order', 'order_item_seq_id'),)


class OrderHeader(models.Model):
    order_id = models.CharField(primary_key=True, max_length=20)
    order_type = models.ForeignKey('OrderType', models.DO_NOTHING, blank=True, null=True)
    order_name = models.CharField(max_length=100, blank=True, null=True)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    sales_channel_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=1, blank=True, null=True)
    entry_date = models.DateTimeField(blank=True, null=True)
    pick_sheet_printed_date = models.DateTimeField(blank=True, null=True)
    visit_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    first_attempt_order_id = models.CharField(max_length=20, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, db_column='currency_uom', blank=True, null=True)
    sync_status = models.ForeignKey('StatusItem', models.DO_NOTHING, related_name='orderheader_sync_status_set', blank=True, null=True)
    billing_account = models.ForeignKey(BillingAccount, models.DO_NOTHING, blank=True, null=True)
    origin_facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    web_site_id = models.CharField(max_length=20, blank=True, null=True)
    product_store = models.ForeignKey('ProductStore', models.DO_NOTHING, blank=True, null=True)
    terminal_id = models.CharField(max_length=60, blank=True, null=True)
    transaction_id = models.CharField(max_length=60, blank=True, null=True)
    auto_order_shopping_list = models.ForeignKey('ShoppingList', models.DO_NOTHING, blank=True, null=True)
    needs_inventory_issuance = models.CharField(max_length=1, blank=True, null=True)
    is_rush_order = models.CharField(max_length=1, blank=True, null=True)
    internal_code = models.CharField(max_length=60, blank=True, null=True)
    remaining_sub_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    is_viewed = models.CharField(max_length=1, blank=True, null=True)
    invoice_per_shipment = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_header'


class OrderHeaderNote(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, note_id) found, that is not supported. The first column is selected.
    note = models.ForeignKey(NoteData, models.DO_NOTHING)
    internal_note = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_header_note'
        unique_together = (('order', 'note'),)


class OrderHeaderWorkEffort(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, work_effort_id) found, that is not supported. The first column is selected.
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_header_work_effort'
        unique_together = (('order', 'work_effort'),)


class OrderItem(models.Model):
    order = models.OneToOneField('OrderItemGroup', models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    order_item_type = models.ForeignKey('OrderItemType', models.DO_NOTHING, blank=True, null=True)
    order_item_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    is_item_group_primary = models.CharField(max_length=1, blank=True, null=True)
    from_inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING, blank=True, null=True)
    budget_id = models.CharField(max_length=20, blank=True, null=True)
    budget_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    supplier_product_id = models.CharField(max_length=60, blank=True, null=True)
    product_feature_id = models.CharField(max_length=20, blank=True, null=True)
    prod_catalog_id = models.CharField(max_length=20, blank=True, null=True)
    product_category_id = models.CharField(max_length=20, blank=True, null=True)
    is_promo = models.CharField(max_length=1, blank=True, null=True)
    quote = models.ForeignKey('QuoteItem', models.DO_NOTHING, blank=True, null=True)
    quote_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    shopping_list_id = models.CharField(max_length=20, blank=True, null=True)
    shopping_list_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    subscription_id = models.CharField(max_length=20, blank=True, null=True)
    deployment_id = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cancel_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    selected_amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    unit_list_price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    unit_average_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unit_recurring_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    is_modified_price = models.CharField(max_length=1, blank=True, null=True)
    recurring_freq_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    item_description = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    corresponding_po_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    sync_status = models.ForeignKey('StatusItem', models.DO_NOTHING, related_name='orderitem_sync_status_set', blank=True, null=True)
    estimated_ship_date = models.DateTimeField(blank=True, null=True)
    estimated_delivery_date = models.DateTimeField(blank=True, null=True)
    auto_cancel_date = models.DateTimeField(blank=True, null=True)
    dont_cancel_set_date = models.DateTimeField(blank=True, null=True)
    dont_cancel_set_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='dont_cancel_set_user_login', blank=True, null=True)
    ship_before_date = models.DateTimeField(blank=True, null=True)
    ship_after_date = models.DateTimeField(blank=True, null=True)
    cancel_back_order_date = models.DateTimeField(blank=True, null=True)
    override_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    sales_opportunity = models.ForeignKey('SalesOpportunity', models.DO_NOTHING, blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, related_name='orderitem_change_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item'
        unique_together = (('order', 'order_item_seq_id'),)


class OrderItemAssoc(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, ship_group_seq_id, to_order_id, to_order_item_seq_id, to_ship_group_seq_id, order_item_assoc_type_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    ship_group_seq_id = models.CharField(max_length=20)
    to_order = models.ForeignKey(OrderHeader, models.DO_NOTHING, related_name='orderitemassoc_to_order_set')
    to_order_item_seq_id = models.CharField(max_length=20)
    to_ship_group_seq_id = models.CharField(max_length=20)
    order_item_assoc_type = models.ForeignKey('OrderItemAssocType', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_assoc'
        unique_together = (('order', 'order_item_seq_id', 'ship_group_seq_id', 'to_order', 'to_order_item_seq_id', 'to_ship_group_seq_id', 'order_item_assoc_type'),)


class OrderItemAssocType(models.Model):
    order_item_assoc_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_assoc_type'


class OrderItemAssociation(models.Model):
    sales_order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (sales_order_id, so_item_seq_id, purchase_order_id, po_item_seq_id) found, that is not supported. The first column is selected.
    so_item_seq_id = models.CharField(max_length=20)
    purchase_order = models.ForeignKey(OrderHeader, models.DO_NOTHING, related_name='orderitemassociation_purchase_order_set')
    po_item_seq_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_association'
        unique_together = (('sales_order', 'so_item_seq_id', 'purchase_order', 'po_item_seq_id'),)


class OrderItemAttribute(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, attr_name) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_attribute'
        unique_together = (('order', 'order_item_seq_id', 'attr_name'),)


class OrderItemBilling(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, invoice_id, invoice_item_seq_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    invoice = models.ForeignKey(InvoiceItem, models.DO_NOTHING)
    invoice_item_seq_id = models.CharField(max_length=20)
    item_issuance = models.ForeignKey(ItemIssuance, models.DO_NOTHING, blank=True, null=True)
    shipment_receipt = models.ForeignKey('ShipmentReceipt', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_billing'
        unique_together = (('order', 'order_item_seq_id', 'invoice', 'invoice_item_seq_id'),)


class OrderItemChange(models.Model):
    order_item_change_id = models.CharField(primary_key=True, max_length=20)
    order = models.ForeignKey(OrderItem, models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    change_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    change_datetime = models.DateTimeField(blank=True, null=True)
    change_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='change_user_login', blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cancel_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    item_description = models.CharField(max_length=255, blank=True, null=True)
    reason_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='orderitemchange_reason_enum_set', blank=True, null=True)
    change_comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_change'


class OrderItemContactMech(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, contact_mech_purpose_type_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    contact_mech_purpose_type = models.ForeignKey(ContactMechPurposeType, models.DO_NOTHING)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_contact_mech'
        unique_together = (('order', 'order_item_seq_id', 'contact_mech_purpose_type'),)


class OrderItemGroup(models.Model):
    order = models.OneToOneField('self', models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_group_seq_id) found, that is not supported. The first column is selected.
    order_item_group_seq_id = models.CharField(max_length=20)
    parent_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_group'
        unique_together = (('order', 'order_item_group_seq_id'),)


class OrderItemGroupOrder(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, group_order_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    group_order = models.ForeignKey('ProductGroupOrder', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_group_order'
        unique_together = (('order', 'order_item_seq_id', 'group_order'),)


class OrderItemInventoryRes(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, inventory_item_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING)
    reserve_order_enum_id = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    quantity_not_available = models.FloatField(blank=True, null=True)
    reserved_datetime = models.DateTimeField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    promised_datetime = models.DateTimeField(blank=True, null=True)
    current_promised_date = models.DateTimeField(blank=True, null=True)
    pick_start_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_inventory_res'
        unique_together = (('order', 'order_item_seq_id', 'inventory_item'),)


class OrderItemPriceInfo(models.Model):
    order_item_price_info_id = models.CharField(primary_key=True, max_length=20)
    order = models.ForeignKey(OrderItem, models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    product_price_rule = models.ForeignKey('ProductPriceAction', models.DO_NOTHING, blank=True, null=True)
    product_price_action_seq_id = models.CharField(max_length=20, blank=True, null=True)
    modify_amount = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    rate_code = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_price_info'


class OrderItemRole(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_role'
        unique_together = (('order', 'order_item_seq_id', 'party', 'role_type_id'),)


class OrderItemShipGroup(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, ship_group_seq_id) found, that is not supported. The first column is selected.
    ship_group_seq_id = models.CharField(max_length=20)
    shipment_method_type = models.ForeignKey('ShipmentMethodType', models.DO_NOTHING, blank=True, null=True)
    supplier_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    vendor_party = models.ForeignKey('Party', models.DO_NOTHING, related_name='orderitemshipgroup_vendor_party_set', blank=True, null=True)
    carrier_party = models.ForeignKey('Party', models.DO_NOTHING, related_name='orderitemshipgroup_carrier_party_set', blank=True, null=True)
    carrier_role_type_id = models.CharField(max_length=20, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    contact_mech = models.ForeignKey('PostalAddress', models.DO_NOTHING, blank=True, null=True)
    telecom_contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    tracking_number = models.CharField(max_length=60, blank=True, null=True)
    shipping_instructions = models.CharField(max_length=255, blank=True, null=True)
    may_split = models.CharField(max_length=1, blank=True, null=True)
    gift_message = models.CharField(max_length=255, blank=True, null=True)
    is_gift = models.CharField(max_length=1, blank=True, null=True)
    ship_after_date = models.DateTimeField(blank=True, null=True)
    ship_by_date = models.DateTimeField(blank=True, null=True)
    estimated_ship_date = models.DateTimeField(blank=True, null=True)
    estimated_delivery_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_ship_group'
        unique_together = (('order', 'ship_group_seq_id'),)


class OrderItemShipGroupAssoc(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, ship_group_seq_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    ship_group_seq_id = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cancel_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_ship_group_assoc'
        unique_together = (('order', 'order_item_seq_id', 'ship_group_seq_id'),)


class OrderItemShipGrpInvRes(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, ship_group_seq_id, order_item_seq_id, inventory_item_id) found, that is not supported. The first column is selected.
    ship_group_seq_id = models.CharField(max_length=20)
    order_item_seq_id = models.CharField(max_length=20)
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING)
    reserve_order_enum_id = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_not_available = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserved_datetime = models.DateTimeField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    promised_datetime = models.DateTimeField(blank=True, null=True)
    current_promised_date = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=1, blank=True, null=True)
    sequence_id = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    pick_start_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_ship_grp_inv_res'
        unique_together = (('order', 'ship_group_seq_id', 'order_item_seq_id', 'inventory_item'),)


class OrderItemType(models.Model):
    order_item_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_type'


class OrderItemTypeAttr(models.Model):
    order_item_type = models.OneToOneField(OrderItemType, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_item_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_type_attr'
        unique_together = (('order_item_type', 'attr_name'),)


class OrderNotification(models.Model):
    order_notification_id = models.CharField(primary_key=True, max_length=20)
    order = models.ForeignKey(OrderHeader, models.DO_NOTHING, blank=True, null=True)
    email_type = models.ForeignKey(Enumeration, models.DO_NOTHING, db_column='email_type', blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    notification_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_notification'


class OrderPaymentPreference(models.Model):
    order_payment_preference_id = models.CharField(primary_key=True, max_length=20)
    order = models.ForeignKey(OrderHeader, models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    ship_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    product_price_purpose = models.ForeignKey('ProductPricePurpose', models.DO_NOTHING, blank=True, null=True)
    payment_method_type = models.ForeignKey('PaymentMethodType', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, blank=True, null=True)
    fin_account = models.ForeignKey(FinAccount, models.DO_NOTHING, blank=True, null=True)
    security_code = models.CharField(max_length=255, blank=True, null=True)
    track2 = models.CharField(max_length=255, blank=True, null=True)
    present_flag = models.CharField(max_length=1, blank=True, null=True)
    swiped_flag = models.CharField(max_length=1, blank=True, null=True)
    overflow_flag = models.CharField(max_length=1, blank=True, null=True)
    max_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    process_attempt = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    billing_postal_code = models.CharField(max_length=60, blank=True, null=True)
    manual_auth_code = models.CharField(max_length=60, blank=True, null=True)
    manual_ref_num = models.CharField(max_length=60, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    needs_nsf_retry = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_payment_preference'


class OrderProductPromoCode(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, product_promo_code_id) found, that is not supported. The first column is selected.
    product_promo_code = models.ForeignKey('ProductPromoCode', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_product_promo_code'
        unique_together = (('order', 'product_promo_code'),)


class OrderRequirementCommitment(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, requirement_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    requirement = models.ForeignKey('Requirement', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_requirement_commitment'
        unique_together = (('order', 'order_item_seq_id', 'requirement'),)


class OrderRole(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_role'
        unique_together = (('order', 'party', 'role_type_id'),)


class OrderShipment(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, ship_group_seq_id, shipment_id, shipment_item_seq_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    ship_group_seq_id = models.CharField(max_length=20)
    shipment = models.ForeignKey('Shipment', models.DO_NOTHING)
    shipment_item_seq_id = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_shipment'
        unique_together = (('order', 'order_item_seq_id', 'ship_group_seq_id', 'shipment', 'shipment_item_seq_id'),)


class OrderShipmentPreference(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    shipment_method_type = models.ForeignKey('ShipmentMethodType', models.DO_NOTHING, blank=True, null=True)
    carrier_party = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    carrier_role_type_id = models.CharField(max_length=20, blank=True, null=True)
    tracking_number = models.CharField(max_length=60, blank=True, null=True)
    shipping_instructions = models.CharField(max_length=255, blank=True, null=True)
    may_split = models.CharField(max_length=1, blank=True, null=True)
    gift_message = models.CharField(max_length=255, blank=True, null=True)
    is_gift = models.CharField(max_length=1, blank=True, null=True)
    ship_after_date = models.DateTimeField(blank=True, null=True)
    ship_before_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_shipment_preference'
        unique_together = (('order', 'order_item_seq_id'),)


class OrderStatus(models.Model):
    order_status_id = models.CharField(primary_key=True, max_length=20)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(OrderHeader, models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    order_payment_preference_id = models.CharField(max_length=20, blank=True, null=True)
    status_datetime = models.DateTimeField(blank=True, null=True)
    status_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='status_user_login', blank=True, null=True)
    change_reason = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_status'


class OrderSummaryEntry(models.Model):
    entry_date = models.DateField(primary_key=True)  # The composite primary key (entry_date, product_id, facility_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    total_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    gross_sales = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    product_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_summary_entry'
        unique_together = (('entry_date', 'product', 'facility'),)


class OrderTerm(models.Model):
    term_type = models.OneToOneField('TermType', models.DO_NOTHING, primary_key=True)  # The composite primary key (term_type_id, order_id, order_item_seq_id) found, that is not supported. The first column is selected.
    order = models.ForeignKey(OrderHeader, models.DO_NOTHING)
    order_item_seq_id = models.CharField(max_length=20)
    term_value = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    term_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    text_value = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_term'
        unique_together = (('term_type', 'order', 'order_item_seq_id'),)


class OrderTermAttribute(models.Model):
    term_type = models.OneToOneField(OrderTerm, models.DO_NOTHING, primary_key=True)  # The composite primary key (term_type_id, order_id, order_item_seq_id, attr_name) found, that is not supported. The first column is selected.
    order_id = models.CharField(max_length=20)
    order_item_seq_id = models.CharField(max_length=20)
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_term_attribute'
        unique_together = (('term_type', 'order_id', 'order_item_seq_id', 'attr_name'),)


class OrderType(models.Model):
    order_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_type'


class OrderTypeAttr(models.Model):
    order_type = models.OneToOneField(OrderType, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_type_attr'
        unique_together = (('order_type', 'attr_name'),)


class OtherDataResource(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)
    data_resource_content = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_data_resource'


class Party(models.Model):
    party_id = models.CharField(primary_key=True, max_length=20)
    party_type = models.ForeignKey('PartyType', models.DO_NOTHING, blank=True, null=True)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    preferred_currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='party_last_modified_by_user_login_set', blank=True, null=True)
    data_source = models.ForeignKey(DataSource, models.DO_NOTHING, blank=True, null=True)
    is_unread = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party'


class PartyAcctgPreference(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)
    fiscal_year_start_month = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    fiscal_year_start_day = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    tax_form = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    cogs_method = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='partyacctgpreference_cogs_method_set', blank=True, null=True)
    base_currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    invoice_seq_cust_meth = models.ForeignKey(CustomMethod, models.DO_NOTHING, blank=True, null=True)
    invoice_id_prefix = models.CharField(max_length=10, blank=True, null=True)
    last_invoice_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_invoice_restart_date = models.DateTimeField(blank=True, null=True)
    use_invoice_id_for_returns = models.CharField(max_length=1, blank=True, null=True)
    quote_seq_cust_meth = models.ForeignKey(CustomMethod, models.DO_NOTHING, related_name='partyacctgpreference_quote_seq_cust_meth_set', blank=True, null=True)
    quote_id_prefix = models.CharField(max_length=10, blank=True, null=True)
    last_quote_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    order_seq_cust_meth = models.ForeignKey(CustomMethod, models.DO_NOTHING, related_name='partyacctgpreference_order_seq_cust_meth_set', blank=True, null=True)
    order_id_prefix = models.CharField(max_length=10, blank=True, null=True)
    last_order_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    refund_payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, blank=True, null=True)
    error_gl_journal = models.ForeignKey(GlJournal, models.DO_NOTHING, blank=True, null=True)
    invoice_sequence_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='partyacctgpreference_invoice_sequence_enum_set', blank=True, null=True)
    order_sequence_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='partyacctgpreference_order_sequence_enum_set', blank=True, null=True)
    quote_sequence_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='partyacctgpreference_quote_sequence_enum_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_acctg_preference'


class PartyAttribute(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_attribute'
        unique_together = (('party', 'attr_name'),)


class PartyBenefit(models.Model):
    role_type_id_from = models.CharField(primary_key=True, max_length=20)  # The composite primary key (role_type_id_from, role_type_id_to, party_id_from, party_id_to, benefit_type_id, from_date) found, that is not supported. The first column is selected.
    role_type_id_to = models.CharField(max_length=20)
    party_id_from = models.ForeignKey(Party, models.DO_NOTHING, db_column='party_id_from')
    party_id_to = models.ForeignKey(Party, models.DO_NOTHING, db_column='party_id_to', related_name='partybenefit_party_id_to_set')
    benefit_type = models.ForeignKey(BenefitType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    period_type_id = models.CharField(max_length=20, blank=True, null=True)
    cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_employer_paid_percent = models.FloatField(blank=True, null=True)
    available_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_benefit'
        unique_together = (('role_type_id_from', 'role_type_id_to', 'party_id_from', 'party_id_to', 'benefit_type', 'from_date'),)


class PartyCarrierAccount(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, carrier_party_id, from_date) found, that is not supported. The first column is selected.
    carrier_party = models.ForeignKey(Party, models.DO_NOTHING, related_name='partycarrieraccount_carrier_party_set')
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_carrier_account'
        unique_together = (('party', 'carrier_party', 'from_date'),)


class PartyClassification(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, party_classification_group_id, from_date) found, that is not supported. The first column is selected.
    party_classification_group = models.ForeignKey('PartyClassificationGroup', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_classification'
        unique_together = (('party', 'party_classification_group', 'from_date'),)


class PartyClassificationGroup(models.Model):
    party_classification_group_id = models.CharField(primary_key=True, max_length=20)
    party_classification_type = models.ForeignKey('PartyClassificationType', models.DO_NOTHING, blank=True, null=True)
    parent_group = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_classification_group'


class PartyClassificationType(models.Model):
    party_classification_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_classification_type'


class PartyContactMech(models.Model):
    party = models.OneToOneField('PartyRole', models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, contact_mech_id, from_date) found, that is not supported. The first column is selected.
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING, blank=True, null=True)
    allow_solicitation = models.CharField(max_length=1, blank=True, null=True)
    extension = models.CharField(max_length=255, blank=True, null=True)
    verified = models.CharField(max_length=1, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    years_with_contact_mech = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    months_with_contact_mech = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_contact_mech'
        unique_together = (('party', 'contact_mech', 'from_date'),)


class PartyContactMechPurpose(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, contact_mech_id, contact_mech_purpose_type_id, from_date) found, that is not supported. The first column is selected.
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    contact_mech_purpose_type = models.ForeignKey(ContactMechPurposeType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_contact_mech_purpose'
        unique_together = (('party', 'contact_mech', 'contact_mech_purpose_type', 'from_date'),)


class PartyContent(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, content_id, party_content_type_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    party_content_type = models.ForeignKey('PartyContentType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_content'
        unique_together = (('party', 'content', 'party_content_type', 'from_date'),)


class PartyContentType(models.Model):
    party_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_content_type'


class PartyDataSource(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, data_source_id, from_date) found, that is not supported. The first column is selected.
    data_source = models.ForeignKey(DataSource, models.DO_NOTHING)
    from_date = models.DateTimeField()
    visit_id = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    is_create = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_data_source'
        unique_together = (('party', 'data_source', 'from_date'),)


class PartyFixedAssetAssignment(models.Model):
    party = models.OneToOneField('PartyRole', models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, role_type_id, fixed_asset_id, from_date) found, that is not supported. The first column is selected.
    role_type_id = models.CharField(max_length=20)
    fixed_asset = models.ForeignKey(FixedAsset, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    allocated_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_fixed_asset_assignment'
        unique_together = (('party', 'role_type_id', 'fixed_asset', 'from_date'),)


class PartyGeoPoint(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, geo_point_id, from_date) found, that is not supported. The first column is selected.
    geo_point = models.ForeignKey(GeoPoint, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_geo_point'
        unique_together = (('party', 'geo_point', 'from_date'),)


class PartyGlAccount(models.Model):
    organization_party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (organization_party_id, party_id, role_type_id, gl_account_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey('PartyRole', models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    gl_account_type = models.ForeignKey(GlAccountType, models.DO_NOTHING)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_gl_account'
        unique_together = (('organization_party', 'party', 'role_type_id', 'gl_account_type'),)


class PartyGroup(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    group_name_local = models.CharField(max_length=100, blank=True, null=True)
    office_site_name = models.CharField(max_length=100, blank=True, null=True)
    annual_revenue = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    num_employees = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    ticker_symbol = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    logo_image_url = models.CharField(max_length=2000, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_group'


class PartyIcsAvsOverride(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)
    avs_decline_string = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_ics_avs_override'


class PartyIdentification(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, party_identification_type_id) found, that is not supported. The first column is selected.
    party_identification_type = models.ForeignKey('PartyIdentificationType', models.DO_NOTHING)
    id_value = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_identification'
        unique_together = (('party', 'party_identification_type'),)


class PartyIdentificationType(models.Model):
    party_identification_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_identification_type'


class PartyInvitation(models.Model):
    party_invitation_id = models.CharField(primary_key=True, max_length=20)
    party_id_from = models.ForeignKey(Party, models.DO_NOTHING, db_column='party_id_from', blank=True, null=True)
    party_id = models.CharField(max_length=20, blank=True, null=True)
    to_name = models.CharField(max_length=100, blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    last_invite_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_invitation'


class PartyInvitationGroupAssoc(models.Model):
    party_invitation = models.OneToOneField(PartyInvitation, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_invitation_id, party_id_to) found, that is not supported. The first column is selected.
    party_id_to = models.ForeignKey(Party, models.DO_NOTHING, db_column='party_id_to')
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_invitation_group_assoc'
        unique_together = (('party_invitation', 'party_id_to'),)


class PartyInvitationRoleAssoc(models.Model):
    party_invitation = models.OneToOneField(PartyInvitation, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_invitation_id, role_type_id) found, that is not supported. The first column is selected.
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_invitation_role_assoc'
        unique_together = (('party_invitation', 'role_type'),)


class PartyNameHistory(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, change_date) found, that is not supported. The first column is selected.
    change_date = models.DateTimeField()
    group_name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    personal_title = models.CharField(max_length=100, blank=True, null=True)
    suffix = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_name_history'
        unique_together = (('party', 'change_date'),)


class PartyNeed(models.Model):
    party_need_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (party_need_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(Party, models.DO_NOTHING)
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING)
    party_type = models.ForeignKey('PartyType', models.DO_NOTHING, blank=True, null=True)
    need_type = models.ForeignKey(NeedType, models.DO_NOTHING, blank=True, null=True)
    communication_event = models.ForeignKey(CommunicationEvent, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    visit_id = models.CharField(max_length=20, blank=True, null=True)
    datetime_recorded = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_need'
        unique_together = (('party_need_id', 'party', 'role_type'),)


class PartyNote(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, note_id) found, that is not supported. The first column is selected.
    note = models.ForeignKey(NoteData, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_note'
        unique_together = (('party', 'note'),)


class PartyProfileDefault(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, product_store_id) found, that is not supported. The first column is selected.
    product_store = models.ForeignKey('ProductStore', models.DO_NOTHING)
    default_ship_addr = models.CharField(max_length=20, blank=True, null=True)
    default_bill_addr = models.CharField(max_length=20, blank=True, null=True)
    default_pay_meth = models.CharField(max_length=20, blank=True, null=True)
    default_ship_meth = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_profile_default'
        unique_together = (('party', 'product_store'),)


class PartyQual(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, party_qual_type_id, from_date) found, that is not supported. The first column is selected.
    party_qual_type = models.ForeignKey('PartyQualType', models.DO_NOTHING)
    qualification_desc = models.CharField(max_length=60, blank=True, null=True)
    title = models.CharField(max_length=60, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    verif_status = models.ForeignKey('StatusItem', models.DO_NOTHING, related_name='partyqual_verif_status_set', blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_qual'
        unique_together = (('party', 'party_qual_type', 'from_date'),)


class PartyQualType(models.Model):
    party_qual_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_qual_type'


class PartyRate(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, rate_type_id, currency_uom_id, from_date) found, that is not supported. The first column is selected.
    rate_type = models.ForeignKey('RateType', models.DO_NOTHING)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING)
    default_rate = models.CharField(max_length=1, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_rate'
        unique_together = (('party', 'rate_type', 'currency_uom', 'from_date'),)


class PartyRateNew(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, rate_type_id, from_date) found, that is not supported. The first column is selected.
    rate_type = models.ForeignKey('RateType', models.DO_NOTHING)
    default_rate = models.CharField(max_length=1, blank=True, null=True)
    percentage_used = models.FloatField(blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_rate_new'
        unique_together = (('party', 'rate_type', 'from_date'),)


class PartyRelationship(models.Model):
    party_id_from = models.OneToOneField('PartyRole', models.DO_NOTHING, db_column='party_id_from', primary_key=True)  # The composite primary key (party_id_from, party_id_to, role_type_id_from, role_type_id_to, from_date) found, that is not supported. The first column is selected.
    party_id_to = models.ForeignKey('PartyRole', models.DO_NOTHING, db_column='party_id_to', related_name='partyrelationship_party_id_to_set')
    role_type_id_from = models.CharField(max_length=20)
    role_type_id_to = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    relationship_name = models.CharField(max_length=100, blank=True, null=True)
    security_group = models.ForeignKey('SecurityGroup', models.DO_NOTHING, blank=True, null=True)
    priority_type = models.ForeignKey('PriorityType', models.DO_NOTHING, blank=True, null=True)
    party_relationship_type = models.ForeignKey('PartyRelationshipType', models.DO_NOTHING, blank=True, null=True)
    permissions_enum_id = models.CharField(max_length=20, blank=True, null=True)
    position_title = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_relationship'
        unique_together = (('party_id_from', 'party_id_to', 'role_type_id_from', 'role_type_id_to', 'from_date'),)


class PartyRelationshipType(models.Model):
    party_relationship_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    party_relationship_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    role_type_id_valid_from = models.ForeignKey('RoleType', models.DO_NOTHING, db_column='role_type_id_valid_from', blank=True, null=True)
    role_type_id_valid_to = models.ForeignKey('RoleType', models.DO_NOTHING, db_column='role_type_id_valid_to', related_name='partyrelationshiptype_role_type_id_valid_to_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_relationship_type'


class PartyResume(models.Model):
    resume_id = models.CharField(primary_key=True, max_length=20)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    content_id = models.CharField(max_length=20, blank=True, null=True)
    resume_date = models.DateTimeField(blank=True, null=True)
    resume_text = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_resume'


class PartyRole(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, role_type_id) found, that is not supported. The first column is selected.
    role_type = models.ForeignKey('RoleType', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_role'
        unique_together = (('party', 'role_type'),)


class PartySkill(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, skill_type_id) found, that is not supported. The first column is selected.
    skill_type = models.ForeignKey('SkillType', models.DO_NOTHING)
    years_experience = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    rating = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    skill_level = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    started_using_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_skill'
        unique_together = (('party', 'skill_type'),)


class PartyStatus(models.Model):
    status = models.OneToOneField('StatusItem', models.DO_NOTHING, primary_key=True)  # The composite primary key (status_id, party_id, status_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey(Party, models.DO_NOTHING)
    status_date = models.DateTimeField()
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_status'
        unique_together = (('status', 'party', 'status_date'),)


class PartyTaxAuthInfo(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, tax_auth_geo_id, tax_auth_party_id, from_date) found, that is not supported. The first column is selected.
    tax_auth_geo = models.ForeignKey('TaxAuthority', models.DO_NOTHING)
    tax_auth_party_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    party_tax_id = models.CharField(max_length=60, blank=True, null=True)
    is_exempt = models.CharField(max_length=1, blank=True, null=True)
    is_nexus = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_tax_auth_info'
        unique_together = (('party', 'tax_auth_geo', 'tax_auth_party_id', 'from_date'),)


class PartyTaxInfo(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, geo_id, from_date) found, that is not supported. The first column is selected.
    geo = models.ForeignKey(Geo, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    party_tax_id = models.CharField(max_length=60, blank=True, null=True)
    is_exempt = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_tax_info'
        unique_together = (('party', 'geo', 'from_date'),)


class PartyType(models.Model):
    party_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_type'


class PartyTypeAttr(models.Model):
    party_type = models.OneToOneField(PartyType, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_type_attr'
        unique_together = (('party_type', 'attr_name'),)


class PayGrade(models.Model):
    pay_grade_id = models.CharField(primary_key=True, max_length=20)
    pay_grade_name = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_grade'


class PayHistory(models.Model):
    role_type_id_from = models.OneToOneField(Employment, models.DO_NOTHING, db_column='role_type_id_from', primary_key=True)  # The composite primary key (role_type_id_from, role_type_id_to, party_id_from, party_id_to, from_date) found, that is not supported. The first column is selected.
    role_type_id_to = models.CharField(max_length=20)
    party_id_from = models.CharField(max_length=20)
    party_id_to = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    salary_step_seq_id = models.CharField(max_length=20, blank=True, null=True)
    pay_grade = models.ForeignKey(PayGrade, models.DO_NOTHING, blank=True, null=True)
    period_type = models.ForeignKey('PeriodType', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_history'
        unique_together = (('role_type_id_from', 'role_type_id_to', 'party_id_from', 'party_id_to', 'from_date'),)


class PayPalPaymentMethod(models.Model):
    payment_method = models.OneToOneField('PaymentMethod', models.DO_NOTHING, primary_key=True)
    payer_id = models.CharField(max_length=20, blank=True, null=True)
    express_checkout_token = models.CharField(max_length=60, blank=True, null=True)
    payer_status = models.CharField(max_length=60, blank=True, null=True)
    avs_addr = models.CharField(max_length=1, blank=True, null=True)
    avs_zip = models.CharField(max_length=1, blank=True, null=True)
    correlation_id = models.CharField(max_length=20, blank=True, null=True)
    contact_mech = models.ForeignKey('PostalAddress', models.DO_NOTHING, blank=True, null=True)
    transaction_id = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_pal_payment_method'


class Payment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=20)
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING, blank=True, null=True)
    payment_method_type = models.ForeignKey('PaymentMethodType', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, blank=True, null=True)
    payment_gateway_response = models.ForeignKey('PaymentGatewayResponse', models.DO_NOTHING, blank=True, null=True)
    payment_preference = models.ForeignKey(OrderPaymentPreference, models.DO_NOTHING, blank=True, null=True)
    party_id_from = models.ForeignKey(Party, models.DO_NOTHING, db_column='party_id_from', blank=True, null=True)
    party_id_to = models.ForeignKey(Party, models.DO_NOTHING, db_column='party_id_to', related_name='payment_party_id_to_set', blank=True, null=True)
    role_type_id_to = models.ForeignKey('RoleType', models.DO_NOTHING, db_column='role_type_id_to', blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    payment_ref_num = models.CharField(max_length=60, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    fin_account_trans = models.ForeignKey(FinAccountTrans, models.DO_NOTHING, blank=True, null=True)
    override_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    actual_currency_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='payment_actual_currency_uom_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentApplication(models.Model):
    payment_application_id = models.CharField(primary_key=True, max_length=20)
    payment = models.ForeignKey(Payment, models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)
    invoice_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    billing_account = models.ForeignKey(BillingAccount, models.DO_NOTHING, blank=True, null=True)
    override_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    to_payment = models.ForeignKey(Payment, models.DO_NOTHING, related_name='paymentapplication_to_payment_set', blank=True, null=True)
    tax_auth_geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    amount_applied = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_application'


class PaymentAttribute(models.Model):
    payment = models.OneToOneField(Payment, models.DO_NOTHING, primary_key=True)  # The composite primary key (payment_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_attribute'
        unique_together = (('payment', 'attr_name'),)


class PaymentBudgetAllocation(models.Model):
    budget = models.OneToOneField(Budget, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, budget_item_seq_id, payment_id) found, that is not supported. The first column is selected.
    budget_item_seq_id = models.CharField(max_length=20)
    payment = models.ForeignKey(Payment, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_budget_allocation'
        unique_together = (('budget', 'budget_item_seq_id', 'payment'),)


class PaymentContent(models.Model):
    payment = models.ForeignKey(Payment, models.DO_NOTHING)
    payment_content_type = models.ForeignKey('PaymentContentType', models.DO_NOTHING)
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)  # The composite primary key (content_id, payment_id, payment_content_type_id, from_date) found, that is not supported. The first column is selected.
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_content'
        unique_together = (('content', 'payment', 'payment_content_type', 'from_date'),)


class PaymentContentType(models.Model):
    payment_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_content_type'


class PaymentGatewayAuthorizeNet(models.Model):
    payment_gateway_config = models.OneToOneField('PaymentGatewayConfig', models.DO_NOTHING, primary_key=True)
    transaction_url = models.CharField(max_length=255, blank=True, null=True)
    certificate_alias = models.CharField(max_length=255, blank=True, null=True)
    api_version = models.CharField(max_length=60, blank=True, null=True)
    delimited_data = models.CharField(max_length=60, blank=True, null=True)
    delimiter_char = models.CharField(max_length=60, blank=True, null=True)
    cp_version = models.CharField(max_length=60, blank=True, null=True)
    cp_market_type = models.CharField(max_length=60, blank=True, null=True)
    cp_device_type = models.CharField(max_length=60, blank=True, null=True)
    method = models.CharField(max_length=60, blank=True, null=True)
    email_customer = models.CharField(max_length=60, blank=True, null=True)
    email_merchant = models.CharField(max_length=60, blank=True, null=True)
    test_mode = models.CharField(max_length=60, blank=True, null=True)
    relay_response = models.CharField(max_length=60, blank=True, null=True)
    tran_key = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    pwd = models.CharField(max_length=255, blank=True, null=True)
    trans_description = models.CharField(max_length=255, blank=True, null=True)
    duplicate_window = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_authorize_net'


class PaymentGatewayClearCommerce(models.Model):
    payment_gateway_config = models.OneToOneField('PaymentGatewayConfig', models.DO_NOTHING, primary_key=True)
    source_id = models.CharField(max_length=60, blank=True, null=True)
    group_id = models.CharField(max_length=60, blank=True, null=True)
    client_id = models.CharField(max_length=60, blank=True, null=True)
    username = models.CharField(max_length=60, blank=True, null=True)
    pwd = models.CharField(max_length=255, blank=True, null=True)
    user_alias = models.CharField(max_length=60, blank=True, null=True)
    effective_alias = models.CharField(max_length=60, blank=True, null=True)
    process_mode = models.CharField(max_length=1, blank=True, null=True)
    server_u_r_l = models.CharField(max_length=255, blank=True, null=True)
    enable_c_v_m = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_clear_commerce'


class PaymentGatewayConfig(models.Model):
    payment_gateway_config_id = models.CharField(primary_key=True, max_length=20)
    payment_gateway_config_type = models.ForeignKey('PaymentGatewayConfigType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_config'


class PaymentGatewayConfigType(models.Model):
    payment_gateway_config_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_config_type'


class PaymentGatewayCyberSource(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    api_version = models.CharField(max_length=60, blank=True, null=True)
    production = models.CharField(max_length=60, blank=True, null=True)
    keys_dir = models.CharField(max_length=255, blank=True, null=True)
    keys_file = models.CharField(max_length=255, blank=True, null=True)
    log_enabled = models.CharField(max_length=60, blank=True, null=True)
    log_dir = models.CharField(max_length=255, blank=True, null=True)
    log_file = models.CharField(max_length=255, blank=True, null=True)
    log_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    merchant_descr = models.CharField(max_length=255, blank=True, null=True)
    merchant_contact = models.CharField(max_length=255, blank=True, null=True)
    auto_bill = models.CharField(max_length=60, blank=True, null=True)
    enable_dav = models.CharField(max_length=1, blank=True, null=True)
    fraud_score = models.CharField(max_length=1, blank=True, null=True)
    ignore_avs = models.CharField(max_length=60, blank=True, null=True)
    disable_bill_avs = models.CharField(max_length=1, blank=True, null=True)
    avs_decline_codes = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_cyber_source'


class PaymentGatewayEway(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    refund_pwd = models.CharField(max_length=255, blank=True, null=True)
    test_mode = models.CharField(max_length=60, blank=True, null=True)
    enable_cvn = models.CharField(max_length=60, blank=True, null=True)
    enable_beagle = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_eway'


class PaymentGatewayOrbital(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    username = models.CharField(max_length=60, blank=True, null=True)
    connection_password = models.CharField(max_length=255, blank=True, null=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    engine_class = models.CharField(max_length=255, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)
    port = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    host_name_failover = models.CharField(max_length=255, blank=True, null=True)
    port_failover = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    connection_timeout_seconds = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    read_timeout_seconds = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    authorization_u_r_i = models.CharField(max_length=255, blank=True, null=True)
    sdk_version = models.CharField(max_length=60, blank=True, null=True)
    ssl_socket_factory = models.CharField(max_length=60, blank=True, null=True)
    response_type = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_orbital'


class PaymentGatewayPayPal(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    business_email = models.CharField(max_length=255, blank=True, null=True)
    api_user_name = models.CharField(max_length=60, blank=True, null=True)
    api_password = models.CharField(max_length=60, blank=True, null=True)
    api_signature = models.CharField(max_length=60, blank=True, null=True)
    api_environment = models.CharField(max_length=60, blank=True, null=True)
    notify_url = models.CharField(max_length=255, blank=True, null=True)
    return_url = models.CharField(max_length=255, blank=True, null=True)
    cancel_return_url = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    confirm_template = models.CharField(max_length=255, blank=True, null=True)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    confirm_url = models.CharField(max_length=255, blank=True, null=True)
    shipping_callback_url = models.CharField(max_length=2000, blank=True, null=True)
    require_confirmed_shipping = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_pay_pal'


class PaymentGatewayPayflowPro(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    certs_path = models.CharField(max_length=255, blank=True, null=True)
    host_address = models.CharField(max_length=255, blank=True, null=True)
    host_port = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    timeout = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    proxy_address = models.CharField(max_length=255, blank=True, null=True)
    proxy_port = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    proxy_logon = models.CharField(max_length=255, blank=True, null=True)
    proxy_password = models.CharField(max_length=255, blank=True, null=True)
    vendor = models.CharField(max_length=60, blank=True, null=True)
    user_id = models.CharField(max_length=60, blank=True, null=True)
    pwd = models.CharField(max_length=255, blank=True, null=True)
    partner = models.CharField(max_length=60, blank=True, null=True)
    check_avs = models.CharField(max_length=1, blank=True, null=True)
    check_cvv2 = models.CharField(max_length=1, blank=True, null=True)
    pre_auth = models.CharField(max_length=1, blank=True, null=True)
    enable_transmit = models.CharField(max_length=255, blank=True, null=True)
    log_file_name = models.CharField(max_length=255, blank=True, null=True)
    logging_level = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_log_file_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    stack_trace_on = models.CharField(max_length=1, blank=True, null=True)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    return_url = models.CharField(max_length=255, blank=True, null=True)
    cancel_return_url = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_payflow_pro'


class PaymentGatewayRespMsg(models.Model):
    payment_gateway_resp_msg_id = models.CharField(primary_key=True, max_length=20)
    payment_gateway_response = models.ForeignKey('PaymentGatewayResponse', models.DO_NOTHING, blank=True, null=True)
    pgr_message = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_resp_msg'


class PaymentGatewayResponse(models.Model):
    payment_gateway_response_id = models.CharField(primary_key=True, max_length=20)
    payment_service_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    order_payment_preference = models.ForeignKey(OrderPaymentPreference, models.DO_NOTHING, blank=True, null=True)
    payment_method_type = models.ForeignKey('PaymentMethodType', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey('PaymentMethod', models.DO_NOTHING, blank=True, null=True)
    trans_code_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='paymentgatewayresponse_trans_code_enum_set', blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    reference_num = models.CharField(max_length=60, blank=True, null=True)
    alt_reference = models.CharField(max_length=60, blank=True, null=True)
    sub_reference = models.CharField(max_length=60, blank=True, null=True)
    gateway_code = models.CharField(max_length=60, blank=True, null=True)
    gateway_flag = models.CharField(max_length=60, blank=True, null=True)
    gateway_avs_result = models.CharField(max_length=60, blank=True, null=True)
    gateway_cv_result = models.CharField(max_length=60, blank=True, null=True)
    gateway_score_result = models.CharField(max_length=60, blank=True, null=True)
    gateway_message = models.CharField(max_length=255, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)
    result_declined = models.CharField(max_length=1, blank=True, null=True)
    result_nsf = models.CharField(max_length=1, blank=True, null=True)
    result_bad_expire = models.CharField(max_length=1, blank=True, null=True)
    result_bad_card_number = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_response'


class PaymentGatewaySagePay(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    vendor = models.CharField(max_length=60, blank=True, null=True)
    production_host = models.CharField(max_length=60, blank=True, null=True)
    testing_host = models.CharField(max_length=60, blank=True, null=True)
    sage_pay_mode = models.CharField(max_length=60, blank=True, null=True)
    protocol_version = models.CharField(max_length=10, blank=True, null=True)
    authentication_trans_type = models.CharField(max_length=60, blank=True, null=True)
    authentication_url = models.CharField(max_length=255, blank=True, null=True)
    authorise_trans_type = models.CharField(max_length=60, blank=True, null=True)
    authorise_url = models.CharField(max_length=255, blank=True, null=True)
    release_trans_type = models.CharField(max_length=60, blank=True, null=True)
    release_url = models.CharField(max_length=255, blank=True, null=True)
    void_url = models.CharField(max_length=255, blank=True, null=True)
    refund_url = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_sage_pay'


class PaymentGatewaySecurePay(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    pwd = models.CharField(max_length=255, blank=True, null=True)
    server_u_r_l = models.CharField(max_length=255, blank=True, null=True)
    process_timeout = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    enable_amount_round = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_secure_pay'


class PaymentGatewayWorldPay(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    inst_id = models.CharField(max_length=255, blank=True, null=True)
    auth_mode = models.CharField(max_length=1, blank=True, null=True)
    fix_contact = models.CharField(max_length=1, blank=True, null=True)
    hide_contact = models.CharField(max_length=1, blank=True, null=True)
    hide_currency = models.CharField(max_length=1, blank=True, null=True)
    lang_id = models.CharField(max_length=60, blank=True, null=True)
    no_language_menu = models.CharField(max_length=1, blank=True, null=True)
    with_delivery = models.CharField(max_length=1, blank=True, null=True)
    test_mode = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_world_pay'


class PaymentGatewayiDEAL(models.Model):
    payment_gateway_config = models.OneToOneField(PaymentGatewayConfig, models.DO_NOTHING, primary_key=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    merchant_sub_id = models.CharField(max_length=255, blank=True, null=True)
    merchant_return_u_r_l = models.CharField(max_length=255, blank=True, null=True)
    acquirer_u_r_l = models.CharField(max_length=255, blank=True, null=True)
    acquirer_timeout = models.CharField(max_length=255, blank=True, null=True)
    private_cert = models.CharField(max_length=255, blank=True, null=True)
    acquirer_key_store_filename = models.CharField(max_length=255, blank=True, null=True)
    acquirer_key_store_password = models.CharField(max_length=255, blank=True, null=True)
    merchant_key_store_filename = models.CharField(max_length=255, blank=True, null=True)
    merchant_key_store_password = models.CharField(max_length=255, blank=True, null=True)
    expiration_period = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gatewayi_d_e_a_l'


class PaymentGlAccountTypeMap(models.Model):
    payment_type = models.OneToOneField('PaymentType', models.DO_NOTHING, primary_key=True)  # The composite primary key (payment_type_id, organization_party_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey(Party, models.DO_NOTHING)
    gl_account_type = models.ForeignKey(GlAccountType, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gl_account_type_map'
        unique_together = (('payment_type', 'organization_party'),)


class PaymentGroup(models.Model):
    payment_group_id = models.CharField(primary_key=True, max_length=20)
    payment_group_type = models.ForeignKey('PaymentGroupType', models.DO_NOTHING, blank=True, null=True)
    payment_group_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_group'


class PaymentGroupMember(models.Model):
    payment_group = models.OneToOneField(PaymentGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (payment_group_id, payment_id, from_date) found, that is not supported. The first column is selected.
    payment = models.ForeignKey(Payment, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_group_member'
        unique_together = (('payment_group', 'payment', 'from_date'),)


class PaymentGroupType(models.Model):
    payment_group_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_group_type'


class PaymentMethod(models.Model):
    payment_method_id = models.CharField(primary_key=True, max_length=20)
    payment_method_type = models.ForeignKey('PaymentMethodType', models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    fin_account = models.ForeignKey(FinAccount, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_method'


class PaymentMethodType(models.Model):
    payment_method_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    default_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_method_type'


class PaymentMethodTypeGlAccount(models.Model):
    payment_method_type = models.OneToOneField(PaymentMethodType, models.DO_NOTHING, primary_key=True)  # The composite primary key (payment_method_type_id, organization_party_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey(Party, models.DO_NOTHING)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_method_type_gl_account'
        unique_together = (('payment_method_type', 'organization_party'),)


class PaymentType(models.Model):
    payment_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_type'


class PaymentTypeAttr(models.Model):
    payment_type = models.OneToOneField(PaymentType, models.DO_NOTHING, primary_key=True)  # The composite primary key (payment_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_type_attr'
        unique_together = (('payment_type', 'attr_name'),)


class PayrollPreference(models.Model):
    party = models.OneToOneField(PartyRole, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, role_type_id, payroll_preference_seq_id) found, that is not supported. The first column is selected.
    role_type_id = models.CharField(max_length=20)
    payroll_preference_seq_id = models.CharField(max_length=20)
    deduction_type_id = models.CharField(max_length=20, blank=True, null=True)
    payment_method_type_id = models.CharField(max_length=20, blank=True, null=True)
    period_type_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    flat_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    routing_number = models.CharField(max_length=60, blank=True, null=True)
    account_number = models.CharField(max_length=60, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payroll_preference'
        unique_together = (('party', 'role_type_id', 'payroll_preference_seq_id'),)


class PerfRatingType(models.Model):
    perf_rating_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_rating_type'


class PerfReview(models.Model):
    employee_party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (employee_party_id, employee_role_type_id, perf_review_id) found, that is not supported. The first column is selected.
    employee_role_type_id = models.CharField(max_length=20)
    perf_review_id = models.CharField(max_length=20)
    manager_party = models.ForeignKey(Party, models.DO_NOTHING, related_name='perfreview_manager_party_set', blank=True, null=True)
    manager_role_type_id = models.CharField(max_length=20, blank=True, null=True)
    payment = models.ForeignKey(Payment, models.DO_NOTHING, blank=True, null=True)
    empl_position_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_review'
        unique_together = (('employee_party', 'employee_role_type_id', 'perf_review_id'),)


class PerfReviewItem(models.Model):
    employee_party = models.OneToOneField(PerfReview, models.DO_NOTHING, primary_key=True)  # The composite primary key (employee_party_id, employee_role_type_id, perf_review_id, perf_review_item_seq_id) found, that is not supported. The first column is selected.
    employee_role_type_id = models.CharField(max_length=20)
    perf_review_id = models.CharField(max_length=20)
    perf_review_item_seq_id = models.CharField(max_length=20)
    perf_review_item_type_id = models.CharField(max_length=20, blank=True, null=True)
    perf_rating_type_id = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_review_item'
        unique_together = (('employee_party', 'employee_role_type_id', 'perf_review_id', 'perf_review_item_seq_id'),)


class PerfReviewItemType(models.Model):
    perf_review_item_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perf_review_item_type'


class PerformanceNote(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    communication_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance_note'
        unique_together = (('party', 'role_type_id', 'from_date'),)


class PeriodType(models.Model):
    period_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    period_length = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'period_type'


class Person(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)
    salutation = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    personal_title = models.CharField(max_length=100, blank=True, null=True)
    suffix = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    first_name_local = models.CharField(max_length=100, blank=True, null=True)
    middle_name_local = models.CharField(max_length=100, blank=True, null=True)
    last_name_local = models.CharField(max_length=100, blank=True, null=True)
    other_local = models.CharField(max_length=100, blank=True, null=True)
    member_id = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    deceased_date = models.DateField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    mothers_maiden_name = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=1, blank=True, null=True)
    social_security_number = models.CharField(max_length=255, blank=True, null=True)
    passport_number = models.CharField(max_length=255, blank=True, null=True)
    passport_expire_date = models.DateField(blank=True, null=True)
    total_years_work_experience = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    employment_status_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    residence_status_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='person_residence_status_enum_set', blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    years_with_employer = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    months_with_employer = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    existing_customer = models.CharField(max_length=1, blank=True, null=True)
    card_id = models.CharField(unique=True, max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class PersonTraining(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, training_class_type_id, from_date) found, that is not supported. The first column is selected.
    training_request = models.ForeignKey('TrainingRequest', models.DO_NOTHING, blank=True, null=True)
    training_class_type = models.ForeignKey('TrainingClassType', models.DO_NOTHING)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    approver = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    approval_status = models.CharField(max_length=60, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_training'
        unique_together = (('party', 'training_class_type', 'from_date'),)


class PhysicalInventory(models.Model):
    physical_inventory_id = models.CharField(primary_key=True, max_length=20)
    physical_inventory_date = models.DateTimeField(blank=True, null=True)
    party_id = models.CharField(max_length=20, blank=True, null=True)
    general_comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physical_inventory'


class Picklist(models.Model):
    picklist_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    shipment_method_type = models.ForeignKey('ShipmentMethodType', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    picklist_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picklist'


class PicklistBin(models.Model):
    picklist_bin_id = models.CharField(primary_key=True, max_length=20)
    picklist = models.ForeignKey(Picklist, models.DO_NOTHING, blank=True, null=True)
    bin_location_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    primary_order = models.ForeignKey(OrderItemShipGroup, models.DO_NOTHING, blank=True, null=True)
    primary_ship_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picklist_bin'


class PicklistItem(models.Model):
    picklist_bin = models.OneToOneField(PicklistBin, models.DO_NOTHING, primary_key=True)  # The composite primary key (picklist_bin_id, order_id, order_item_seq_id, ship_group_seq_id, inventory_item_id) found, that is not supported. The first column is selected.
    order = models.ForeignKey(OrderItemShipGroup, models.DO_NOTHING)
    order_item_seq_id = models.CharField(max_length=20)
    ship_group_seq_id = models.CharField(max_length=20)
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING)
    item_status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picklist_item'
        unique_together = (('picklist_bin', 'order', 'order_item_seq_id', 'ship_group_seq_id', 'inventory_item'),)


class PicklistRole(models.Model):
    picklist = models.OneToOneField(Picklist, models.DO_NOTHING, primary_key=True)  # The composite primary key (picklist_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='picklistrole_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picklist_role'
        unique_together = (('picklist', 'party', 'role_type_id', 'from_date'),)


class PicklistStatusHistory(models.Model):
    picklist = models.OneToOneField(Picklist, models.DO_NOTHING, primary_key=True)  # The composite primary key (picklist_id, change_date) found, that is not supported. The first column is selected.
    change_date = models.DateTimeField()
    change_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusValidChange', models.DO_NOTHING, blank=True, null=True)
    status_id_to = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='status_id_to', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picklist_status_history'
        unique_together = (('picklist', 'change_date'),)


class PlatformType(models.Model):
    platform_type_id = models.CharField(primary_key=True, max_length=20)
    platform_name = models.CharField(max_length=100, blank=True, null=True)
    platform_version = models.CharField(max_length=10, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform_type'


class PortalPage(models.Model):
    portal_page_id = models.CharField(primary_key=True, max_length=20)
    portal_page_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    owner_user_login_id = models.CharField(max_length=255, blank=True, null=True)
    original_portal_page_id = models.CharField(max_length=20, blank=True, null=True)
    parent_portal_page = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    security_group = models.ForeignKey('SecurityGroup', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    help_content = models.ForeignKey(Content, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_page'


class PortalPageColumn(models.Model):
    portal_page = models.OneToOneField(PortalPage, models.DO_NOTHING, primary_key=True)  # The composite primary key (portal_page_id, column_seq_id) found, that is not supported. The first column is selected.
    column_seq_id = models.CharField(max_length=20)
    column_width_pixels = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    column_width_percentage = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_page_column'
        unique_together = (('portal_page', 'column_seq_id'),)


class PortalPagePortlet(models.Model):
    portal_page = models.OneToOneField(PortalPage, models.DO_NOTHING, primary_key=True)  # The composite primary key (portal_page_id, portal_portlet_id, portlet_seq_id) found, that is not supported. The first column is selected.
    portal_portlet = models.ForeignKey('PortalPortlet', models.DO_NOTHING)
    portlet_seq_id = models.CharField(max_length=20)
    column_seq_id = models.CharField(max_length=20, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_page_portlet'
        unique_together = (('portal_page', 'portal_portlet', 'portlet_seq_id'),)


class PortalPortlet(models.Model):
    portal_portlet_id = models.CharField(primary_key=True, max_length=20)
    portlet_name = models.CharField(max_length=100, blank=True, null=True)
    screen_name = models.CharField(max_length=255, blank=True, null=True)
    screen_location = models.CharField(max_length=255, blank=True, null=True)
    edit_form_name = models.CharField(max_length=255, blank=True, null=True)
    edit_form_location = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    screenshot = models.CharField(max_length=2000, blank=True, null=True)
    security_service_name = models.CharField(max_length=255, blank=True, null=True)
    security_main_action = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_portlet'


class PortletAttribute(models.Model):
    portal_page_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (portal_page_id, portal_portlet_id, portlet_seq_id, attr_name) found, that is not supported. The first column is selected.
    portal_portlet = models.ForeignKey(PortalPortlet, models.DO_NOTHING)
    portlet_seq_id = models.CharField(max_length=20)
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    attr_type = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portlet_attribute'
        unique_together = (('portal_page_id', 'portal_portlet', 'portlet_seq_id', 'attr_name'),)


class PortletCategory(models.Model):
    portlet_category_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portlet_category'


class PortletPortletCategory(models.Model):
    portal_portlet = models.OneToOneField(PortalPortlet, models.DO_NOTHING, primary_key=True)  # The composite primary key (portal_portlet_id, portlet_category_id) found, that is not supported. The first column is selected.
    portlet_category = models.ForeignKey(PortletCategory, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portlet_portlet_category'
        unique_together = (('portal_portlet', 'portlet_category'),)


class PosTerminal(models.Model):
    pos_terminal_id = models.CharField(primary_key=True, max_length=20)
    facility_id = models.CharField(max_length=20, blank=True, null=True)
    push_entity_sync_id = models.CharField(max_length=20, blank=True, null=True)
    terminal_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_terminal'


class PosTerminalInternTx(models.Model):
    pos_terminal_log = models.OneToOneField('PosTerminalLog', models.DO_NOTHING, primary_key=True)
    paid_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    reason_comment = models.CharField(max_length=255, blank=True, null=True)
    reason_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_terminal_intern_tx'


class PosTerminalLog(models.Model):
    pos_terminal_log_id = models.CharField(primary_key=True, max_length=20)
    pos_terminal = models.ForeignKey(PosTerminal, models.DO_NOTHING, blank=True, null=True)
    transaction_id = models.CharField(max_length=20, blank=True, null=True)
    item_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    order = models.ForeignKey(OrderHeader, models.DO_NOTHING, blank=True, null=True)
    return_field = models.ForeignKey('ReturnHeader', models.DO_NOTHING, db_column='return_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    user_login_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    log_start_date_time = models.DateTimeField(blank=True, null=True)
    log_end_date_time = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_terminal_log'


class PosTerminalState(models.Model):
    pos_terminal = models.OneToOneField(PosTerminal, models.DO_NOTHING, primary_key=True)  # The composite primary key (pos_terminal_id, opened_date) found, that is not supported. The first column is selected.
    opened_date = models.DateTimeField()
    closed_date = models.DateTimeField(blank=True, null=True)
    starting_tx_id = models.CharField(max_length=60, blank=True, null=True)
    ending_tx_id = models.CharField(max_length=60, blank=True, null=True)
    opened_by_user_login_id = models.CharField(max_length=255, blank=True, null=True)
    closed_by_user_login_id = models.CharField(max_length=255, blank=True, null=True)
    starting_drawer_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_ending_cash = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_ending_check = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_ending_cc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_ending_gc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_ending_other = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pos_terminal_state'
        unique_together = (('pos_terminal', 'opened_date'),)


class PostalAddress(models.Model):
    contact_mech = models.OneToOneField(ContactMech, models.DO_NOTHING, primary_key=True)
    to_name = models.CharField(max_length=100, blank=True, null=True)
    attn_name = models.CharField(max_length=100, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    house_number_ext = models.CharField(max_length=60, blank=True, null=True)
    directions = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    postal_code = models.CharField(max_length=60, blank=True, null=True)
    postal_code_ext = models.CharField(max_length=60, blank=True, null=True)
    country_geo = models.ForeignKey(Geo, models.DO_NOTHING, related_name='postaladdress_country_geo_set', blank=True, null=True)
    state_province_geo = models.ForeignKey(Geo, models.DO_NOTHING, related_name='postaladdress_state_province_geo_set', blank=True, null=True)
    country_geo = models.ForeignKey(Geo, models.DO_NOTHING, related_name='postaladdress_country_geo_set', blank=True, null=True)
    municipality_geo = models.ForeignKey(Geo, models.DO_NOTHING, related_name='postaladdress_municipality_geo_set', blank=True, null=True)
    postal_code_geo = models.ForeignKey(Geo, models.DO_NOTHING, related_name='postaladdress_postal_code_geo_set', blank=True, null=True)
    geo_point = models.ForeignKey(GeoPoint, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'postal_address'


class PostalAddressBoundary(models.Model):
    contact_mech = models.OneToOneField(PostalAddress, models.DO_NOTHING, primary_key=True)  # The composite primary key (contact_mech_id, geo_id) found, that is not supported. The first column is selected.
    geo = models.ForeignKey(Geo, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'postal_address_boundary'
        unique_together = (('contact_mech', 'geo'),)


class PriorityType(models.Model):
    priority_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'priority_type'


class ProdCatalog(models.Model):
    prod_catalog_id = models.CharField(primary_key=True, max_length=20)
    catalog_name = models.CharField(max_length=100, blank=True, null=True)
    use_quick_add = models.CharField(max_length=1, blank=True, null=True)
    style_sheet = models.CharField(max_length=2000, blank=True, null=True)
    header_logo = models.CharField(max_length=2000, blank=True, null=True)
    content_path_prefix = models.CharField(max_length=255, blank=True, null=True)
    template_path_prefix = models.CharField(max_length=255, blank=True, null=True)
    view_allow_perm_reqd = models.CharField(max_length=1, blank=True, null=True)
    purchase_allow_perm_reqd = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_catalog'


class ProdCatalogCategory(models.Model):
    prod_catalog = models.OneToOneField(ProdCatalog, models.DO_NOTHING, primary_key=True)  # The composite primary key (prod_catalog_id, product_category_id, prod_catalog_category_type_id, from_date) found, that is not supported. The first column is selected.
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING)
    prod_catalog_category_type = models.ForeignKey('ProdCatalogCategoryType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_catalog_category'
        unique_together = (('prod_catalog', 'product_category', 'prod_catalog_category_type', 'from_date'),)


class ProdCatalogCategoryType(models.Model):
    prod_catalog_category_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_catalog_category_type'


class ProdCatalogInvFacility(models.Model):
    prod_catalog = models.OneToOneField(ProdCatalog, models.DO_NOTHING, primary_key=True)  # The composite primary key (prod_catalog_id, facility_id, from_date) found, that is not supported. The first column is selected.
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_catalog_inv_facility'
        unique_together = (('prod_catalog', 'facility', 'from_date'),)


class ProdCatalogRole(models.Model):
    party = models.OneToOneField(PartyRole, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, role_type_id, prod_catalog_id, from_date) found, that is not supported. The first column is selected.
    role_type_id = models.CharField(max_length=20)
    prod_catalog = models.ForeignKey(ProdCatalog, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_catalog_role'
        unique_together = (('party', 'role_type_id', 'prod_catalog', 'from_date'),)


class ProdConfItemContent(models.Model):
    config_item = models.OneToOneField('ProductConfigItem', models.DO_NOTHING, primary_key=True)  # The composite primary key (config_item_id, content_id, conf_item_content_type_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    conf_item_content_type = models.ForeignKey('ProdConfItemContentType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_conf_item_content'
        unique_together = (('config_item', 'content', 'conf_item_content_type', 'from_date'),)


class ProdConfItemContentType(models.Model):
    conf_item_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_conf_item_content_type'


class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=20)
    product_type = models.ForeignKey('ProductType', models.DO_NOTHING, blank=True, null=True)
    primary_product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    manufacturer_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    introduction_date = models.DateTimeField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    support_discontinuation_date = models.DateTimeField(blank=True, null=True)
    sales_discontinuation_date = models.DateTimeField(blank=True, null=True)
    sales_disc_when_not_avail = models.CharField(max_length=1, blank=True, null=True)
    internal_name = models.CharField(max_length=255, blank=True, null=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    price_detail_text = models.CharField(max_length=255, blank=True, null=True)
    small_image_url = models.CharField(max_length=2000, blank=True, null=True)
    medium_image_url = models.CharField(max_length=2000, blank=True, null=True)
    large_image_url = models.CharField(max_length=2000, blank=True, null=True)
    detail_image_url = models.CharField(max_length=2000, blank=True, null=True)
    original_image_url = models.CharField(max_length=2000, blank=True, null=True)
    detail_screen = models.CharField(max_length=255, blank=True, null=True)
    inventory_message = models.CharField(max_length=255, blank=True, null=True)
    inventory_item_type = models.ForeignKey(InventoryItemType, models.DO_NOTHING, blank=True, null=True)
    require_inventory = models.CharField(max_length=1, blank=True, null=True)
    quantity_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    quantity_included = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    pieces_included = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    require_amount = models.CharField(max_length=1, blank=True, null=True)
    fixed_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    amount_uom_type = models.ForeignKey('UomType', models.DO_NOTHING, blank=True, null=True)
    weight_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='product_weight_uom_set', blank=True, null=True)
    shipping_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    height_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='product_height_uom_set', blank=True, null=True)
    product_height = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    shipping_height = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    width_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='product_width_uom_set', blank=True, null=True)
    product_width = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    shipping_width = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    depth_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='product_depth_uom_set', blank=True, null=True)
    product_depth = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    shipping_depth = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    diameter_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='product_diameter_uom_set', blank=True, null=True)
    product_diameter = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_rating = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    rating_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, db_column='rating_type_enum', blank=True, null=True)
    returnable = models.CharField(max_length=1, blank=True, null=True)
    taxable = models.CharField(max_length=1, blank=True, null=True)
    charge_shipping = models.CharField(max_length=1, blank=True, null=True)
    auto_create_keywords = models.CharField(max_length=1, blank=True, null=True)
    include_in_promotions = models.CharField(max_length=1, blank=True, null=True)
    is_virtual = models.CharField(max_length=1, blank=True, null=True)
    is_variant = models.CharField(max_length=1, blank=True, null=True)
    virtual_variant_method_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, db_column='virtual_variant_method_enum', related_name='product_virtual_variant_method_enum_set', blank=True, null=True)
    origin_geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    requirement_method_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='product_requirement_method_enum_set', blank=True, null=True)
    bill_of_material_level = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    reserv_max_persons = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv2nd_p_p_perc = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_nth_p_p_perc = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    config_id = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='product_last_modified_by_user_login_set', blank=True, null=True)
    in_shipping_box = models.CharField(max_length=1, blank=True, null=True)
    default_shipment_box_type = models.ForeignKey('ShipmentBoxType', models.DO_NOTHING, blank=True, null=True)
    lot_id_filled_in = models.CharField(max_length=255, blank=True, null=True)
    order_decimal_quantity = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductAssoc(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, product_id_to, product_assoc_type_id, from_date) found, that is not supported. The first column is selected.
    product_id_to = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_id_to', related_name='productassoc_product_id_to_set')
    product_assoc_type = models.ForeignKey('ProductAssocType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    scrap_factor = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    instruction = models.CharField(max_length=255, blank=True, null=True)
    routing_work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    estimate_calc_method = models.ForeignKey(CustomMethod, models.DO_NOTHING, db_column='estimate_calc_method', blank=True, null=True)
    recurrence_info = models.ForeignKey('RecurrenceInfo', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_assoc'
        unique_together = (('product', 'product_id_to', 'product_assoc_type', 'from_date'),)


class ProductAssocType(models.Model):
    product_assoc_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_assoc_type'


class ProductAttribute(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_type = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute'
        unique_together = (('product', 'attr_name'),)


class ProductAverageCost(models.Model):
    product_average_cost_type = models.OneToOneField('ProductAverageCostType', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_average_cost_type_id, organization_party_id, product_id, facility_id, from_date) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey(Party, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    average_cost = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_average_cost'
        unique_together = (('product_average_cost_type', 'organization_party', 'product', 'facility', 'from_date'),)


class ProductAverageCostType(models.Model):
    product_average_cost_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_average_cost_type'


class ProductCalculatedInfo(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)
    total_quantity_ordered = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_times_viewed = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    average_customer_rating = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_calculated_info'


class ProductCategory(models.Model):
    product_category_id = models.CharField(primary_key=True, max_length=20)
    product_category_type = models.ForeignKey('ProductCategoryType', models.DO_NOTHING, blank=True, null=True)
    primary_parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    category_image_url = models.CharField(max_length=2000, blank=True, null=True)
    link_one_image_url = models.CharField(max_length=2000, blank=True, null=True)
    link_two_image_url = models.CharField(max_length=2000, blank=True, null=True)
    detail_screen = models.CharField(max_length=255, blank=True, null=True)
    show_in_select = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductCategoryAttribute(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_attribute'
        unique_together = (('product_category', 'attr_name'),)


class ProductCategoryContent(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, content_id, prod_cat_content_type_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    prod_cat_content_type = models.ForeignKey('ProductCategoryContentType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    purchase_from_date = models.DateTimeField(blank=True, null=True)
    purchase_thru_date = models.DateTimeField(blank=True, null=True)
    use_count_limit = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_days_limit = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_content'
        unique_together = (('product_category', 'content', 'prod_cat_content_type', 'from_date'),)


class ProductCategoryContentType(models.Model):
    prod_cat_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_content_type'


class ProductCategoryGlAccount(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, organization_party_id, gl_account_type_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey(Party, models.DO_NOTHING)
    gl_account_type = models.ForeignKey(GlAccountType, models.DO_NOTHING)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_gl_account'
        unique_together = (('product_category', 'organization_party', 'gl_account_type'),)


class ProductCategoryLink(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, link_seq_id, from_date) found, that is not supported. The first column is selected.
    link_seq_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    title_text = models.CharField(max_length=255, blank=True, null=True)
    detail_text = models.TextField(blank=True, null=True)
    image_url = models.CharField(max_length=2000, blank=True, null=True)
    image_two_url = models.CharField(max_length=2000, blank=True, null=True)
    link_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    link_info = models.CharField(max_length=255, blank=True, null=True)
    detail_sub_screen = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_link'
        unique_together = (('product_category', 'link_seq_id', 'from_date'),)


class ProductCategoryMember(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, product_id, from_date) found, that is not supported. The first column is selected.
    product = models.ForeignKey(Product, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_member'
        unique_together = (('product_category', 'product', 'from_date'),)


class ProductCategoryRole(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_role'
        unique_together = (('product_category', 'party', 'role_type_id', 'from_date'),)


class ProductCategoryRollup(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, parent_product_category_id, from_date) found, that is not supported. The first column is selected.
    parent_product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, related_name='productcategoryrollup_parent_product_category_set')
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_rollup'
        unique_together = (('product_category', 'parent_product_category', 'from_date'),)


class ProductCategoryType(models.Model):
    product_category_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_type'


class ProductCategoryTypeAttr(models.Model):
    product_category_type = models.OneToOneField(ProductCategoryType, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category_type_attr'
        unique_together = (('product_category_type', 'attr_name'),)


class ProductConfig(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, config_item_id, sequence_num, from_date) found, that is not supported. The first column is selected.
    config_item = models.ForeignKey('ProductConfigItem', models.DO_NOTHING)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0)
    from_date = models.DateTimeField()
    description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    config_type_id = models.CharField(max_length=20, blank=True, null=True)
    default_config_option_id = models.CharField(max_length=20, blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    is_mandatory = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_config'
        unique_together = (('product', 'config_item', 'sequence_num', 'from_date'),)


class ProductConfigConfig(models.Model):
    config_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (config_id, config_item_id, config_option_id, sequence_num) found, that is not supported. The first column is selected.
    config_item = models.ForeignKey('ProductConfigOption', models.DO_NOTHING)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0)
    config_option_id = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_config_config'
        unique_together = (('config_id', 'config_item', 'config_option_id', 'sequence_num'),)


class ProductConfigItem(models.Model):
    config_item_id = models.CharField(primary_key=True, max_length=20)
    config_item_type_id = models.CharField(max_length=20, blank=True, null=True)
    config_item_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    image_url = models.CharField(max_length=2000, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_config_item'


class ProductConfigOption(models.Model):
    config_item = models.OneToOneField(ProductConfigItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (config_item_id, config_option_id) found, that is not supported. The first column is selected.
    config_option_id = models.CharField(max_length=20)
    config_option_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_config_option'
        unique_together = (('config_item', 'config_option_id'),)


class ProductConfigOptionIactn(models.Model):
    config_item = models.OneToOneField(ProductConfigOption, models.DO_NOTHING, primary_key=True)  # The composite primary key (config_item_id, config_option_id, config_item_id_to, config_option_id_to, sequence_num) found, that is not supported. The first column is selected.
    config_option_id = models.CharField(max_length=20)
    config_item_id_to = models.ForeignKey(ProductConfigOption, models.DO_NOTHING, db_column='config_item_id_to', related_name='productconfigoptioniactn_config_item_id_to_set')
    config_option_id_to = models.CharField(max_length=20)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0)
    config_iactn_type_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_config_option_iactn'
        unique_together = (('config_item', 'config_option_id', 'config_item_id_to', 'config_option_id_to', 'sequence_num'),)


class ProductConfigProduct(models.Model):
    config_item = models.OneToOneField(ProductConfigOption, models.DO_NOTHING, primary_key=True)  # The composite primary key (config_item_id, config_option_id, product_id) found, that is not supported. The first column is selected.
    config_option_id = models.CharField(max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_config_product'
        unique_together = (('config_item', 'config_option_id', 'product'),)


class ProductConfigStats(models.Model):
    config_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (config_id, product_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey(Product, models.DO_NOTHING)
    num_of_confs = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    config_type_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_config_stats'
        unique_together = (('config_id', 'product'),)


class ProductContent(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, content_id, product_content_type_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    product_content_type = models.ForeignKey('ProductContentType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    purchase_from_date = models.DateTimeField(blank=True, null=True)
    purchase_thru_date = models.DateTimeField(blank=True, null=True)
    use_count_limit = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    use_role_type = models.ForeignKey('RoleType', models.DO_NOTHING, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_content'
        unique_together = (('product', 'content', 'product_content_type', 'from_date'),)


class ProductContentType(models.Model):
    product_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_content_type'


class ProductCostComponentCalc(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, cost_component_type_id, from_date) found, that is not supported. The first column is selected.
    cost_component_type = models.ForeignKey(CostComponentType, models.DO_NOTHING)
    cost_component_calc = models.ForeignKey(CostComponentCalc, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField()
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_cost_component_calc'
        unique_together = (('product', 'cost_component_type', 'from_date'),)


class ProductFacility(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, facility_id) found, that is not supported. The first column is selected.
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    minimum_stock = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reorder_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    days_to_ship = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_inventory_count = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_facility'
        unique_together = (('product', 'facility'),)


class ProductFacilityLocation(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, facility_id, location_seq_id) found, that is not supported. The first column is selected.
    facility = models.ForeignKey(FacilityLocation, models.DO_NOTHING)
    location_seq_id = models.CharField(max_length=20)
    minimum_stock = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    move_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_facility_location'
        unique_together = (('product', 'facility', 'location_seq_id'),)


class ProductFeature(models.Model):
    product_feature_id = models.CharField(primary_key=True, max_length=20)
    product_feature_type = models.ForeignKey('ProductFeatureType', models.DO_NOTHING, blank=True, null=True)
    product_feature_category = models.ForeignKey('ProductFeatureCategory', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    number_specified = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    default_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    default_sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    abbrev = models.CharField(max_length=20, blank=True, null=True)
    id_code = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature'


class ProductFeatureAppl(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, product_feature_id, from_date) found, that is not supported. The first column is selected.
    product_feature = models.ForeignKey(ProductFeature, models.DO_NOTHING)
    product_feature_appl_type = models.ForeignKey('ProductFeatureApplType', models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    recurring_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_appl'
        unique_together = (('product', 'product_feature', 'from_date'),)


class ProductFeatureApplAttr(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, product_feature_id, from_date, attr_name) found, that is not supported. The first column is selected.
    product_feature = models.ForeignKey(ProductFeature, models.DO_NOTHING)
    from_date = models.DateTimeField()
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_appl_attr'
        unique_together = (('product', 'product_feature', 'from_date', 'attr_name'),)


class ProductFeatureApplType(models.Model):
    product_feature_appl_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_appl_type'


class ProductFeatureCatGrpAppl(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, product_feature_group_id, from_date) found, that is not supported. The first column is selected.
    product_feature_group = models.ForeignKey('ProductFeatureGroup', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_cat_grp_appl'
        unique_together = (('product_category', 'product_feature_group', 'from_date'),)


class ProductFeatureCategory(models.Model):
    product_feature_category_id = models.CharField(primary_key=True, max_length=20)
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_category'


class ProductFeatureCategoryAppl(models.Model):
    product_category = models.OneToOneField(ProductCategory, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_category_id, product_feature_category_id, from_date) found, that is not supported. The first column is selected.
    product_feature_category = models.ForeignKey(ProductFeatureCategory, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_category_appl'
        unique_together = (('product_category', 'product_feature_category', 'from_date'),)


class ProductFeatureDataResource(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)  # The composite primary key (data_resource_id, product_feature_id) found, that is not supported. The first column is selected.
    product_feature = models.ForeignKey(ProductFeature, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_data_resource'
        unique_together = (('data_resource', 'product_feature'),)


class ProductFeatureGroup(models.Model):
    product_feature_group_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_group'


class ProductFeatureGroupAppl(models.Model):
    product_feature_group = models.OneToOneField(ProductFeatureGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_feature_group_id, product_feature_id, from_date) found, that is not supported. The first column is selected.
    product_feature = models.ForeignKey(ProductFeature, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_group_appl'
        unique_together = (('product_feature_group', 'product_feature', 'from_date'),)


class ProductFeatureIactn(models.Model):
    product_feature = models.OneToOneField(ProductFeature, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_feature_id, product_feature_id_to) found, that is not supported. The first column is selected.
    product_feature_id_to = models.ForeignKey(ProductFeature, models.DO_NOTHING, db_column='product_feature_id_to', related_name='productfeatureiactn_product_feature_id_to_set')
    product_feature_iactn_type = models.ForeignKey('ProductFeatureIactnType', models.DO_NOTHING, blank=True, null=True)
    product_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_iactn'
        unique_together = (('product_feature', 'product_feature_id_to'),)


class ProductFeatureIactnType(models.Model):
    product_feature_iactn_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_iactn_type'


class ProductFeaturePrice(models.Model):
    product_feature_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (product_feature_id, product_price_type_id, currency_uom_id, from_date) found, that is not supported. The first column is selected.
    product_price_type = models.ForeignKey('ProductPriceType', models.DO_NOTHING)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='productfeatureprice_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_price'
        unique_together = (('product_feature_id', 'product_price_type', 'currency_uom', 'from_date'),)


class ProductFeatureType(models.Model):
    product_feature_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_feature_type'


class ProductGeo(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, geo_id) found, that is not supported. The first column is selected.
    geo = models.ForeignKey(Geo, models.DO_NOTHING)
    product_geo_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_geo'
        unique_together = (('product', 'geo'),)


class ProductGlAccount(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, organization_party_id, gl_account_type_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey(Party, models.DO_NOTHING)
    gl_account_type = models.ForeignKey(GlAccountType, models.DO_NOTHING)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_gl_account'
        unique_together = (('product', 'organization_party', 'gl_account_type'),)


class ProductGroupOrder(models.Model):
    group_order_id = models.CharField(primary_key=True, max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    req_order_qty = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    sold_order_qty = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    job = models.ForeignKey(JobSandbox, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_group_order'


class ProductKeyword(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, keyword) found, that is not supported. The first column is selected.
    keyword = models.CharField(max_length=60)
    relevancy_weight = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_keyword'
        unique_together = (('product', 'keyword'),)


class ProductKeywordNew(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, keyword, keyword_type_id) found, that is not supported. The first column is selected.
    keyword = models.CharField(max_length=60)
    keyword_type = models.ForeignKey(Enumeration, models.DO_NOTHING)
    relevancy_weight = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_keyword_new'
        unique_together = (('product', 'keyword', 'keyword_type'),)


class ProductKeywordResult(models.Model):
    product_keyword_result_id = models.CharField(primary_key=True, max_length=20)
    visit_id = models.CharField(max_length=20, blank=True, null=True)
    product_category_id = models.CharField(max_length=20, blank=True, null=True)
    search_string = models.CharField(max_length=60, blank=True, null=True)
    intra_keyword_operator = models.CharField(max_length=10, blank=True, null=True)
    any_prefix = models.CharField(max_length=1, blank=True, null=True)
    any_suffix = models.CharField(max_length=1, blank=True, null=True)
    remove_stems = models.CharField(max_length=1, blank=True, null=True)
    num_results = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_keyword_result'


class ProductMaint(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, product_maint_seq_id) found, that is not supported. The first column is selected.
    product_maint_seq_id = models.CharField(max_length=20)
    product_maint_type = models.ForeignKey('ProductMaintType', models.DO_NOTHING, blank=True, null=True)
    maint_name = models.CharField(max_length=100, blank=True, null=True)
    maint_template_work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    interval_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    interval_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    interval_meter_type = models.ForeignKey('ProductMeterType', models.DO_NOTHING, blank=True, null=True)
    repeat_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_maint'
        unique_together = (('product', 'product_maint_seq_id'),)


class ProductMaintType(models.Model):
    product_maint_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_maint_type'


class ProductManufacturingRule(models.Model):
    rule_id = models.CharField(primary_key=True, max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    product_id_for = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_id_for', related_name='productmanufacturingrule_product_id_for_set', blank=True, null=True)
    product_id_in = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_id_in', related_name='productmanufacturingrule_product_id_in_set', blank=True, null=True)
    rule_seq_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    product_id_in_subst = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_id_in_subst', related_name='productmanufacturingrule_product_id_in_subst_set', blank=True, null=True)
    product_feature = models.ForeignKey(ProductFeature, models.DO_NOTHING, db_column='product_feature', blank=True, null=True)
    rule_operator = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_manufacturing_rule'


class ProductMeter(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, product_meter_type_id) found, that is not supported. The first column is selected.
    product_meter_type = models.ForeignKey('ProductMeterType', models.DO_NOTHING)
    meter_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    meter_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_meter'
        unique_together = (('product', 'product_meter_type'),)


class ProductMeterType(models.Model):
    product_meter_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    default_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_meter_type'


class ProductOrderItem(models.Model):
    order = models.OneToOneField(OrderItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, order_item_seq_id, engagement_id, engagement_item_seq_id) found, that is not supported. The first column is selected.
    order_item_seq_id = models.CharField(max_length=20)
    engagement = models.ForeignKey(OrderItem, models.DO_NOTHING, related_name='productorderitem_engagement_set')
    engagement_item_seq_id = models.CharField(max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_order_item'
        unique_together = (('order', 'order_item_seq_id', 'engagement', 'engagement_item_seq_id'),)


class ProductPaymentMethodType(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, payment_method_type_id, product_price_purpose_id, from_date) found, that is not supported. The first column is selected.
    payment_method_type = models.ForeignKey(PaymentMethodType, models.DO_NOTHING)
    product_price_purpose = models.ForeignKey('ProductPricePurpose', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_payment_method_type'
        unique_together = (('product', 'payment_method_type', 'product_price_purpose', 'from_date'),)


class ProductPrice(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, product_price_type_id, product_price_purpose_id, currency_uom_id, product_store_group_id, from_date) found, that is not supported. The first column is selected.
    product_price_type = models.ForeignKey('ProductPriceType', models.DO_NOTHING)
    product_price_purpose = models.ForeignKey('ProductPricePurpose', models.DO_NOTHING)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING)
    product_store_group = models.ForeignKey('ProductStoreGroup', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    term_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='productprice_term_uom_set', blank=True, null=True)
    custom_price_calc_service = models.ForeignKey(CustomMethod, models.DO_NOTHING, db_column='custom_price_calc_service', blank=True, null=True)
    price_without_tax = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    price_with_tax = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    tax_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    tax_auth_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    tax_auth_geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    tax_in_price = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='productprice_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price'
        unique_together = (('product', 'product_price_type', 'product_price_purpose', 'currency_uom', 'product_store_group', 'from_date'),)


class ProductPriceAction(models.Model):
    product_price_rule = models.OneToOneField('ProductPriceRule', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_price_rule_id, product_price_action_seq_id) found, that is not supported. The first column is selected.
    product_price_action_seq_id = models.CharField(max_length=20)
    product_price_action_type = models.ForeignKey('ProductPriceActionType', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    rate_code = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_action'
        unique_together = (('product_price_rule', 'product_price_action_seq_id'),)


class ProductPriceActionType(models.Model):
    product_price_action_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_action_type'


class ProductPriceAutoNotice(models.Model):
    product_price_notice_id = models.CharField(primary_key=True, max_length=20)
    facility_id = models.CharField(max_length=20, blank=True, null=True)
    run_date = models.DateTimeField(blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_auto_notice'


class ProductPriceChange(models.Model):
    product_price_change_id = models.CharField(primary_key=True, max_length=20)
    product_id = models.CharField(max_length=20, blank=True, null=True)
    product_price_type_id = models.CharField(max_length=20, blank=True, null=True)
    product_price_purpose_id = models.CharField(max_length=20, blank=True, null=True)
    currency_uom_id = models.CharField(max_length=20, blank=True, null=True)
    product_store_group_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    old_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    changed_date = models.DateTimeField(blank=True, null=True)
    changed_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='changed_by_user_login', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_change'


class ProductPriceCond(models.Model):
    product_price_rule = models.OneToOneField('ProductPriceRule', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_price_rule_id, product_price_cond_seq_id) found, that is not supported. The first column is selected.
    product_price_cond_seq_id = models.CharField(max_length=20)
    input_param_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    operator_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='productpricecond_operator_enum_set', blank=True, null=True)
    cond_value = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_cond'
        unique_together = (('product_price_rule', 'product_price_cond_seq_id'),)


class ProductPricePurpose(models.Model):
    product_price_purpose_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_purpose'


class ProductPriceRule(models.Model):
    product_price_rule_id = models.CharField(primary_key=True, max_length=20)
    rule_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_sale = models.CharField(max_length=1, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_rule'


class ProductPriceType(models.Model):
    product_price_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price_type'


class ProductPromo(models.Model):
    product_promo_id = models.CharField(primary_key=True, max_length=20)
    promo_name = models.CharField(max_length=100, blank=True, null=True)
    promo_text = models.CharField(max_length=255, blank=True, null=True)
    user_entered = models.CharField(max_length=1, blank=True, null=True)
    show_to_customer = models.CharField(max_length=1, blank=True, null=True)
    require_code = models.CharField(max_length=1, blank=True, null=True)
    use_limit_per_order = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_limit_per_customer = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_limit_per_promotion = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    billback_factor = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    override_org_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='productpromo_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo'


class ProductPromoAction(models.Model):
    product_promo = models.OneToOneField('ProductPromoRule', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_promo_id, product_promo_rule_id, product_promo_action_seq_id) found, that is not supported. The first column is selected.
    product_promo_rule_id = models.CharField(max_length=20)
    product_promo_action_seq_id = models.CharField(max_length=20)
    product_promo_action_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    order_adjustment_type = models.ForeignKey(OrderAdjustmentType, models.DO_NOTHING, blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_id = models.CharField(max_length=20, blank=True, null=True)
    party_id = models.CharField(max_length=20, blank=True, null=True)
    use_cart_quantity = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_action'
        unique_together = (('product_promo', 'product_promo_rule_id', 'product_promo_action_seq_id'),)


class ProductPromoCategory(models.Model):
    product_promo = models.OneToOneField(ProductPromo, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_promo_id, product_promo_rule_id, product_promo_action_seq_id, product_promo_cond_seq_id, product_category_id, and_group_id) found, that is not supported. The first column is selected.
    product_promo_rule_id = models.CharField(max_length=20)
    product_promo_action_seq_id = models.CharField(max_length=20)
    product_promo_cond_seq_id = models.CharField(max_length=20)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    and_group_id = models.CharField(max_length=20)
    product_promo_appl_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    include_sub_categories = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_category'
        unique_together = (('product_promo', 'product_promo_rule_id', 'product_promo_action_seq_id', 'product_promo_cond_seq_id', 'product_category', 'and_group_id'),)


class ProductPromoCode(models.Model):
    product_promo_code_id = models.CharField(primary_key=True, max_length=20)
    product_promo = models.ForeignKey(ProductPromo, models.DO_NOTHING, blank=True, null=True)
    user_entered = models.CharField(max_length=1, blank=True, null=True)
    require_email_or_party = models.CharField(max_length=1, blank=True, null=True)
    use_limit_per_code = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_limit_per_customer = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='last_modified_by_user_login', related_name='productpromocode_last_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_code'


class ProductPromoCodeEmail(models.Model):
    product_promo_code = models.OneToOneField(ProductPromoCode, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_promo_code_id, email_address) found, that is not supported. The first column is selected.
    email_address = models.CharField(max_length=320)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_code_email'
        unique_together = (('product_promo_code', 'email_address'),)


class ProductPromoCodeParty(models.Model):
    product_promo_code = models.OneToOneField(ProductPromoCode, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_promo_code_id, party_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(Party, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_code_party'
        unique_together = (('product_promo_code', 'party'),)


class ProductPromoCond(models.Model):
    product_promo = models.OneToOneField('ProductPromoRule', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_promo_id, product_promo_rule_id, product_promo_cond_seq_id) found, that is not supported. The first column is selected.
    product_promo_rule_id = models.CharField(max_length=20)
    product_promo_cond_seq_id = models.CharField(max_length=20)
    input_param_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    operator_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='productpromocond_operator_enum_set', blank=True, null=True)
    cond_value = models.CharField(max_length=255, blank=True, null=True)
    other_value = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_cond'
        unique_together = (('product_promo', 'product_promo_rule_id', 'product_promo_cond_seq_id'),)


class ProductPromoContent(models.Model):
    product_promo = models.OneToOneField(ProductPromo, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_promo_id, content_id, product_promo_content_type_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    product_promo_content_type = models.ForeignKey(ProductContentType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_content'
        unique_together = (('product_promo', 'content', 'product_promo_content_type', 'from_date'),)


class ProductPromoProduct(models.Model):
    product_promo = models.OneToOneField(ProductPromo, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_promo_id, product_promo_rule_id, product_promo_action_seq_id, product_promo_cond_seq_id, product_id) found, that is not supported. The first column is selected.
    product_promo_rule_id = models.CharField(max_length=20)
    product_promo_action_seq_id = models.CharField(max_length=20)
    product_promo_cond_seq_id = models.CharField(max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    product_promo_appl_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_product'
        unique_together = (('product_promo', 'product_promo_rule_id', 'product_promo_action_seq_id', 'product_promo_cond_seq_id', 'product'),)


class ProductPromoRule(models.Model):
    product_promo = models.OneToOneField(ProductPromo, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_promo_id, product_promo_rule_id) found, that is not supported. The first column is selected.
    product_promo_rule_id = models.CharField(max_length=20)
    rule_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_rule'
        unique_together = (('product_promo', 'product_promo_rule_id'),)


class ProductPromoUse(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, promo_sequence_id) found, that is not supported. The first column is selected.
    promo_sequence_id = models.CharField(max_length=20)
    product_promo = models.ForeignKey(ProductPromo, models.DO_NOTHING, blank=True, null=True)
    product_promo_code = models.ForeignKey(ProductPromoCode, models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    total_discount_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    quantity_left_in_actions = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_promo_use'
        unique_together = (('order', 'promo_sequence_id'),)


class ProductReview(models.Model):
    product_review_id = models.CharField(primary_key=True, max_length=20)
    product_store = models.ForeignKey('ProductStore', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    posted_anonymous = models.CharField(max_length=1, blank=True, null=True)
    posted_date_time = models.DateTimeField(blank=True, null=True)
    product_rating = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_review = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_review'


class ProductRole(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_role'
        unique_together = (('product', 'party', 'role_type_id', 'from_date'),)


class ProductSearchConstraint(models.Model):
    product_search_result = models.OneToOneField('ProductSearchResult', models.DO_NOTHING, primary_key=True)  # The composite primary key (product_search_result_id, constraint_seq_id) found, that is not supported. The first column is selected.
    constraint_seq_id = models.CharField(max_length=20)
    constraint_name = models.CharField(max_length=255, blank=True, null=True)
    info_string = models.CharField(max_length=255, blank=True, null=True)
    include_sub_categories = models.CharField(max_length=1, blank=True, null=True)
    is_and = models.CharField(max_length=1, blank=True, null=True)
    any_prefix = models.CharField(max_length=1, blank=True, null=True)
    any_suffix = models.CharField(max_length=1, blank=True, null=True)
    remove_stems = models.CharField(max_length=1, blank=True, null=True)
    low_value = models.CharField(max_length=60, blank=True, null=True)
    high_value = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_search_constraint'
        unique_together = (('product_search_result', 'constraint_seq_id'),)


class ProductSearchResult(models.Model):
    product_search_result_id = models.CharField(primary_key=True, max_length=20)
    visit_id = models.CharField(max_length=20, blank=True, null=True)
    order_by_name = models.CharField(max_length=255, blank=True, null=True)
    is_ascending = models.CharField(max_length=1, blank=True, null=True)
    num_results = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    seconds_total = models.FloatField(blank=True, null=True)
    search_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_search_result'


class ProductStore(models.Model):
    product_store_id = models.CharField(primary_key=True, max_length=20)
    primary_store_group = models.ForeignKey('ProductStoreGroup', models.DO_NOTHING, blank=True, null=True)
    store_name = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    pay_to_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    days_to_cancel_non_pay = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    manual_auth_is_capture = models.CharField(max_length=1, blank=True, null=True)
    prorate_shipping = models.CharField(max_length=1, blank=True, null=True)
    prorate_taxes = models.CharField(max_length=1, blank=True, null=True)
    view_cart_on_add = models.CharField(max_length=1, blank=True, null=True)
    auto_save_cart = models.CharField(max_length=1, blank=True, null=True)
    auto_approve_reviews = models.CharField(max_length=1, blank=True, null=True)
    is_demo_store = models.CharField(max_length=1, blank=True, null=True)
    is_immediately_fulfilled = models.CharField(max_length=1, blank=True, null=True)
    inventory_facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    one_inventory_facility = models.CharField(max_length=1, blank=True, null=True)
    check_inventory = models.CharField(max_length=1, blank=True, null=True)
    reserve_inventory = models.CharField(max_length=1, blank=True, null=True)
    reserve_order_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    require_inventory = models.CharField(max_length=1, blank=True, null=True)
    balance_res_on_order_creation = models.CharField(max_length=1, blank=True, null=True)
    requirement_method_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='productstore_requirement_method_enum_set', blank=True, null=True)
    order_number_prefix = models.CharField(max_length=60, blank=True, null=True)
    default_locale_string = models.CharField(max_length=10, blank=True, null=True)
    default_currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    default_time_zone_string = models.CharField(max_length=60, blank=True, null=True)
    default_sales_channel_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='productstore_default_sales_channel_enum_set', blank=True, null=True)
    allow_password = models.CharField(max_length=1, blank=True, null=True)
    default_password = models.CharField(max_length=255, blank=True, null=True)
    explode_order_items = models.CharField(max_length=1, blank=True, null=True)
    check_gc_balance = models.CharField(max_length=1, blank=True, null=True)
    retry_failed_auths = models.CharField(max_length=1, blank=True, null=True)
    header_approved_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='header_approved_status', blank=True, null=True)
    item_approved_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='item_approved_status', related_name='productstore_item_approved_status_set', blank=True, null=True)
    digital_item_approved_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='digital_item_approved_status', related_name='productstore_digital_item_approved_status_set', blank=True, null=True)
    header_declined_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='header_declined_status', related_name='productstore_header_declined_status_set', blank=True, null=True)
    item_declined_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='item_declined_status', related_name='productstore_item_declined_status_set', blank=True, null=True)
    header_cancel_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='header_cancel_status', related_name='productstore_header_cancel_status_set', blank=True, null=True)
    item_cancel_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='item_cancel_status', related_name='productstore_item_cancel_status_set', blank=True, null=True)
    auth_declined_message = models.CharField(max_length=255, blank=True, null=True)
    auth_fraud_message = models.CharField(max_length=255, blank=True, null=True)
    auth_error_message = models.CharField(max_length=255, blank=True, null=True)
    visual_theme_id = models.CharField(max_length=20, blank=True, null=True)
    store_credit_account_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='productstore_store_credit_account_enum_set', blank=True, null=True)
    use_primary_email_username = models.CharField(max_length=1, blank=True, null=True)
    require_customer_role = models.CharField(max_length=1, blank=True, null=True)
    auto_invoice_digital_items = models.CharField(max_length=1, blank=True, null=True)
    req_ship_addr_for_dig_items = models.CharField(max_length=1, blank=True, null=True)
    show_checkout_gift_options = models.CharField(max_length=1, blank=True, null=True)
    select_payment_type_per_item = models.CharField(max_length=1, blank=True, null=True)
    show_prices_with_vat_tax = models.CharField(max_length=1, blank=True, null=True)
    show_tax_is_exempt = models.CharField(max_length=1, blank=True, null=True)
    vat_tax_auth_geo = models.ForeignKey('TaxAuthority', models.DO_NOTHING, blank=True, null=True)
    vat_tax_auth_party_id = models.CharField(max_length=20, blank=True, null=True)
    enable_auto_suggestion_list = models.CharField(max_length=1, blank=True, null=True)
    enable_dig_prod_upload = models.CharField(max_length=1, blank=True, null=True)
    prod_search_exclude_variants = models.CharField(max_length=1, blank=True, null=True)
    dig_prod_upload_category_id = models.CharField(max_length=20, blank=True, null=True)
    auto_order_cc_try_exp = models.CharField(max_length=1, blank=True, null=True)
    auto_order_cc_try_other_cards = models.CharField(max_length=1, blank=True, null=True)
    auto_order_cc_try_later_nsf = models.CharField(max_length=1, blank=True, null=True)
    auto_order_cc_try_later_max = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    store_credit_valid_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    auto_approve_invoice = models.CharField(max_length=1, blank=True, null=True)
    auto_approve_order = models.CharField(max_length=1, blank=True, null=True)
    ship_if_capture_fails = models.CharField(max_length=1, blank=True, null=True)
    set_owner_upon_issuance = models.CharField(max_length=1, blank=True, null=True)
    req_return_inventory_receive = models.CharField(max_length=1, blank=True, null=True)
    add_to_cart_remove_incompat = models.CharField(max_length=1, blank=True, null=True)
    add_to_cart_replace_upsell = models.CharField(max_length=1, blank=True, null=True)
    split_pay_pref_per_shp_grp = models.CharField(max_length=1, blank=True, null=True)
    managed_by_lot = models.CharField(max_length=1, blank=True, null=True)
    show_out_of_stock_products = models.CharField(max_length=1, blank=True, null=True)
    order_decimal_quantity = models.CharField(max_length=1, blank=True, null=True)
    allow_comment = models.CharField(max_length=1, blank=True, null=True)
    style_sheet = models.CharField(max_length=2000, blank=True, null=True)
    header_logo = models.CharField(max_length=2000, blank=True, null=True)
    header_middle_background = models.CharField(max_length=2000, blank=True, null=True)
    header_right_background = models.CharField(max_length=2000, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store'


class ProductStoreCatalog(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, prod_catalog_id, from_date) found, that is not supported. The first column is selected.
    prod_catalog = models.ForeignKey(ProdCatalog, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_catalog'
        unique_together = (('product_store', 'prod_catalog', 'from_date'),)


class ProductStoreEmailSetting(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, email_type) found, that is not supported. The first column is selected.
    email_type = models.ForeignKey(Enumeration, models.DO_NOTHING, db_column='email_type')
    body_screen_location = models.CharField(max_length=255, blank=True, null=True)
    xslfo_attach_screen_location = models.CharField(max_length=255, blank=True, null=True)
    from_address = models.CharField(max_length=320, blank=True, null=True)
    cc_address = models.CharField(max_length=320, blank=True, null=True)
    bcc_address = models.CharField(max_length=320, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_email_setting'
        unique_together = (('product_store', 'email_type'),)


class ProductStoreFacility(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, facility_id, from_date) found, that is not supported. The first column is selected.
    facility = models.ForeignKey(Facility, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_facility'
        unique_together = (('product_store', 'facility', 'from_date'),)


class ProductStoreFinActSetting(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, fin_account_type_id) found, that is not supported. The first column is selected.
    fin_account_type = models.ForeignKey(FinAccountType, models.DO_NOTHING)
    require_pin_code = models.CharField(max_length=1, blank=True, null=True)
    validate_g_c_fin_acct = models.CharField(max_length=1, blank=True, null=True)
    account_code_length = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    pin_code_length = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    account_valid_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    auth_valid_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    purchase_survey = models.ForeignKey('Survey', models.DO_NOTHING, blank=True, null=True)
    purch_survey_send_to = models.CharField(max_length=20, blank=True, null=True)
    purch_survey_copy_me = models.CharField(max_length=20, blank=True, null=True)
    allow_auth_to_negative = models.CharField(max_length=1, blank=True, null=True)
    min_balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    replenish_threshold = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    replenish_method_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_fin_act_setting'
        unique_together = (('product_store', 'fin_account_type'),)


class ProductStoreGroup(models.Model):
    product_store_group_id = models.CharField(primary_key=True, max_length=20)
    product_store_group_type = models.ForeignKey('ProductStoreGroupType', models.DO_NOTHING, blank=True, null=True)
    primary_parent_group = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    product_store_group_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_group'


class ProductStoreGroupMember(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, product_store_group_id, from_date) found, that is not supported. The first column is selected.
    product_store_group = models.ForeignKey(ProductStoreGroup, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_group_member'
        unique_together = (('product_store', 'product_store_group', 'from_date'),)


class ProductStoreGroupRole(models.Model):
    product_store_group = models.OneToOneField(ProductStoreGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_group_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_group_role'
        unique_together = (('product_store_group', 'party', 'role_type_id'),)


class ProductStoreGroupRollup(models.Model):
    product_store_group = models.OneToOneField(ProductStoreGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_group_id, parent_group_id, from_date) found, that is not supported. The first column is selected.
    parent_group = models.ForeignKey(ProductStoreGroup, models.DO_NOTHING, related_name='productstoregrouprollup_parent_group_set')
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_group_rollup'
        unique_together = (('product_store_group', 'parent_group', 'from_date'),)


class ProductStoreGroupType(models.Model):
    product_store_group_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_group_type'


class ProductStoreKeywordOvrd(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, keyword, from_date) found, that is not supported. The first column is selected.
    keyword = models.CharField(max_length=60)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    target_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_keyword_ovrd'
        unique_together = (('product_store', 'keyword', 'from_date'),)


class ProductStorePaymentSetting(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, payment_method_type_id, payment_service_type_enum_id) found, that is not supported. The first column is selected.
    payment_method_type = models.ForeignKey(PaymentMethodType, models.DO_NOTHING)
    payment_service_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING)
    payment_service = models.CharField(max_length=255, blank=True, null=True)
    payment_custom_method = models.ForeignKey(CustomMethod, models.DO_NOTHING, blank=True, null=True)
    payment_gateway_config = models.ForeignKey(PaymentGatewayConfig, models.DO_NOTHING, blank=True, null=True)
    payment_properties_path = models.CharField(max_length=255, blank=True, null=True)
    apply_to_all_products = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_payment_setting'
        unique_together = (('product_store', 'payment_method_type', 'payment_service_type_enum'),)


class ProductStorePromoAppl(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, product_promo_id, from_date) found, that is not supported. The first column is selected.
    product_promo = models.ForeignKey(ProductPromo, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    manual_only = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_promo_appl'
        unique_together = (('product_store', 'product_promo', 'from_date'),)


class ProductStoreRole(models.Model):
    party = models.OneToOneField(PartyRole, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, role_type_id, product_store_id, from_date) found, that is not supported. The first column is selected.
    role_type_id = models.CharField(max_length=20)
    product_store = models.ForeignKey(ProductStore, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_role'
        unique_together = (('party', 'role_type_id', 'product_store', 'from_date'),)


class ProductStoreShipmentMeth(models.Model):
    product_store_ship_meth_id = models.CharField(primary_key=True, max_length=20)
    product_store_id = models.CharField(max_length=20, blank=True, null=True)
    shipment_method_type = models.ForeignKey('ShipmentMethodType', models.DO_NOTHING, blank=True, null=True)
    party_id = models.CharField(max_length=20, blank=True, null=True)
    role_type_id = models.CharField(max_length=20, blank=True, null=True)
    company_party_id = models.CharField(max_length=20, blank=True, null=True)
    min_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    max_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    min_size = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    max_size = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    min_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    max_total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    allow_usps_addr = models.CharField(max_length=1, blank=True, null=True)
    require_usps_addr = models.CharField(max_length=1, blank=True, null=True)
    allow_company_addr = models.CharField(max_length=1, blank=True, null=True)
    require_company_addr = models.CharField(max_length=1, blank=True, null=True)
    include_no_charge_items = models.CharField(max_length=1, blank=True, null=True)
    include_feature_group = models.CharField(max_length=20, blank=True, null=True)
    exclude_feature_group = models.CharField(max_length=20, blank=True, null=True)
    include_geo_id = models.CharField(max_length=20, blank=True, null=True)
    exclude_geo_id = models.CharField(max_length=20, blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    config_props = models.CharField(max_length=255, blank=True, null=True)
    shipment_custom_method = models.ForeignKey(CustomMethod, models.DO_NOTHING, blank=True, null=True)
    shipment_gateway_config = models.ForeignKey('ShipmentGatewayConfig', models.DO_NOTHING, blank=True, null=True)
    sequence_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    allowance_percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    minimum_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_shipment_meth'


class ProductStoreSurveyAppl(models.Model):
    product_store_survey_id = models.CharField(primary_key=True, max_length=20)
    product_store = models.ForeignKey(ProductStore, models.DO_NOTHING, blank=True, null=True)
    survey_appl_type = models.ForeignKey('SurveyApplType', models.DO_NOTHING, blank=True, null=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    survey = models.ForeignKey('Survey', models.DO_NOTHING, blank=True, null=True)
    product_id = models.CharField(max_length=20, blank=True, null=True)
    product_category_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    survey_template = models.CharField(max_length=255, blank=True, null=True)
    result_template = models.CharField(max_length=255, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_survey_appl'


class ProductStoreVendorPayment(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, vendor_party_id, payment_method_type_id, credit_card_enum_id) found, that is not supported. The first column is selected.
    vendor_party = models.ForeignKey(Party, models.DO_NOTHING)
    payment_method_type = models.ForeignKey(PaymentMethodType, models.DO_NOTHING)
    credit_card_enum = models.ForeignKey(Enumeration, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_vendor_payment'
        unique_together = (('product_store', 'vendor_party', 'payment_method_type', 'credit_card_enum'),)


class ProductStoreVendorShipment(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, vendor_party_id, shipment_method_type_id, carrier_party_id) found, that is not supported. The first column is selected.
    vendor_party = models.ForeignKey(Party, models.DO_NOTHING)
    shipment_method_type = models.ForeignKey('ShipmentMethodType', models.DO_NOTHING)
    carrier_party = models.ForeignKey(Party, models.DO_NOTHING, related_name='productstorevendorshipment_carrier_party_set')
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_store_vendor_shipment'
        unique_together = (('product_store', 'vendor_party', 'shipment_method_type', 'carrier_party'),)


class ProductSubscriptionResource(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, subscription_resource_id, from_date) found, that is not supported. The first column is selected.
    subscription_resource = models.ForeignKey('SubscriptionResource', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    purchase_from_date = models.DateTimeField(blank=True, null=True)
    purchase_thru_date = models.DateTimeField(blank=True, null=True)
    max_life_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_life_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    available_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    available_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='productsubscriptionresource_available_time_uom_set', blank=True, null=True)
    use_count_limit = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='productsubscriptionresource_use_time_uom_set', blank=True, null=True)
    use_role_type = models.ForeignKey('RoleType', models.DO_NOTHING, blank=True, null=True)
    automatic_extend = models.CharField(max_length=1, blank=True, null=True)
    cancl_autm_ext_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    cancl_autm_ext_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='productsubscriptionresource_cancl_autm_ext_time_uom_set', blank=True, null=True)
    grace_period_on_expiry = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    grace_period_on_expiry_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='productsubscriptionresource_grace_period_on_expiry_uom_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_subscription_resource'
        unique_together = (('product', 'subscription_resource', 'from_date'),)


class ProductType(models.Model):
    product_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    is_physical = models.CharField(max_length=1, blank=True, null=True)
    is_digital = models.CharField(max_length=1, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_type'


class ProductTypeAttr(models.Model):
    product_type = models.OneToOneField(ProductType, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_type_attr'
        unique_together = (('product_type', 'attr_name'),)


class ProtectedView(models.Model):
    group = models.OneToOneField('SecurityGroup', models.DO_NOTHING, primary_key=True)  # The composite primary key (group_id, view_name_id) found, that is not supported. The first column is selected.
    view_name_id = models.CharField(max_length=60)
    max_hits = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_hits_duration = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    tarpit_duration = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protected_view'
        unique_together = (('group', 'view_name_id'),)


class ProtocolType(models.Model):
    protocol_type_id = models.CharField(primary_key=True, max_length=20)
    protocol_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'protocol_type'


class QuantityBreak(models.Model):
    quantity_break_id = models.CharField(primary_key=True, max_length=20)
    quantity_break_type = models.ForeignKey('QuantityBreakType', models.DO_NOTHING, blank=True, null=True)
    from_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    thru_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quantity_break'


class QuantityBreakType(models.Model):
    quantity_break_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quantity_break_type'


class Quote(models.Model):
    quote_id = models.CharField(primary_key=True, max_length=20)
    quote_type = models.ForeignKey('QuoteType', models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    product_store = models.ForeignKey(ProductStore, models.DO_NOTHING, blank=True, null=True)
    sales_channel_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    valid_from_date = models.DateTimeField(blank=True, null=True)
    valid_thru_date = models.DateTimeField(blank=True, null=True)
    quote_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote'


class QuoteAdjustment(models.Model):
    quote_adjustment_id = models.CharField(primary_key=True, max_length=20)
    quote_adjustment_type = models.ForeignKey(OrderAdjustmentType, models.DO_NOTHING, blank=True, null=True)
    quote = models.ForeignKey(Quote, models.DO_NOTHING, blank=True, null=True)
    quote_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    product_promo = models.ForeignKey(ProductPromo, models.DO_NOTHING, blank=True, null=True)
    product_promo_rule_id = models.CharField(max_length=20, blank=True, null=True)
    product_promo_action_seq_id = models.CharField(max_length=20, blank=True, null=True)
    product_feature_id = models.CharField(max_length=20, blank=True, null=True)
    corresponding_product_id = models.CharField(max_length=20, blank=True, null=True)
    source_reference_id = models.CharField(max_length=60, blank=True, null=True)
    source_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    customer_reference_id = models.CharField(max_length=60, blank=True, null=True)
    primary_geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    secondary_geo = models.ForeignKey(Geo, models.DO_NOTHING, related_name='quoteadjustment_secondary_geo_set', blank=True, null=True)
    exempt_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tax_auth_geo = models.ForeignKey('TaxAuthority', models.DO_NOTHING, blank=True, null=True)
    tax_auth_party_id = models.CharField(max_length=20, blank=True, null=True)
    override_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    include_in_tax = models.CharField(max_length=1, blank=True, null=True)
    include_in_shipping = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_adjustment'


class QuoteAttribute(models.Model):
    quote = models.OneToOneField(Quote, models.DO_NOTHING, primary_key=True)  # The composite primary key (quote_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_attribute'
        unique_together = (('quote', 'attr_name'),)


class QuoteCoefficient(models.Model):
    quote = models.OneToOneField(Quote, models.DO_NOTHING, primary_key=True)  # The composite primary key (quote_id, coeff_name) found, that is not supported. The first column is selected.
    coeff_name = models.CharField(max_length=60)
    coeff_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_coefficient'
        unique_together = (('quote', 'coeff_name'),)


class QuoteItem(models.Model):
    quote = models.OneToOneField(Quote, models.DO_NOTHING, primary_key=True)  # The composite primary key (quote_id, quote_item_seq_id) found, that is not supported. The first column is selected.
    quote_item_seq_id = models.CharField(max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    product_feature = models.ForeignKey(ProductFeature, models.DO_NOTHING, blank=True, null=True)
    deliverable_type = models.ForeignKey(DeliverableType, models.DO_NOTHING, blank=True, null=True)
    skill_type = models.ForeignKey('SkillType', models.DO_NOTHING, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    cust_request = models.ForeignKey(CustRequest, models.DO_NOTHING, blank=True, null=True)
    cust_request_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    selected_amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quote_unit_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    reserv_start = models.DateTimeField(blank=True, null=True)
    reserv_length = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_persons = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    config_id = models.CharField(max_length=20, blank=True, null=True)
    estimated_delivery_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    is_promo = models.CharField(max_length=1, blank=True, null=True)
    lead_time_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_item'
        unique_together = (('quote', 'quote_item_seq_id'),)


class QuoteNote(models.Model):
    quote = models.OneToOneField(Quote, models.DO_NOTHING, primary_key=True)  # The composite primary key (quote_id, note_id) found, that is not supported. The first column is selected.
    note = models.ForeignKey(NoteData, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_note'
        unique_together = (('quote', 'note'),)


class QuoteRole(models.Model):
    quote = models.OneToOneField(Quote, models.DO_NOTHING, primary_key=True)  # The composite primary key (quote_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_role'
        unique_together = (('quote', 'party', 'role_type_id'),)


class QuoteTerm(models.Model):
    term_type = models.OneToOneField('TermType', models.DO_NOTHING, primary_key=True)  # The composite primary key (term_type_id, quote_id, quote_item_seq_id) found, that is not supported. The first column is selected.
    quote = models.ForeignKey(Quote, models.DO_NOTHING)
    quote_item_seq_id = models.CharField(max_length=20)
    term_value = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    uom_id = models.CharField(max_length=20, blank=True, null=True)
    term_days = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    text_value = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_term'
        unique_together = (('term_type', 'quote', 'quote_item_seq_id'),)


class QuoteTermAttribute(models.Model):
    term_type = models.OneToOneField(QuoteTerm, models.DO_NOTHING, primary_key=True)  # The composite primary key (term_type_id, quote_id, quote_item_seq_id, attr_name) found, that is not supported. The first column is selected.
    quote_id = models.CharField(max_length=20)
    quote_item_seq_id = models.CharField(max_length=20)
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_term_attribute'
        unique_together = (('term_type', 'quote_id', 'quote_item_seq_id', 'attr_name'),)


class QuoteType(models.Model):
    quote_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_type'


class QuoteTypeAttr(models.Model):
    quote_type = models.OneToOneField(QuoteType, models.DO_NOTHING, primary_key=True)  # The composite primary key (quote_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_type_attr'
        unique_together = (('quote_type', 'attr_name'),)


class QuoteWorkEffort(models.Model):
    quote = models.OneToOneField(Quote, models.DO_NOTHING, primary_key=True)  # The composite primary key (quote_id, work_effort_id) found, that is not supported. The first column is selected.
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_work_effort'
        unique_together = (('quote', 'work_effort'),)


class RateAmount(models.Model):
    rate_type = models.OneToOneField('RateType', models.DO_NOTHING, primary_key=True)  # The composite primary key (rate_type_id, rate_currency_uom_id, period_type_id, party_id, work_effort_id, empl_position_type_id, from_date) found, that is not supported. The first column is selected.
    rate_currency_uom = models.ForeignKey('Uom', models.DO_NOTHING)
    period_type = models.ForeignKey(PeriodType, models.DO_NOTHING)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    empl_position_type = models.ForeignKey(EmplPositionType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    rate_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rate_amount'
        unique_together = (('rate_type', 'rate_currency_uom', 'period_type', 'party', 'work_effort', 'empl_position_type', 'from_date'),)


class RateType(models.Model):
    rate_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rate_type'


class RecurrenceInfo(models.Model):
    recurrence_info_id = models.CharField(primary_key=True, max_length=20)
    start_date_time = models.DateTimeField(blank=True, null=True)
    exception_date_times = models.TextField(blank=True, null=True)
    recurrence_date_times = models.TextField(blank=True, null=True)
    exception_rule = models.ForeignKey('RecurrenceRule', models.DO_NOTHING, blank=True, null=True)
    recurrence_rule = models.ForeignKey('RecurrenceRule', models.DO_NOTHING, related_name='recurrenceinfo_recurrence_rule_set', blank=True, null=True)
    recurrence_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recurrence_info'


class RecurrenceRule(models.Model):
    recurrence_rule_id = models.CharField(primary_key=True, max_length=20)
    frequency = models.CharField(max_length=60, blank=True, null=True)
    until_date_time = models.DateTimeField(blank=True, null=True)
    count_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    interval_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    by_second_list = models.TextField(blank=True, null=True)
    by_minute_list = models.TextField(blank=True, null=True)
    by_hour_list = models.TextField(blank=True, null=True)
    by_day_list = models.TextField(blank=True, null=True)
    by_month_day_list = models.TextField(blank=True, null=True)
    by_year_day_list = models.TextField(blank=True, null=True)
    by_week_no_list = models.TextField(blank=True, null=True)
    by_month_list = models.TextField(blank=True, null=True)
    by_set_pos_list = models.TextField(blank=True, null=True)
    week_start = models.CharField(max_length=60, blank=True, null=True)
    x_name = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recurrence_rule'


class RejectionReason(models.Model):
    rejection_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rejection_reason'


class ReorderGuideline(models.Model):
    reorder_guideline_id = models.CharField(primary_key=True, max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    role_type_id = models.CharField(max_length=20, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    reorder_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reorder_level = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reorder_guideline'


class Requirement(models.Model):
    requirement_id = models.CharField(primary_key=True, max_length=20)
    requirement_type = models.ForeignKey('RequirementType', models.DO_NOTHING, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    deliverable = models.ForeignKey(Deliverable, models.DO_NOTHING, blank=True, null=True)
    fixed_asset = models.ForeignKey(FixedAsset, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    requirement_start_date = models.DateTimeField(blank=True, null=True)
    required_by_date = models.DateTimeField(blank=True, null=True)
    estimated_budget = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    use_case = models.TextField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement'


class RequirementAttribute(models.Model):
    requirement = models.OneToOneField(Requirement, models.DO_NOTHING, primary_key=True)  # The composite primary key (requirement_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement_attribute'
        unique_together = (('requirement', 'attr_name'),)


class RequirementBudgetAllocation(models.Model):
    budget = models.OneToOneField(BudgetItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (budget_id, budget_item_seq_id, requirement_id) found, that is not supported. The first column is selected.
    budget_item_seq_id = models.CharField(max_length=20)
    requirement = models.ForeignKey(Requirement, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement_budget_allocation'
        unique_together = (('budget', 'budget_item_seq_id', 'requirement'),)


class RequirementCustRequest(models.Model):
    cust_request = models.OneToOneField(CustRequestItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (cust_request_id, cust_request_item_seq_id, requirement_id) found, that is not supported. The first column is selected.
    cust_request_item_seq_id = models.CharField(max_length=20)
    requirement = models.ForeignKey(Requirement, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement_cust_request'
        unique_together = (('cust_request', 'cust_request_item_seq_id', 'requirement'),)


class RequirementRole(models.Model):
    requirement = models.OneToOneField(Requirement, models.DO_NOTHING, primary_key=True)  # The composite primary key (requirement_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey(Party, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement_role'
        unique_together = (('requirement', 'party', 'role_type_id', 'from_date'),)


class RequirementStatus(models.Model):
    requirement = models.OneToOneField(Requirement, models.DO_NOTHING, primary_key=True)  # The composite primary key (requirement_id, status_id) found, that is not supported. The first column is selected.
    status = models.ForeignKey('StatusItem', models.DO_NOTHING)
    status_date = models.DateTimeField(blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement_status'
        unique_together = (('requirement', 'status'),)


class RequirementType(models.Model):
    requirement_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement_type'


class RequirementTypeAttr(models.Model):
    requirement_type = models.OneToOneField(RequirementType, models.DO_NOTHING, primary_key=True)  # The composite primary key (requirement_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement_type_attr'
        unique_together = (('requirement_type', 'attr_name'),)


class RespondingParty(models.Model):
    responding_party_seq_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (responding_party_seq_id, cust_request_id, party_id) found, that is not supported. The first column is selected.
    cust_request = models.ForeignKey(CustRequest, models.DO_NOTHING)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responding_party'
        unique_together = (('responding_party_seq_id', 'cust_request', 'party'),)


class ResponsibilityType(models.Model):
    responsibility_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responsibility_type'


class ReturnAdjustment(models.Model):
    return_adjustment_id = models.CharField(primary_key=True, max_length=20)
    return_adjustment_type = models.ForeignKey('ReturnAdjustmentType', models.DO_NOTHING, blank=True, null=True)
    return_field = models.ForeignKey('ReturnHeader', models.DO_NOTHING, db_column='return_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    return_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    ship_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    return_type = models.ForeignKey('ReturnType', models.DO_NOTHING, blank=True, null=True)
    order_adjustment = models.ForeignKey(OrderAdjustment, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    product_promo = models.ForeignKey(ProductPromo, models.DO_NOTHING, blank=True, null=True)
    product_promo_rule_id = models.CharField(max_length=20, blank=True, null=True)
    product_promo_action_seq_id = models.CharField(max_length=20, blank=True, null=True)
    product_feature_id = models.CharField(max_length=20, blank=True, null=True)
    corresponding_product_id = models.CharField(max_length=20, blank=True, null=True)
    tax_authority_rate_seq = models.ForeignKey('TaxAuthorityRateProduct', models.DO_NOTHING, blank=True, null=True)
    source_reference_id = models.CharField(max_length=60, blank=True, null=True)
    source_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    customer_reference_id = models.CharField(max_length=60, blank=True, null=True)
    primary_geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    secondary_geo = models.ForeignKey(Geo, models.DO_NOTHING, related_name='returnadjustment_secondary_geo_set', blank=True, null=True)
    exempt_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tax_auth_geo = models.ForeignKey('TaxAuthority', models.DO_NOTHING, blank=True, null=True)
    tax_auth_party_id = models.CharField(max_length=20, blank=True, null=True)
    override_gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    include_in_tax = models.CharField(max_length=1, blank=True, null=True)
    include_in_shipping = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_adjustment'


class ReturnAdjustmentType(models.Model):
    return_adjustment_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_adjustment_type'


class ReturnContactMech(models.Model):
    return_field = models.OneToOneField('ReturnHeader', models.DO_NOTHING, db_column='return_id', primary_key=True)  # Field renamed because it was a Python reserved word. The composite primary key (return_id, contact_mech_purpose_type_id, contact_mech_id) found, that is not supported. The first column is selected.
    contact_mech_purpose_type = models.ForeignKey(ContactMechPurposeType, models.DO_NOTHING)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_contact_mech'
        unique_together = (('return_field', 'contact_mech_purpose_type', 'contact_mech'),)


class ReturnHeader(models.Model):
    return_id = models.CharField(primary_key=True, max_length=20)
    return_header_type = models.ForeignKey('ReturnHeaderType', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    from_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    to_party = models.ForeignKey(Party, models.DO_NOTHING, related_name='returnheader_to_party_set', blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, blank=True, null=True)
    fin_account = models.ForeignKey(FinAccount, models.DO_NOTHING, blank=True, null=True)
    billing_account = models.ForeignKey(BillingAccount, models.DO_NOTHING, blank=True, null=True)
    entry_date = models.DateTimeField(blank=True, null=True)
    origin_contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    destination_facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    needs_inventory_receive = models.CharField(max_length=1, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    supplier_rma_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_header'


class ReturnHeaderType(models.Model):
    return_header_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_header_type'


class ReturnItem(models.Model):
    return_field = models.OneToOneField(ReturnHeader, models.DO_NOTHING, db_column='return_id', primary_key=True)  # Field renamed because it was a Python reserved word. The composite primary key (return_id, return_item_seq_id) found, that is not supported. The first column is selected.
    return_item_seq_id = models.CharField(max_length=20)
    return_reason = models.ForeignKey('ReturnReason', models.DO_NOTHING, blank=True, null=True)
    return_type = models.ForeignKey('ReturnType', models.DO_NOTHING, blank=True, null=True)
    return_item_type = models.ForeignKey('ReturnItemType', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    order = models.ForeignKey(OrderItem, models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    expected_item_status = models.ForeignKey('StatusItem', models.DO_NOTHING, db_column='expected_item_status', related_name='returnitem_expected_item_status_set', blank=True, null=True)
    return_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    received_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    return_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    return_item_response = models.ForeignKey('ReturnItemResponse', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_item'
        unique_together = (('return_field', 'return_item_seq_id'),)


class ReturnItemBilling(models.Model):
    return_field = models.OneToOneField(ReturnItem, models.DO_NOTHING, db_column='return_id', primary_key=True)  # Field renamed because it was a Python reserved word. The composite primary key (return_id, return_item_seq_id, invoice_id, invoice_item_seq_id) found, that is not supported. The first column is selected.
    return_item_seq_id = models.CharField(max_length=20)
    invoice = models.ForeignKey(InvoiceItem, models.DO_NOTHING)
    invoice_item_seq_id = models.CharField(max_length=20)
    shipment_receipt = models.ForeignKey('ShipmentReceipt', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_item_billing'
        unique_together = (('return_field', 'return_item_seq_id', 'invoice', 'invoice_item_seq_id'),)


class ReturnItemResponse(models.Model):
    return_item_response_id = models.CharField(primary_key=True, max_length=20)
    order_payment_preference = models.ForeignKey(OrderPaymentPreference, models.DO_NOTHING, blank=True, null=True)
    replacement_order = models.ForeignKey(OrderHeader, models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey(Payment, models.DO_NOTHING, blank=True, null=True)
    billing_account = models.ForeignKey(BillingAccount, models.DO_NOTHING, blank=True, null=True)
    fin_account_trans = models.ForeignKey(FinAccountTrans, models.DO_NOTHING, blank=True, null=True)
    response_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_item_response'


class ReturnItemShipment(models.Model):
    return_field = models.OneToOneField(ReturnItem, models.DO_NOTHING, db_column='return_id', primary_key=True)  # Field renamed because it was a Python reserved word. The composite primary key (return_id, return_item_seq_id, shipment_id, shipment_item_seq_id) found, that is not supported. The first column is selected.
    return_item_seq_id = models.CharField(max_length=20)
    shipment = models.ForeignKey('Shipment', models.DO_NOTHING)
    shipment_item_seq_id = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_item_shipment'
        unique_together = (('return_field', 'return_item_seq_id', 'shipment', 'shipment_item_seq_id'),)


class ReturnItemType(models.Model):
    return_item_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_item_type'


class ReturnItemTypeMap(models.Model):
    return_item_map_key = models.CharField(primary_key=True, max_length=20)  # The composite primary key (return_item_map_key, return_header_type_id) found, that is not supported. The first column is selected.
    return_header_type = models.ForeignKey(ReturnHeaderType, models.DO_NOTHING)
    return_item_type_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_item_type_map'
        unique_together = (('return_item_map_key', 'return_header_type'),)


class ReturnReason(models.Model):
    return_reason_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    sequence_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_reason'


class ReturnStatus(models.Model):
    return_status_id = models.CharField(primary_key=True, max_length=20)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    return_field = models.ForeignKey(ReturnHeader, models.DO_NOTHING, db_column='return_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    return_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    status_datetime = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_status'


class ReturnType(models.Model):
    return_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    sequence_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_type'


class RoleType(models.Model):
    role_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_type'


class RoleTypeAttr(models.Model):
    role_type = models.OneToOneField(RoleType, models.DO_NOTHING, primary_key=True)  # The composite primary key (role_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_type_attr'
        unique_together = (('role_type', 'attr_name'),)


class RuntimeData(models.Model):
    runtime_data_id = models.CharField(primary_key=True, max_length=20)
    runtime_info = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'runtime_data'


class SalaryStep(models.Model):
    salary_step_seq_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (salary_step_seq_id, pay_grade_id) found, that is not supported. The first column is selected.
    pay_grade = models.ForeignKey(PayGrade, models.DO_NOTHING)
    date_modified = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary_step'
        unique_together = (('salary_step_seq_id', 'pay_grade'),)


class SalaryStepNew(models.Model):
    salary_step_seq_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (salary_step_seq_id, pay_grade_id, from_date) found, that is not supported. The first column is selected.
    pay_grade = models.ForeignKey(PayGrade, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary_step_new'
        unique_together = (('salary_step_seq_id', 'pay_grade', 'from_date'),)


class SaleType(models.Model):
    sale_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_type'


class SalesForecast(models.Model):
    sales_forecast_id = models.CharField(primary_key=True, max_length=20)
    parent_sales_forecast = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    organization_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    internal_party = models.ForeignKey(Party, models.DO_NOTHING, related_name='salesforecast_internal_party_set', blank=True, null=True)
    custom_time_period = models.ForeignKey(CustomTimePeriod, models.DO_NOTHING, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    quota_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    forecast_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    best_case_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    closed_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    percent_of_quota_forecast = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    percent_of_quota_closed = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    pipeline_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, related_name='salesforecast_modified_by_user_login_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_forecast'


class SalesForecastDetail(models.Model):
    sales_forecast = models.OneToOneField(SalesForecast, models.DO_NOTHING, primary_key=True)  # The composite primary key (sales_forecast_id, sales_forecast_detail_id) found, that is not supported. The first column is selected.
    sales_forecast_detail_id = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    quantity_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_forecast_detail'
        unique_together = (('sales_forecast', 'sales_forecast_detail_id'),)


class SalesForecastHistory(models.Model):
    sales_forecast_history_id = models.CharField(primary_key=True, max_length=20)
    sales_forecast = models.ForeignKey(SalesForecast, models.DO_NOTHING, blank=True, null=True)
    parent_sales_forecast_id = models.CharField(max_length=20, blank=True, null=True)
    organization_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    internal_party = models.ForeignKey(Party, models.DO_NOTHING, related_name='salesforecasthistory_internal_party_set', blank=True, null=True)
    custom_time_period = models.ForeignKey(CustomTimePeriod, models.DO_NOTHING, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    quota_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    forecast_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    best_case_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    closed_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    percent_of_quota_forecast = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    percent_of_quota_closed = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    change_note = models.TextField(blank=True, null=True)
    modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    modified_timestamp = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_forecast_history'


class SalesOpportunity(models.Model):
    sales_opportunity_id = models.CharField(primary_key=True, max_length=20)
    opportunity_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    next_step = models.TextField(blank=True, null=True)
    next_step_date = models.DateTimeField(blank=True, null=True)
    estimated_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estimated_probability = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    marketing_campaign = models.ForeignKey(MarketingCampaign, models.DO_NOTHING, blank=True, null=True)
    data_source_id = models.CharField(max_length=20, blank=True, null=True)
    estimated_close_date = models.DateTimeField(blank=True, null=True)
    opportunity_stage = models.ForeignKey('SalesOpportunityStage', models.DO_NOTHING, blank=True, null=True)
    type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    created_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='created_by_user_login', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_opportunity'


class SalesOpportunityCompetitor(models.Model):
    sales_opportunity = models.OneToOneField(SalesOpportunity, models.DO_NOTHING, primary_key=True)  # The composite primary key (sales_opportunity_id, competitor_party_id) found, that is not supported. The first column is selected.
    competitor_party_id = models.CharField(max_length=20)
    position_enum_id = models.CharField(max_length=20, blank=True, null=True)
    strengths = models.TextField(blank=True, null=True)
    weaknesses = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_opportunity_competitor'
        unique_together = (('sales_opportunity', 'competitor_party_id'),)


class SalesOpportunityHistory(models.Model):
    sales_opportunity_history_id = models.CharField(primary_key=True, max_length=20)
    sales_opportunity = models.ForeignKey(SalesOpportunity, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    next_step = models.TextField(blank=True, null=True)
    estimated_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    estimated_probability = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    estimated_close_date = models.DateTimeField(blank=True, null=True)
    opportunity_stage = models.ForeignKey('SalesOpportunityStage', models.DO_NOTHING, blank=True, null=True)
    change_note = models.TextField(blank=True, null=True)
    modified_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, db_column='modified_by_user_login', blank=True, null=True)
    modified_timestamp = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_opportunity_history'


class SalesOpportunityQuote(models.Model):
    sales_opportunity = models.OneToOneField(SalesOpportunity, models.DO_NOTHING, primary_key=True)  # The composite primary key (sales_opportunity_id, quote_id) found, that is not supported. The first column is selected.
    quote = models.ForeignKey(Quote, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_opportunity_quote'
        unique_together = (('sales_opportunity', 'quote'),)


class SalesOpportunityRole(models.Model):
    sales_opportunity = models.OneToOneField(SalesOpportunity, models.DO_NOTHING, primary_key=True)  # The composite primary key (sales_opportunity_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type = models.ForeignKey(RoleType, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_opportunity_role'
        unique_together = (('sales_opportunity', 'party', 'role_type'),)


class SalesOpportunityStage(models.Model):
    opportunity_stage_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    default_probability = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_opportunity_stage'


class SalesOpportunityTrckCode(models.Model):
    sales_opportunity = models.OneToOneField(SalesOpportunity, models.DO_NOTHING, primary_key=True)  # The composite primary key (sales_opportunity_id, tracking_code_id) found, that is not supported. The first column is selected.
    tracking_code_id = models.CharField(max_length=20)
    received_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_opportunity_trck_code'
        unique_together = (('sales_opportunity', 'tracking_code_id'),)


class SalesOpportunityWorkEffort(models.Model):
    sales_opportunity = models.OneToOneField(SalesOpportunity, models.DO_NOTHING, primary_key=True)  # The composite primary key (sales_opportunity_id, work_effort_id) found, that is not supported. The first column is selected.
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_opportunity_work_effort'
        unique_together = (('sales_opportunity', 'work_effort'),)


class SecurityGroup(models.Model):
    group_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_group'


class SecurityGroupPermission(models.Model):
    group = models.OneToOneField(SecurityGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (group_id, permission_id) found, that is not supported. The first column is selected.
    permission_id = models.CharField(max_length=60)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_group_permission'
        unique_together = (('group', 'permission_id'),)


class SecurityPermission(models.Model):
    permission_id = models.CharField(primary_key=True, max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_permission'


class SegmentGroup(models.Model):
    segment_group_id = models.CharField(primary_key=True, max_length=20)
    segment_group_type = models.ForeignKey('SegmentGroupType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    product_store = models.ForeignKey(ProductStore, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'segment_group'


class SegmentGroupClassification(models.Model):
    segment_group = models.OneToOneField(SegmentGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (segment_group_id, party_classification_group_id) found, that is not supported. The first column is selected.
    party_classification_group = models.ForeignKey(PartyClassificationGroup, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'segment_group_classification'
        unique_together = (('segment_group', 'party_classification_group'),)


class SegmentGroupGeo(models.Model):
    segment_group = models.OneToOneField(SegmentGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (segment_group_id, geo_id) found, that is not supported. The first column is selected.
    geo = models.ForeignKey(Geo, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'segment_group_geo'
        unique_together = (('segment_group', 'geo'),)


class SegmentGroupRole(models.Model):
    segment_group = models.OneToOneField(SegmentGroup, models.DO_NOTHING, primary_key=True)  # The composite primary key (segment_group_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'segment_group_role'
        unique_together = (('segment_group', 'party', 'role_type_id'),)


class SegmentGroupType(models.Model):
    segment_group_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'segment_group_type'


class SequenceValueItem(models.Model):
    seq_name = models.CharField(primary_key=True, max_length=60)
    seq_id = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sequence_value_item'


class ServerHit(models.Model):
    visit = models.OneToOneField('Visit', models.DO_NOTHING, primary_key=True)  # The composite primary key (visit_id, content_id, hit_start_date_time, hit_type_id) found, that is not supported. The first column is selected.
    content_id = models.CharField(max_length=255)
    hit_start_date_time = models.DateTimeField()
    hit_type = models.ForeignKey('ServerHitType', models.DO_NOTHING)
    num_of_bytes = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    running_time_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    user_login_id = models.CharField(max_length=255, blank=True, null=True)
    status_id = models.CharField(max_length=20, blank=True, null=True)
    request_url = models.CharField(max_length=2000, blank=True, null=True)
    referrer_url = models.CharField(max_length=2000, blank=True, null=True)
    server_ip_address = models.CharField(max_length=20, blank=True, null=True)
    server_host_name = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    internal_content = models.ForeignKey(Content, models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    id_by_ip_contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    ref_by_web_contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, related_name='serverhit_ref_by_web_contact_mech_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_hit'
        unique_together = (('visit', 'content_id', 'hit_start_date_time', 'hit_type'),)


class ServerHitBin(models.Model):
    server_hit_bin_id = models.CharField(primary_key=True, max_length=20)
    content_id = models.CharField(max_length=255, blank=True, null=True)
    hit_type = models.ForeignKey('ServerHitType', models.DO_NOTHING, blank=True, null=True)
    server_ip_address = models.CharField(max_length=20, blank=True, null=True)
    server_host_name = models.CharField(max_length=255, blank=True, null=True)
    bin_start_date_time = models.DateTimeField(blank=True, null=True)
    bin_end_date_time = models.DateTimeField(blank=True, null=True)
    number_hits = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    total_time_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    min_time_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_time_millis = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    internal_content = models.ForeignKey(Content, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_hit_bin'


class ServerHitType(models.Model):
    hit_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_hit_type'


class ServiceSemaphore(models.Model):
    service_name = models.CharField(primary_key=True, max_length=100)
    locked_by_instance_id = models.CharField(max_length=20, blank=True, null=True)
    lock_thread = models.CharField(max_length=100, blank=True, null=True)
    lock_time = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_semaphore'


class SettlementTerm(models.Model):
    settlement_term_id = models.CharField(primary_key=True, max_length=20)
    term_name = models.CharField(max_length=100, blank=True, null=True)
    term_value = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    uom_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settlement_term'


class Shipment(models.Model):
    shipment_id = models.CharField(primary_key=True, max_length=20)
    shipment_type = models.ForeignKey('ShipmentType', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    primary_order = models.ForeignKey(OrderHeader, models.DO_NOTHING, blank=True, null=True)
    primary_return = models.ForeignKey(ReturnHeader, models.DO_NOTHING, blank=True, null=True)
    primary_ship_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    picklist_bin = models.ForeignKey(PicklistBin, models.DO_NOTHING, blank=True, null=True)
    estimated_ready_date = models.DateTimeField(blank=True, null=True)
    estimated_ship_date = models.DateTimeField(blank=True, null=True)
    estimated_ship_work_eff = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    estimated_arrival_date = models.DateTimeField(blank=True, null=True)
    estimated_arrival_work_eff = models.ForeignKey('WorkEffort', models.DO_NOTHING, related_name='shipment_estimated_arrival_work_eff_set', blank=True, null=True)
    latest_cancel_date = models.DateTimeField(blank=True, null=True)
    estimated_ship_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    handling_instructions = models.CharField(max_length=255, blank=True, null=True)
    origin_facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    destination_facility = models.ForeignKey(Facility, models.DO_NOTHING, related_name='shipment_destination_facility_set', blank=True, null=True)
    origin_contact_mech = models.ForeignKey(PostalAddress, models.DO_NOTHING, blank=True, null=True)
    origin_telecom_number = models.ForeignKey('TelecomNumber', models.DO_NOTHING, blank=True, null=True)
    destination_contact_mech = models.ForeignKey(PostalAddress, models.DO_NOTHING, related_name='shipment_destination_contact_mech_set', blank=True, null=True)
    destination_telecom_number = models.ForeignKey('TelecomNumber', models.DO_NOTHING, related_name='shipment_destination_telecom_number_set', blank=True, null=True)
    party_id_to = models.ForeignKey(Party, models.DO_NOTHING, db_column='party_id_to', blank=True, null=True)
    party_id_from = models.ForeignKey(Party, models.DO_NOTHING, db_column='party_id_from', related_name='shipment_party_id_from_set', blank=True, null=True)
    additional_shipping_charge = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    addtl_shipping_charge_desc = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment'


class ShipmentAttribute(models.Model):
    shipment = models.OneToOneField(Shipment, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_attribute'
        unique_together = (('shipment', 'attr_name'),)


class ShipmentBoxType(models.Model):
    shipment_box_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    dimension_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    box_length = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    box_width = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    box_height = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    weight_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='shipmentboxtype_weight_uom_set', blank=True, null=True)
    box_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_box_type'


class ShipmentContactMech(models.Model):
    shipment = models.OneToOneField(Shipment, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, shipment_contact_mech_type_id) found, that is not supported. The first column is selected.
    shipment_contact_mech_type = models.ForeignKey('ShipmentContactMechType', models.DO_NOTHING)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_contact_mech'
        unique_together = (('shipment', 'shipment_contact_mech_type'),)


class ShipmentContactMechType(models.Model):
    shipment_contact_mech_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_contact_mech_type'


class ShipmentCostEstimate(models.Model):
    shipment_cost_estimate_id = models.CharField(primary_key=True, max_length=20)
    shipment_method_type = models.ForeignKey(CarrierShipmentMethod, models.DO_NOTHING, blank=True, null=True)
    carrier_party_id = models.CharField(max_length=20, blank=True, null=True)
    carrier_role_type_id = models.CharField(max_length=20, blank=True, null=True)
    product_store_ship_meth = models.ForeignKey(ProductStoreShipmentMeth, models.DO_NOTHING, blank=True, null=True)
    product_store_id = models.CharField(max_length=20, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    role_type = models.ForeignKey(RoleType, models.DO_NOTHING, blank=True, null=True)
    geo_id_to = models.ForeignKey(Geo, models.DO_NOTHING, db_column='geo_id_to', blank=True, null=True)
    geo_id_from = models.ForeignKey(Geo, models.DO_NOTHING, db_column='geo_id_from', related_name='shipmentcostestimate_geo_id_from_set', blank=True, null=True)
    weight_break = models.ForeignKey(QuantityBreak, models.DO_NOTHING, blank=True, null=True)
    weight_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    weight_unit_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    quantity_break = models.ForeignKey(QuantityBreak, models.DO_NOTHING, related_name='shipmentcostestimate_quantity_break_set', blank=True, null=True)
    quantity_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='shipmentcostestimate_quantity_uom_set', blank=True, null=True)
    quantity_unit_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    price_break = models.ForeignKey(QuantityBreak, models.DO_NOTHING, related_name='shipmentcostestimate_price_break_set', blank=True, null=True)
    price_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='shipmentcostestimate_price_uom_set', blank=True, null=True)
    price_unit_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    order_flat_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    order_price_percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    order_item_flat_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    shipping_price_percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_feature_group_id = models.CharField(max_length=20, blank=True, null=True)
    oversize_unit = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    oversize_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    feature_percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    feature_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_cost_estimate'


class ShipmentGatewayConfig(models.Model):
    shipment_gateway_config_id = models.CharField(primary_key=True, max_length=20)
    shipment_gateway_conf_type = models.ForeignKey('ShipmentGatewayConfigType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_gateway_config'


class ShipmentGatewayConfigType(models.Model):
    shipment_gateway_conf_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_gateway_config_type'


class ShipmentGatewayDhl(models.Model):
    shipment_gateway_config = models.OneToOneField(ShipmentGatewayConfig, models.DO_NOTHING, primary_key=True)
    connect_url = models.CharField(max_length=255, blank=True, null=True)
    connect_timeout = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    head_version = models.CharField(max_length=60, blank=True, null=True)
    head_action = models.CharField(max_length=255, blank=True, null=True)
    access_user_id = models.CharField(max_length=255, blank=True, null=True)
    access_password = models.CharField(max_length=255, blank=True, null=True)
    access_account_nbr = models.CharField(max_length=255, blank=True, null=True)
    access_shipping_key = models.CharField(max_length=255, blank=True, null=True)
    label_image_format = models.CharField(max_length=60, blank=True, null=True)
    rate_estimate_template = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_gateway_dhl'


class ShipmentGatewayFedex(models.Model):
    shipment_gateway_config = models.OneToOneField(ShipmentGatewayConfig, models.DO_NOTHING, primary_key=True)
    connect_url = models.CharField(max_length=255, blank=True, null=True)
    connect_soap_url = models.CharField(max_length=255, blank=True, null=True)
    connect_timeout = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    access_account_nbr = models.CharField(max_length=255, blank=True, null=True)
    access_meter_number = models.CharField(max_length=255, blank=True, null=True)
    access_user_key = models.CharField(max_length=255, blank=True, null=True)
    access_user_pwd = models.CharField(max_length=255, blank=True, null=True)
    label_image_type = models.CharField(max_length=60, blank=True, null=True)
    default_dropoff_type = models.CharField(max_length=255, blank=True, null=True)
    default_packaging_type = models.CharField(max_length=255, blank=True, null=True)
    template_shipment = models.CharField(max_length=255, blank=True, null=True)
    template_subscription = models.CharField(max_length=255, blank=True, null=True)
    rate_estimate_template = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_gateway_fedex'


class ShipmentGatewayUps(models.Model):
    shipment_gateway_config = models.OneToOneField(ShipmentGatewayConfig, models.DO_NOTHING, primary_key=True)
    connect_url = models.CharField(max_length=255, blank=True, null=True)
    connect_timeout = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    shipper_number = models.CharField(max_length=255, blank=True, null=True)
    bill_shipper_account_number = models.CharField(max_length=255, blank=True, null=True)
    access_license_number = models.CharField(max_length=255, blank=True, null=True)
    access_user_id = models.CharField(max_length=255, blank=True, null=True)
    access_password = models.CharField(max_length=255, blank=True, null=True)
    save_cert_info = models.CharField(max_length=60, blank=True, null=True)
    save_cert_path = models.CharField(max_length=255, blank=True, null=True)
    shipper_pickup_type = models.CharField(max_length=60, blank=True, null=True)
    customer_classification = models.CharField(max_length=60, blank=True, null=True)
    max_estimate_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    min_estimate_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cod_allow_cod = models.CharField(max_length=255, blank=True, null=True)
    cod_surcharge_amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    cod_surcharge_currency_uom_id = models.CharField(max_length=60, blank=True, null=True)
    cod_surcharge_apply_to_package = models.CharField(max_length=60, blank=True, null=True)
    cod_funds_code = models.CharField(max_length=60, blank=True, null=True)
    default_return_label_memo = models.CharField(max_length=255, blank=True, null=True)
    default_return_label_subject = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_gateway_ups'


class ShipmentGatewayUsps(models.Model):
    shipment_gateway_config = models.OneToOneField(ShipmentGatewayConfig, models.DO_NOTHING, primary_key=True)
    connect_url = models.CharField(max_length=255, blank=True, null=True)
    connect_url_labels = models.CharField(max_length=255, blank=True, null=True)
    connect_timeout = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    access_user_id = models.CharField(max_length=255, blank=True, null=True)
    access_password = models.CharField(max_length=255, blank=True, null=True)
    max_estimate_weight = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    test = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_gateway_usps'


class ShipmentItem(models.Model):
    shipment = models.OneToOneField(Shipment, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, shipment_item_seq_id) found, that is not supported. The first column is selected.
    shipment_item_seq_id = models.CharField(max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    shipment_content_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_item'
        unique_together = (('shipment', 'shipment_item_seq_id'),)


class ShipmentItemBilling(models.Model):
    shipment = models.OneToOneField(ShipmentItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, shipment_item_seq_id, invoice_id, invoice_item_seq_id) found, that is not supported. The first column is selected.
    shipment_item_seq_id = models.CharField(max_length=20)
    invoice = models.ForeignKey(InvoiceItem, models.DO_NOTHING)
    invoice_item_seq_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_item_billing'
        unique_together = (('shipment', 'shipment_item_seq_id', 'invoice', 'invoice_item_seq_id'),)


class ShipmentItemFeature(models.Model):
    shipment = models.OneToOneField(ShipmentItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, shipment_item_seq_id, product_feature_id) found, that is not supported. The first column is selected.
    shipment_item_seq_id = models.CharField(max_length=20)
    product_feature = models.ForeignKey(ProductFeature, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_item_feature'
        unique_together = (('shipment', 'shipment_item_seq_id', 'product_feature'),)


class ShipmentMethodType(models.Model):
    shipment_method_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_method_type'


class ShipmentPackage(models.Model):
    shipment = models.OneToOneField(Shipment, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, shipment_package_seq_id) found, that is not supported. The first column is selected.
    shipment_package_seq_id = models.CharField(max_length=20)
    shipment_box_type = models.ForeignKey(ShipmentBoxType, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    box_length = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    box_height = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    box_width = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    dimension_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    weight_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='shipmentpackage_weight_uom_set', blank=True, null=True)
    insured_value = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_package'
        unique_together = (('shipment', 'shipment_package_seq_id'),)


class ShipmentPackageContent(models.Model):
    shipment = models.OneToOneField(ShipmentPackage, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, shipment_package_seq_id, shipment_item_seq_id) found, that is not supported. The first column is selected.
    shipment_package_seq_id = models.CharField(max_length=20)
    shipment_item_seq_id = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    sub_product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    sub_product_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_package_content'
        unique_together = (('shipment', 'shipment_package_seq_id', 'shipment_item_seq_id'),)


class ShipmentPackageRouteSeg(models.Model):
    shipment = models.OneToOneField(ShipmentPackage, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, shipment_package_seq_id, shipment_route_segment_id) found, that is not supported. The first column is selected.
    shipment_package_seq_id = models.CharField(max_length=20)
    shipment_route_segment_id = models.CharField(max_length=20)
    tracking_code = models.CharField(max_length=60, blank=True, null=True)
    box_number = models.CharField(max_length=60, blank=True, null=True)
    label_image = models.BinaryField(blank=True, null=True)
    label_intl_sign_image = models.BinaryField(blank=True, null=True)
    label_html = models.TextField(blank=True, null=True)
    label_printed = models.CharField(max_length=1, blank=True, null=True)
    international_invoice = models.BinaryField(blank=True, null=True)
    package_transport_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    package_service_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    package_other_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cod_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    insured_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_package_route_seg'
        unique_together = (('shipment', 'shipment_package_seq_id', 'shipment_route_segment_id'),)


class ShipmentReceipt(models.Model):
    receipt_id = models.CharField(primary_key=True, max_length=20)
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    shipment = models.ForeignKey(ShipmentPackage, models.DO_NOTHING, blank=True, null=True)
    shipment_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    shipment_package_seq_id = models.CharField(max_length=20, blank=True, null=True)
    order = models.ForeignKey(OrderItem, models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    return_field = models.ForeignKey(ReturnItem, models.DO_NOTHING, db_column='return_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    return_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    rejection = models.ForeignKey(RejectionReason, models.DO_NOTHING, blank=True, null=True)
    received_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    datetime_received = models.DateTimeField(blank=True, null=True)
    item_description = models.CharField(max_length=255, blank=True, null=True)
    quantity_accepted = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_rejected = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_receipt'


class ShipmentReceiptRole(models.Model):
    receipt = models.OneToOneField(ShipmentReceipt, models.DO_NOTHING, primary_key=True)  # The composite primary key (receipt_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(Party, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_receipt_role'
        unique_together = (('receipt', 'party', 'role_type_id'),)


class ShipmentRouteSegment(models.Model):
    shipment = models.OneToOneField(Shipment, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_id, shipment_route_segment_id) found, that is not supported. The first column is selected.
    shipment_route_segment_id = models.CharField(max_length=20)
    delivery = models.ForeignKey(Delivery, models.DO_NOTHING, blank=True, null=True)
    origin_facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    dest_facility = models.ForeignKey(Facility, models.DO_NOTHING, related_name='shipmentroutesegment_dest_facility_set', blank=True, null=True)
    origin_contact_mech = models.ForeignKey(PostalAddress, models.DO_NOTHING, blank=True, null=True)
    origin_telecom_number = models.ForeignKey('TelecomNumber', models.DO_NOTHING, blank=True, null=True)
    dest_contact_mech = models.ForeignKey(PostalAddress, models.DO_NOTHING, related_name='shipmentroutesegment_dest_contact_mech_set', blank=True, null=True)
    dest_telecom_number = models.ForeignKey('TelecomNumber', models.DO_NOTHING, related_name='shipmentroutesegment_dest_telecom_number_set', blank=True, null=True)
    carrier_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    shipment_method_type = models.ForeignKey(ShipmentMethodType, models.DO_NOTHING, blank=True, null=True)
    carrier_service_status = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    carrier_delivery_zone = models.CharField(max_length=60, blank=True, null=True)
    carrier_restriction_codes = models.CharField(max_length=60, blank=True, null=True)
    carrier_restriction_desc = models.TextField(blank=True, null=True)
    billing_weight = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    billing_weight_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    actual_transport_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_service_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_other_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    actual_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='shipmentroutesegment_currency_uom_set', blank=True, null=True)
    actual_start_date = models.DateTimeField(blank=True, null=True)
    actual_arrival_date = models.DateTimeField(blank=True, null=True)
    estimated_start_date = models.DateTimeField(blank=True, null=True)
    estimated_arrival_date = models.DateTimeField(blank=True, null=True)
    tracking_id_number = models.CharField(max_length=60, blank=True, null=True)
    tracking_digest = models.TextField(blank=True, null=True)
    updated_by_user_login_id = models.CharField(max_length=255, blank=True, null=True)
    last_updated_date = models.DateTimeField(blank=True, null=True)
    home_delivery_type = models.CharField(max_length=20, blank=True, null=True)
    home_delivery_date = models.DateTimeField(blank=True, null=True)
    third_party_account_number = models.CharField(max_length=20, blank=True, null=True)
    third_party_postal_code = models.CharField(max_length=20, blank=True, null=True)
    third_party_country_geo_code = models.CharField(max_length=20, blank=True, null=True)
    ups_high_value_report = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_route_segment'
        unique_together = (('shipment', 'shipment_route_segment_id'),)


class ShipmentStatus(models.Model):
    status = models.OneToOneField('StatusItem', models.DO_NOTHING, primary_key=True)  # The composite primary key (status_id, shipment_id) found, that is not supported. The first column is selected.
    shipment = models.ForeignKey(Shipment, models.DO_NOTHING)
    status_date = models.DateTimeField(blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_status'
        unique_together = (('status', 'shipment'),)


class ShipmentType(models.Model):
    shipment_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_type'


class ShipmentTypeAttr(models.Model):
    shipment_type = models.OneToOneField(ShipmentType, models.DO_NOTHING, primary_key=True)  # The composite primary key (shipment_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipment_type_attr'
        unique_together = (('shipment_type', 'attr_name'),)


class ShippingDocument(models.Model):
    document = models.OneToOneField(Document, models.DO_NOTHING, primary_key=True)
    shipment = models.ForeignKey(ShipmentItem, models.DO_NOTHING, blank=True, null=True)
    shipment_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    shipment_package_seq_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_document'


class ShoppingList(models.Model):
    shopping_list_id = models.CharField(primary_key=True, max_length=20)
    shopping_list_type = models.ForeignKey('ShoppingListType', models.DO_NOTHING, blank=True, null=True)
    parent_shopping_list = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    product_store = models.ForeignKey(ProductStore, models.DO_NOTHING, blank=True, null=True)
    visitor_id = models.CharField(max_length=20, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    list_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_public = models.CharField(max_length=1, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    currency_uom = models.CharField(max_length=20, blank=True, null=True)
    shipment_method_type = models.ForeignKey(CarrierShipmentMethod, models.DO_NOTHING, blank=True, null=True)
    carrier_party_id = models.CharField(max_length=20, blank=True, null=True)
    carrier_role_type_id = models.CharField(max_length=20, blank=True, null=True)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, blank=True, null=True)
    recurrence_info = models.ForeignKey(RecurrenceInfo, models.DO_NOTHING, blank=True, null=True)
    last_ordered_date = models.DateTimeField(blank=True, null=True)
    last_admin_modified = models.DateTimeField(blank=True, null=True)
    product_promo_code = models.ForeignKey(ProductPromoCode, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_list'


class ShoppingListItem(models.Model):
    shopping_list = models.OneToOneField(ShoppingList, models.DO_NOTHING, primary_key=True)  # The composite primary key (shopping_list_id, shopping_list_item_seq_id) found, that is not supported. The first column is selected.
    shopping_list_item_seq_id = models.CharField(max_length=20)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    modified_price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    reserv_start = models.DateTimeField(blank=True, null=True)
    reserv_length = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_persons = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_purchased = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    config_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_list_item'
        unique_together = (('shopping_list', 'shopping_list_item_seq_id'),)


class ShoppingListItemSurvey(models.Model):
    shopping_list = models.OneToOneField(ShoppingList, models.DO_NOTHING, primary_key=True)  # The composite primary key (shopping_list_id, shopping_list_item_seq_id, survey_response_id) found, that is not supported. The first column is selected.
    shopping_list_item_seq_id = models.CharField(max_length=20)
    survey_response = models.ForeignKey('SurveyResponse', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_list_item_survey'
        unique_together = (('shopping_list', 'shopping_list_item_seq_id', 'survey_response'),)


class ShoppingListType(models.Model):
    shopping_list_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_list_type'


class ShoppingListWorkEffort(models.Model):
    shopping_list = models.OneToOneField(ShoppingList, models.DO_NOTHING, primary_key=True)  # The composite primary key (shopping_list_id, work_effort_id) found, that is not supported. The first column is selected.
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_list_work_effort'
        unique_together = (('shopping_list', 'work_effort'),)


class SkillType(models.Model):
    skill_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_type'


class StandardLanguage(models.Model):
    standard_language_id = models.CharField(primary_key=True, max_length=20)
    lang_code3t = models.CharField(max_length=10, blank=True, null=True)
    lang_code3b = models.CharField(max_length=10, blank=True, null=True)
    lang_code2 = models.CharField(max_length=10, blank=True, null=True)
    lang_name = models.CharField(max_length=60, blank=True, null=True)
    lang_family = models.CharField(max_length=60, blank=True, null=True)
    lang_charset = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'standard_language'


class StatusItem(models.Model):
    status_id = models.CharField(primary_key=True, max_length=20)
    status_type = models.ForeignKey('StatusType', models.DO_NOTHING, blank=True, null=True)
    status_code = models.CharField(max_length=60, blank=True, null=True)
    sequence_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_item'


class StatusType(models.Model):
    status_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_type'


class StatusValidChange(models.Model):
    status = models.OneToOneField(StatusItem, models.DO_NOTHING, primary_key=True)  # The composite primary key (status_id, status_id_to) found, that is not supported. The first column is selected.
    status_id_to = models.ForeignKey(StatusItem, models.DO_NOTHING, db_column='status_id_to', related_name='statusvalidchange_status_id_to_set')
    condition_expression = models.CharField(max_length=255, blank=True, null=True)
    transition_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_valid_change'
        unique_together = (('status', 'status_id_to'),)


class Subscription(models.Model):
    subscription_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    subscription_resource = models.ForeignKey('SubscriptionResource', models.DO_NOTHING, blank=True, null=True)
    communication_event_id = models.CharField(max_length=20, blank=True, null=True)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    originated_from_party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    originated_from_role_type = models.ForeignKey(RoleType, models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, related_name='subscription_party_set', blank=True, null=True)
    role_type = models.ForeignKey(RoleType, models.DO_NOTHING, related_name='subscription_role_type_set', blank=True, null=True)
    party_need_id = models.CharField(max_length=20, blank=True, null=True)
    need_type = models.ForeignKey(NeedType, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(OrderItem, models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING, blank=True, null=True)
    subscription_type = models.ForeignKey('SubscriptionType', models.DO_NOTHING, blank=True, null=True)
    external_subscription_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    purchase_from_date = models.DateTimeField(blank=True, null=True)
    purchase_thru_date = models.DateTimeField(blank=True, null=True)
    max_life_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    max_life_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    available_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    available_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='subscription_available_time_uom_set', blank=True, null=True)
    use_count_limit = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    use_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='subscription_use_time_uom_set', blank=True, null=True)
    automatic_extend = models.CharField(max_length=1, blank=True, null=True)
    cancl_autm_ext_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    cancl_autm_ext_time_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='subscription_cancl_autm_ext_time_uom_set', blank=True, null=True)
    grace_period_on_expiry = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    grace_period_on_expiry_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='subscription_grace_period_on_expiry_uom_set', blank=True, null=True)
    expiration_completed_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription'


class SubscriptionActivity(models.Model):
    subscription_activity_id = models.CharField(primary_key=True, max_length=20)
    comments = models.CharField(max_length=255, blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_activity'


class SubscriptionAttribute(models.Model):
    subscription = models.OneToOneField(Subscription, models.DO_NOTHING, primary_key=True)  # The composite primary key (subscription_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_attribute'
        unique_together = (('subscription', 'attr_name'),)


class SubscriptionCommEvent(models.Model):
    subscription = models.OneToOneField(Subscription, models.DO_NOTHING, primary_key=True)  # The composite primary key (subscription_id, communication_event_id) found, that is not supported. The first column is selected.
    communication_event = models.ForeignKey(CommunicationEvent, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_comm_event'
        unique_together = (('subscription', 'communication_event'),)


class SubscriptionFulfillmentPiece(models.Model):
    subscription_activity = models.OneToOneField(SubscriptionActivity, models.DO_NOTHING, primary_key=True)  # The composite primary key (subscription_activity_id, subscription_id) found, that is not supported. The first column is selected.
    subscription = models.ForeignKey(Subscription, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_fulfillment_piece'
        unique_together = (('subscription_activity', 'subscription'),)


class SubscriptionResource(models.Model):
    subscription_resource_id = models.CharField(primary_key=True, max_length=20)
    parent_resource = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    content = models.ForeignKey(Content, models.DO_NOTHING, blank=True, null=True)
    web_site = models.ForeignKey('WebSite', models.DO_NOTHING, blank=True, null=True)
    service_name_on_expiry = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_resource'


class SubscriptionType(models.Model):
    subscription_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_type'


class SubscriptionTypeAttr(models.Model):
    subscription_type = models.OneToOneField(SubscriptionType, models.DO_NOTHING, primary_key=True)  # The composite primary key (subscription_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_type_attr'
        unique_together = (('subscription_type', 'attr_name'),)


class SupplierPrefOrder(models.Model):
    supplier_pref_order_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_pref_order'


class SupplierProduct(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, party_id, currency_uom_id, minimum_order_quantity, available_from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey(Party, models.DO_NOTHING)
    available_from_date = models.DateTimeField()
    available_thru_date = models.DateTimeField(blank=True, null=True)
    supplier_pref_order = models.ForeignKey(SupplierPrefOrder, models.DO_NOTHING, blank=True, null=True)
    supplier_rating_type = models.ForeignKey('SupplierRatingType', models.DO_NOTHING, blank=True, null=True)
    standard_lead_time_days = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    minimum_order_quantity = models.DecimalField(max_digits=18, decimal_places=6)
    order_qty_increments = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    units_included = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    agreement = models.ForeignKey(AgreementItem, models.DO_NOTHING, blank=True, null=True)
    agreement_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    last_price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    shipping_price = models.DecimalField(max_digits=18, decimal_places=3, blank=True, null=True)
    currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, related_name='supplierproduct_currency_uom_set')
    supplier_product_name = models.CharField(max_length=100, blank=True, null=True)
    supplier_product_id = models.CharField(max_length=20, blank=True, null=True)
    can_drop_ship = models.CharField(max_length=1, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_product'
        unique_together = (('product', 'party', 'currency_uom', 'minimum_order_quantity', 'available_from_date'),)


class SupplierProductFeature(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, product_feature_id) found, that is not supported. The first column is selected.
    product_feature = models.ForeignKey(ProductFeature, models.DO_NOTHING)
    description = models.CharField(max_length=100, blank=True, null=True)
    uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)
    id_code = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_product_feature'
        unique_together = (('party', 'product_feature'),)


class SupplierRatingType(models.Model):
    supplier_rating_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_rating_type'


class Survey(models.Model):
    survey_id = models.CharField(primary_key=True, max_length=20)
    survey_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    submit_caption = models.CharField(max_length=60, blank=True, null=True)
    response_service = models.CharField(max_length=255, blank=True, null=True)
    is_anonymous = models.CharField(max_length=1, blank=True, null=True)
    allow_multiple = models.CharField(max_length=1, blank=True, null=True)
    allow_update = models.CharField(max_length=1, blank=True, null=True)
    acro_form_content_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey'


class SurveyApplType(models.Model):
    survey_appl_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_appl_type'


class SurveyMultiResp(models.Model):
    survey = models.OneToOneField(Survey, models.DO_NOTHING, primary_key=True)  # The composite primary key (survey_id, survey_multi_resp_id) found, that is not supported. The first column is selected.
    survey_multi_resp_id = models.CharField(max_length=20)
    multi_resp_title = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_multi_resp'
        unique_together = (('survey', 'survey_multi_resp_id'),)


class SurveyMultiRespColumn(models.Model):
    survey = models.OneToOneField(SurveyMultiResp, models.DO_NOTHING, primary_key=True)  # The composite primary key (survey_id, survey_multi_resp_id, survey_multi_resp_col_id) found, that is not supported. The first column is selected.
    survey_multi_resp_id = models.CharField(max_length=20)
    survey_multi_resp_col_id = models.CharField(max_length=20)
    column_title = models.CharField(max_length=100, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_multi_resp_column'
        unique_together = (('survey', 'survey_multi_resp_id', 'survey_multi_resp_col_id'),)


class SurveyPage(models.Model):
    survey = models.OneToOneField(Survey, models.DO_NOTHING, primary_key=True)  # The composite primary key (survey_id, survey_page_seq_id) found, that is not supported. The first column is selected.
    survey_page_seq_id = models.CharField(max_length=20)
    page_name = models.CharField(max_length=100, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_page'
        unique_together = (('survey', 'survey_page_seq_id'),)


class SurveyQuestion(models.Model):
    survey_question_id = models.CharField(primary_key=True, max_length=20)
    survey_question_category = models.ForeignKey('SurveyQuestionCategory', models.DO_NOTHING, blank=True, null=True)
    survey_question_type = models.ForeignKey('SurveyQuestionType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    enum_type_id = models.CharField(max_length=20, blank=True, null=True)
    geo = models.ForeignKey(Geo, models.DO_NOTHING, blank=True, null=True)
    format_string = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_question'


class SurveyQuestionAppl(models.Model):
    survey = models.OneToOneField(Survey, models.DO_NOTHING, primary_key=True)  # The composite primary key (survey_id, survey_question_id, from_date) found, that is not supported. The first column is selected.
    survey_question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    survey_page_seq_id = models.CharField(max_length=20, blank=True, null=True)
    survey_multi_resp_id = models.CharField(max_length=20, blank=True, null=True)
    survey_multi_resp_col_id = models.CharField(max_length=20, blank=True, null=True)
    required_field = models.CharField(max_length=1, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    external_field_ref = models.CharField(max_length=255, blank=True, null=True)
    with_survey_question = models.ForeignKey('SurveyQuestionOption', models.DO_NOTHING, blank=True, null=True)
    with_survey_option_seq_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_question_appl'
        unique_together = (('survey', 'survey_question', 'from_date'),)


class SurveyQuestionCategory(models.Model):
    survey_question_category_id = models.CharField(primary_key=True, max_length=20)
    parent_category = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_question_category'


class SurveyQuestionOption(models.Model):
    survey_question = models.OneToOneField(SurveyQuestion, models.DO_NOTHING, primary_key=True)  # The composite primary key (survey_question_id, survey_option_seq_id) found, that is not supported. The first column is selected.
    survey_option_seq_id = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    amount_base = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    amount_base_uom_id = models.CharField(max_length=20, blank=True, null=True)
    weight_factor = models.FloatField(blank=True, null=True)
    duration = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    duration_uom_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_question_option'
        unique_together = (('survey_question', 'survey_option_seq_id'),)


class SurveyQuestionType(models.Model):
    survey_question_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_question_type'


class SurveyResponse(models.Model):
    survey_response_id = models.CharField(primary_key=True, max_length=20)
    survey = models.ForeignKey(Survey, models.DO_NOTHING, blank=True, null=True)
    party_id = models.CharField(max_length=20, blank=True, null=True)
    response_date = models.DateTimeField(blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    reference_id = models.CharField(max_length=255, blank=True, null=True)
    general_feedback = models.TextField(blank=True, null=True)
    order_id = models.CharField(max_length=20, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_response'


class SurveyResponseAnswer(models.Model):
    survey_response = models.OneToOneField(SurveyResponse, models.DO_NOTHING, primary_key=True)  # The composite primary key (survey_response_id, survey_question_id, survey_multi_resp_col_id) found, that is not supported. The first column is selected.
    survey_question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)
    survey_multi_resp_col_id = models.CharField(max_length=20)
    survey_multi_resp_id = models.CharField(max_length=20, blank=True, null=True)
    boolean_response = models.CharField(max_length=1, blank=True, null=True)
    currency_response = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    float_response = models.FloatField(blank=True, null=True)
    numeric_response = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    text_response = models.TextField(blank=True, null=True)
    survey_option_seq_id = models.CharField(max_length=20, blank=True, null=True)
    content = models.ForeignKey(Content, models.DO_NOTHING, blank=True, null=True)
    answered_date = models.DateTimeField(blank=True, null=True)
    amount_base = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    amount_base_uom_id = models.CharField(max_length=20, blank=True, null=True)
    weight_factor = models.FloatField(blank=True, null=True)
    duration = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    duration_uom_id = models.CharField(max_length=20, blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_response_answer'
        unique_together = (('survey_response', 'survey_question', 'survey_multi_resp_col_id'),)


class SurveyTrigger(models.Model):
    survey = models.OneToOneField(Survey, models.DO_NOTHING, primary_key=True)  # The composite primary key (survey_id, survey_appl_type_id, from_date) found, that is not supported. The first column is selected.
    survey_appl_type = models.ForeignKey(SurveyApplType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_trigger'
        unique_together = (('survey', 'survey_appl_type', 'from_date'),)


class SystemProperty(models.Model):
    system_resource_id = models.CharField(primary_key=True, max_length=60)  # The composite primary key (system_resource_id, system_property_id) found, that is not supported. The first column is selected.
    system_property_id = models.CharField(max_length=60)
    system_property_value = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_property'
        unique_together = (('system_resource_id', 'system_property_id'),)


class TarpittedLoginView(models.Model):
    view_name_id = models.CharField(primary_key=True, max_length=60)  # The composite primary key (view_name_id, user_login_id) found, that is not supported. The first column is selected.
    user_login_id = models.CharField(max_length=255)
    tarpit_release_date_time = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarpitted_login_view'
        unique_together = (('view_name_id', 'user_login_id'),)


class TaxAuthority(models.Model):
    tax_auth_geo = models.OneToOneField(Geo, models.DO_NOTHING, primary_key=True)  # The composite primary key (tax_auth_geo_id, tax_auth_party_id) found, that is not supported. The first column is selected.
    tax_auth_party = models.ForeignKey(Party, models.DO_NOTHING)
    require_tax_id_for_exemption = models.CharField(max_length=1, blank=True, null=True)
    tax_id_format_pattern = models.CharField(max_length=255, blank=True, null=True)
    include_tax_in_price = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_authority'
        unique_together = (('tax_auth_geo', 'tax_auth_party'),)


class TaxAuthorityAssoc(models.Model):
    tax_auth_geo = models.OneToOneField(TaxAuthority, models.DO_NOTHING, primary_key=True)  # The composite primary key (tax_auth_geo_id, tax_auth_party_id, to_tax_auth_geo_id, to_tax_auth_party_id, from_date) found, that is not supported. The first column is selected.
    tax_auth_party_id = models.CharField(max_length=20)
    to_tax_auth_geo = models.ForeignKey(TaxAuthority, models.DO_NOTHING, related_name='taxauthorityassoc_to_tax_auth_geo_set')
    to_tax_auth_party_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    tax_authority_assoc_type = models.ForeignKey('TaxAuthorityAssocType', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_authority_assoc'
        unique_together = (('tax_auth_geo', 'tax_auth_party_id', 'to_tax_auth_geo', 'to_tax_auth_party_id', 'from_date'),)


class TaxAuthorityAssocType(models.Model):
    tax_authority_assoc_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_authority_assoc_type'


class TaxAuthorityCategory(models.Model):
    tax_auth_geo = models.OneToOneField(TaxAuthority, models.DO_NOTHING, primary_key=True)  # The composite primary key (tax_auth_geo_id, tax_auth_party_id, product_category_id) found, that is not supported. The first column is selected.
    tax_auth_party_id = models.CharField(max_length=20)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_authority_category'
        unique_together = (('tax_auth_geo', 'tax_auth_party_id', 'product_category'),)


class TaxAuthorityGlAccount(models.Model):
    tax_auth_geo = models.OneToOneField(TaxAuthority, models.DO_NOTHING, primary_key=True)  # The composite primary key (tax_auth_geo_id, tax_auth_party_id, organization_party_id) found, that is not supported. The first column is selected.
    tax_auth_party_id = models.CharField(max_length=20)
    organization_party = models.ForeignKey(Party, models.DO_NOTHING)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_authority_gl_account'
        unique_together = (('tax_auth_geo', 'tax_auth_party_id', 'organization_party'),)


class TaxAuthorityRateProduct(models.Model):
    tax_authority_rate_seq_id = models.CharField(primary_key=True, max_length=20)
    tax_auth_geo = models.ForeignKey(TaxAuthority, models.DO_NOTHING, blank=True, null=True)
    tax_auth_party_id = models.CharField(max_length=20, blank=True, null=True)
    tax_authority_rate_type = models.ForeignKey('TaxAuthorityRateType', models.DO_NOTHING, blank=True, null=True)
    product_store = models.ForeignKey(ProductStore, models.DO_NOTHING, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    title_transfer_enum_id = models.CharField(max_length=20, blank=True, null=True)
    min_item_price = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    min_purchase = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tax_shipping = models.CharField(max_length=1, blank=True, null=True)
    tax_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    tax_promotions = models.CharField(max_length=1, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    is_tax_in_shipping_price = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_authority_rate_product'


class TaxAuthorityRateType(models.Model):
    tax_authority_rate_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_authority_rate_type'


class TechDataCalendar(models.Model):
    calendar_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    calendar_week = models.ForeignKey('TechDataCalendarWeek', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tech_data_calendar'


class TechDataCalendarExcDay(models.Model):
    calendar = models.OneToOneField(TechDataCalendar, models.DO_NOTHING, primary_key=True)  # The composite primary key (calendar_id, exception_date_start_time) found, that is not supported. The first column is selected.
    exception_date_start_time = models.DateTimeField()
    exception_capacity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    used_capacity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tech_data_calendar_exc_day'
        unique_together = (('calendar', 'exception_date_start_time'),)


class TechDataCalendarExcWeek(models.Model):
    calendar = models.OneToOneField(TechDataCalendar, models.DO_NOTHING, primary_key=True)  # The composite primary key (calendar_id, exception_date_start) found, that is not supported. The first column is selected.
    exception_date_start = models.DateField()
    calendar_week = models.ForeignKey('TechDataCalendarWeek', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tech_data_calendar_exc_week'
        unique_together = (('calendar', 'exception_date_start'),)


class TechDataCalendarWeek(models.Model):
    calendar_week_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    monday_start_time = models.TimeField(blank=True, null=True)
    monday_capacity = models.FloatField(blank=True, null=True)
    tuesday_start_time = models.TimeField(blank=True, null=True)
    tuesday_capacity = models.FloatField(blank=True, null=True)
    wednesday_start_time = models.TimeField(blank=True, null=True)
    wednesday_capacity = models.FloatField(blank=True, null=True)
    thursday_start_time = models.TimeField(blank=True, null=True)
    thursday_capacity = models.FloatField(blank=True, null=True)
    friday_start_time = models.TimeField(blank=True, null=True)
    friday_capacity = models.FloatField(blank=True, null=True)
    saturday_start_time = models.TimeField(blank=True, null=True)
    saturday_capacity = models.FloatField(blank=True, null=True)
    sunday_start_time = models.TimeField(blank=True, null=True)
    sunday_capacity = models.FloatField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tech_data_calendar_week'


class TelecomNumber(models.Model):
    contact_mech = models.OneToOneField(ContactMech, models.DO_NOTHING, primary_key=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    area_code = models.CharField(max_length=10, blank=True, null=True)
    contact_number = models.CharField(max_length=60, blank=True, null=True)
    ask_for_name = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telecom_number'


class TemporalExpression(models.Model):
    temp_expr_id = models.CharField(primary_key=True, max_length=20)
    temp_expr_type_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    date1 = models.DateTimeField(blank=True, null=True)
    date2 = models.DateTimeField(blank=True, null=True)
    integer1 = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    integer2 = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    string1 = models.CharField(max_length=20, blank=True, null=True)
    string2 = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporal_expression'


class TemporalExpressionAssoc(models.Model):
    from_temp_expr = models.OneToOneField(TemporalExpression, models.DO_NOTHING, primary_key=True)  # The composite primary key (from_temp_expr_id, to_temp_expr_id) found, that is not supported. The first column is selected.
    to_temp_expr = models.ForeignKey(TemporalExpression, models.DO_NOTHING, related_name='temporalexpressionassoc_to_temp_expr_set')
    expr_assoc_type = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporal_expression_assoc'
        unique_together = (('from_temp_expr', 'to_temp_expr'),)


class TermType(models.Model):
    term_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'term_type'


class TermTypeAttr(models.Model):
    term_type = models.OneToOneField(TermType, models.DO_NOTHING, primary_key=True)  # The composite primary key (term_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'term_type_attr'
        unique_together = (('term_type', 'attr_name'),)


class TerminationReason(models.Model):
    termination_reason_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'termination_reason'


class TerminationType(models.Model):
    termination_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'termination_type'


class TestBlob(models.Model):
    test_blob_id = models.CharField(primary_key=True, max_length=20)
    test_blob_field = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_blob'


class TestFieldType(models.Model):
    test_field_type_id = models.CharField(primary_key=True, max_length=20)
    blob_field = models.BinaryField(blank=True, null=True)
    byte_array_field = models.BinaryField(blank=True, null=True)
    object_field = models.BinaryField(blank=True, null=True)
    date_field = models.DateField(blank=True, null=True)
    time_field = models.TimeField(blank=True, null=True)
    date_time_field = models.DateTimeField(blank=True, null=True)
    fixed_point_field = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    floating_point_field = models.FloatField(blank=True, null=True)
    numeric_field = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    clob_field = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_field_type'


class Testing(models.Model):
    testing_id = models.CharField(primary_key=True, max_length=20)
    testing_type = models.ForeignKey('TestingType', models.DO_NOTHING, blank=True, null=True)
    testing_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    testing_size = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    testing_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing'


class TestingCrypto(models.Model):
    testing_crypto_id = models.CharField(primary_key=True, max_length=20)
    testing_crypto_type_id = models.CharField(max_length=20, blank=True, null=True)
    unencrypted_value = models.CharField(max_length=255, blank=True, null=True)
    encrypted_value = models.CharField(max_length=255, blank=True, null=True)
    salted_encrypted_value = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_crypto'


class TestingItem(models.Model):
    testing = models.OneToOneField(Testing, models.DO_NOTHING, primary_key=True)  # The composite primary key (testing_id, testing_seq_id) found, that is not supported. The first column is selected.
    testing_seq_id = models.CharField(max_length=20)
    testing_history = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_item'
        unique_together = (('testing', 'testing_seq_id'),)


class TestingNode(models.Model):
    testing_node_id = models.CharField(primary_key=True, max_length=20)
    primary_parent_node = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_node'


class TestingNodeMember(models.Model):
    testing_node = models.OneToOneField(TestingNode, models.DO_NOTHING, primary_key=True)  # The composite primary key (testing_node_id, testing_id, from_date) found, that is not supported. The first column is selected.
    testing = models.ForeignKey(Testing, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    extend_from_date = models.DateTimeField(blank=True, null=True)
    extend_thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_node_member'
        unique_together = (('testing_node', 'testing', 'from_date'),)


class TestingRemoveAll(models.Model):
    testing_remove_all_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_remove_all'


class TestingStatus(models.Model):
    testing_status_id = models.CharField(primary_key=True, max_length=20)
    testing_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    status_date = models.DateTimeField(blank=True, null=True)
    change_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_status'


class TestingSubtype(models.Model):
    testing_type_id = models.CharField(primary_key=True, max_length=20)
    subtype_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_subtype'


class TestingType(models.Model):
    testing_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testing_type'


class ThirdPartyLogin(models.Model):
    product_store = models.OneToOneField(ProductStore, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_store_id, login_meth_type_id, login_provider_id, from_date) found, that is not supported. The first column is selected.
    login_meth_type_id = models.CharField(max_length=20)
    login_provider_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'third_party_login'
        unique_together = (('product_store', 'login_meth_type_id', 'login_provider_id', 'from_date'),)


class TimeEntry(models.Model):
    time_entry_id = models.CharField(primary_key=True, max_length=20)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    rate_type = models.ForeignKey(RateType, models.DO_NOTHING, blank=True, null=True)
    work_effort = models.ForeignKey('WorkEffort', models.DO_NOTHING, blank=True, null=True)
    timesheet = models.ForeignKey('Timesheet', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(InvoiceItem, models.DO_NOTHING, blank=True, null=True)
    invoice_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    plan_hours = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_entry'


class Timesheet(models.Model):
    timesheet_id = models.CharField(primary_key=True, max_length=20)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    client_party = models.ForeignKey(Party, models.DO_NOTHING, related_name='timesheet_client_party_set', blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    approved_by_user_login = models.ForeignKey('UserLogin', models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timesheet'


class TimesheetRole(models.Model):
    timesheet = models.OneToOneField(Timesheet, models.DO_NOTHING, primary_key=True)  # The composite primary key (timesheet_id, party_id, role_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timesheet_role'
        unique_together = (('timesheet', 'party', 'role_type_id'),)


class TrackingCode(models.Model):
    tracking_code_id = models.CharField(primary_key=True, max_length=20)
    tracking_code_type = models.ForeignKey('TrackingCodeType', models.DO_NOTHING, blank=True, null=True)
    marketing_campaign = models.ForeignKey(MarketingCampaign, models.DO_NOTHING, blank=True, null=True)
    redirect_url = models.CharField(max_length=2000, blank=True, null=True)
    override_logo = models.CharField(max_length=2000, blank=True, null=True)
    override_css = models.CharField(max_length=2000, blank=True, null=True)
    prod_catalog_id = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    trackable_lifetime = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    billable_lifetime = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    group_id = models.CharField(max_length=20, blank=True, null=True)
    subgroup_id = models.CharField(max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracking_code'


class TrackingCodeOrder(models.Model):
    order = models.OneToOneField(OrderHeader, models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, tracking_code_type_id) found, that is not supported. The first column is selected.
    tracking_code_type = models.ForeignKey('TrackingCodeType', models.DO_NOTHING)
    tracking_code = models.ForeignKey(TrackingCode, models.DO_NOTHING, blank=True, null=True)
    is_billable = models.CharField(max_length=1, blank=True, null=True)
    site_id = models.CharField(max_length=255, blank=True, null=True)
    has_exported = models.CharField(max_length=1, blank=True, null=True)
    affiliate_referred_time_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracking_code_order'
        unique_together = (('order', 'tracking_code_type'),)


class TrackingCodeOrderReturn(models.Model):
    return_field = models.OneToOneField(ReturnHeader, models.DO_NOTHING, db_column='return_id', primary_key=True)  # Field renamed because it was a Python reserved word. The composite primary key (return_id, order_id, tracking_code_type_id) found, that is not supported. The first column is selected.
    order = models.ForeignKey(OrderHeader, models.DO_NOTHING)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    tracking_code_type = models.ForeignKey('TrackingCodeType', models.DO_NOTHING)
    tracking_code = models.ForeignKey(TrackingCode, models.DO_NOTHING, blank=True, null=True)
    is_billable = models.CharField(max_length=1, blank=True, null=True)
    site_id = models.CharField(max_length=255, blank=True, null=True)
    has_exported = models.CharField(max_length=1, blank=True, null=True)
    affiliate_referred_time_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracking_code_order_return'
        unique_together = (('return_field', 'order', 'tracking_code_type'),)


class TrackingCodeType(models.Model):
    tracking_code_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracking_code_type'


class TrackingCodeVisit(models.Model):
    tracking_code = models.OneToOneField(TrackingCode, models.DO_NOTHING, primary_key=True)  # The composite primary key (tracking_code_id, visit_id, from_date) found, that is not supported. The first column is selected.
    visit_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    source_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracking_code_visit'
        unique_together = (('tracking_code', 'visit_id', 'from_date'),)


class TrainingClassType(models.Model):
    training_class_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_class_type'


class TrainingRequest(models.Model):
    training_request_id = models.CharField(primary_key=True, max_length=20)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_request'


class UnemploymentClaim(models.Model):
    unemployment_claim_id = models.CharField(primary_key=True, max_length=20)
    unemployment_claim_date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status_id = models.CharField(max_length=20, blank=True, null=True)
    party_id_from = models.CharField(max_length=20, blank=True, null=True)
    party_id_to = models.CharField(max_length=20, blank=True, null=True)
    role_type_id_from = models.CharField(max_length=20, blank=True, null=True)
    role_type_id_to = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unemployment_claim'


class Uom(models.Model):
    uom_id = models.CharField(primary_key=True, max_length=20)
    uom_type = models.ForeignKey('UomType', models.DO_NOTHING, blank=True, null=True)
    abbreviation = models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom'


class UomConversion(models.Model):
    uom = models.OneToOneField(Uom, models.DO_NOTHING, primary_key=True)  # The composite primary key (uom_id, uom_id_to) found, that is not supported. The first column is selected.
    uom_id_to = models.ForeignKey(Uom, models.DO_NOTHING, db_column='uom_id_to', related_name='uomconversion_uom_id_to_set')
    conversion_factor = models.FloatField(blank=True, null=True)
    custom_method = models.ForeignKey(CustomMethod, models.DO_NOTHING, blank=True, null=True)
    decimal_scale = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    rounding_mode = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_conversion'
        unique_together = (('uom', 'uom_id_to'),)


class UomConversionDated(models.Model):
    uom = models.OneToOneField(Uom, models.DO_NOTHING, primary_key=True)  # The composite primary key (uom_id, uom_id_to, from_date) found, that is not supported. The first column is selected.
    uom_id_to = models.ForeignKey(Uom, models.DO_NOTHING, db_column='uom_id_to', related_name='uomconversiondated_uom_id_to_set')
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    conversion_factor = models.FloatField(blank=True, null=True)
    custom_method = models.ForeignKey(CustomMethod, models.DO_NOTHING, blank=True, null=True)
    decimal_scale = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    rounding_mode = models.CharField(max_length=20, blank=True, null=True)
    purpose_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_conversion_dated'
        unique_together = (('uom', 'uom_id_to', 'from_date'),)


class UomGroup(models.Model):
    uom_group_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (uom_group_id, uom_id) found, that is not supported. The first column is selected.
    uom = models.ForeignKey(Uom, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_group'
        unique_together = (('uom_group_id', 'uom'),)


class UomType(models.Model):
    uom_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_type'


class UserAgent(models.Model):
    user_agent_id = models.CharField(primary_key=True, max_length=20)
    browser_type = models.ForeignKey(BrowserType, models.DO_NOTHING, blank=True, null=True)
    platform_type = models.ForeignKey(PlatformType, models.DO_NOTHING, blank=True, null=True)
    protocol_type = models.ForeignKey(ProtocolType, models.DO_NOTHING, blank=True, null=True)
    user_agent_type = models.ForeignKey('UserAgentType', models.DO_NOTHING, blank=True, null=True)
    user_agent_method_type = models.ForeignKey('UserAgentMethodType', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_agent'


class UserAgentMethodType(models.Model):
    user_agent_method_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_agent_method_type'


class UserAgentType(models.Model):
    user_agent_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_agent_type'


class UserLogin(models.Model):
    user_login_id = models.CharField(primary_key=True, max_length=255)
    current_password = models.CharField(max_length=60, blank=True, null=True)
    password_hint = models.CharField(max_length=255, blank=True, null=True)
    is_system = models.CharField(max_length=1, blank=True, null=True)
    enabled = models.CharField(max_length=1, blank=True, null=True)
    has_logged_out = models.CharField(max_length=1, blank=True, null=True)
    require_password_change = models.CharField(max_length=1, blank=True, null=True)
    last_currency_uom = models.CharField(max_length=20, blank=True, null=True)
    last_locale = models.CharField(max_length=10, blank=True, null=True)
    last_time_zone = models.CharField(max_length=60, blank=True, null=True)
    disabled_date_time = models.DateTimeField(blank=True, null=True)
    successive_failed_logins = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    external_auth_id = models.CharField(max_length=255, blank=True, null=True)
    user_ldap_dn = models.CharField(max_length=255, blank=True, null=True)
    disabled_by = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login'


class UserLoginHistory(models.Model):
    user_login = models.OneToOneField(UserLogin, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_login_id, from_date) found, that is not supported. The first column is selected.
    visit_id = models.CharField(max_length=20, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    password_used = models.CharField(max_length=255, blank=True, null=True)
    successful_login = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login_history'
        unique_together = (('user_login', 'from_date'),)


class UserLoginPasswordHistory(models.Model):
    user_login = models.OneToOneField(UserLogin, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_login_id, from_date) found, that is not supported. The first column is selected.
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    current_password = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login_password_history'
        unique_together = (('user_login', 'from_date'),)


class UserLoginSecurityGroup(models.Model):
    user_login = models.OneToOneField(UserLogin, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_login_id, group_id, from_date) found, that is not supported. The first column is selected.
    group = models.ForeignKey(SecurityGroup, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login_security_group'
        unique_together = (('user_login', 'group', 'from_date'),)


class UserLoginSecurityQuestion(models.Model):
    question_enum = models.OneToOneField(Enumeration, models.DO_NOTHING, primary_key=True)  # The composite primary key (question_enum_id, user_login_id) found, that is not supported. The first column is selected.
    user_login = models.ForeignKey(UserLogin, models.DO_NOTHING)
    security_answer = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login_security_question'
        unique_together = (('question_enum', 'user_login'),)


class UserLoginSession(models.Model):
    user_login = models.OneToOneField(UserLogin, models.DO_NOTHING, primary_key=True)
    saved_date = models.DateTimeField(blank=True, null=True)
    session_data = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login_session'


class UserPrefGroupType(models.Model):
    user_pref_group_type_id = models.CharField(primary_key=True, max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_pref_group_type'


class UserPreference(models.Model):
    user_login_id = models.CharField(primary_key=True, max_length=255)  # The composite primary key (user_login_id, user_pref_type_id) found, that is not supported. The first column is selected.
    user_pref_type_id = models.CharField(max_length=60)
    user_pref_group_type_id = models.CharField(max_length=60, blank=True, null=True)
    user_pref_value = models.CharField(max_length=255, blank=True, null=True)
    user_pref_data_type = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_preference'
        unique_together = (('user_login_id', 'user_pref_type_id'),)


class ValidContactMechRole(models.Model):
    role_type = models.OneToOneField(RoleType, models.DO_NOTHING, primary_key=True)  # The composite primary key (role_type_id, contact_mech_type_id) found, that is not supported. The first column is selected.
    contact_mech_type = models.ForeignKey(ContactMechType, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valid_contact_mech_role'
        unique_together = (('role_type', 'contact_mech_type'),)


class ValidResponsibility(models.Model):
    empl_position_type = models.OneToOneField(EmplPositionType, models.DO_NOTHING, primary_key=True)  # The composite primary key (empl_position_type_id, responsibility_type_id, from_date) found, that is not supported. The first column is selected.
    responsibility_type = models.ForeignKey(ResponsibilityType, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valid_responsibility'
        unique_together = (('empl_position_type', 'responsibility_type', 'from_date'),)


class ValueLinkFulfillment(models.Model):
    fulfillment_id = models.CharField(primary_key=True, max_length=20)
    type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    merchant_id = models.CharField(max_length=255, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(OrderItem, models.DO_NOTHING, blank=True, null=True)
    order_item_seq_id = models.CharField(max_length=20, blank=True, null=True)
    survey_response = models.ForeignKey(SurveyResponse, models.DO_NOTHING, blank=True, null=True)
    card_number = models.CharField(max_length=60, blank=True, null=True)
    pin_number = models.CharField(max_length=60, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    response_code = models.CharField(max_length=60, blank=True, null=True)
    reference_num = models.CharField(max_length=60, blank=True, null=True)
    auth_code = models.CharField(max_length=60, blank=True, null=True)
    fulfillment_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'value_link_fulfillment'


class ValueLinkKey(models.Model):
    merchant_id = models.CharField(primary_key=True, max_length=255)
    public_key = models.TextField(blank=True, null=True)
    private_key = models.TextField(blank=True, null=True)
    exchange_key = models.TextField(blank=True, null=True)
    working_key = models.TextField(blank=True, null=True)
    working_key_index = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_working_key = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_terminal = models.CharField(max_length=60, blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_terminal = models.CharField(max_length=60, blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'value_link_key'


class VarianceReason(models.Model):
    variance_reason_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variance_reason'


class VarianceReasonGlAccount(models.Model):
    variance_reason = models.OneToOneField(VarianceReason, models.DO_NOTHING, primary_key=True)  # The composite primary key (variance_reason_id, organization_party_id) found, that is not supported. The first column is selected.
    organization_party = models.ForeignKey(Party, models.DO_NOTHING)
    gl_account = models.ForeignKey(GlAccount, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variance_reason_gl_account'
        unique_together = (('variance_reason', 'organization_party'),)


class Vendor(models.Model):
    party = models.OneToOneField(Party, models.DO_NOTHING, primary_key=True)
    manifest_company_name = models.CharField(max_length=100, blank=True, null=True)
    manifest_company_title = models.CharField(max_length=100, blank=True, null=True)
    manifest_logo_url = models.CharField(max_length=2000, blank=True, null=True)
    manifest_policies = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor'


class VendorProduct(models.Model):
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)  # The composite primary key (product_id, vendor_party_id, product_store_group_id) found, that is not supported. The first column is selected.
    vendor_party = models.ForeignKey(Party, models.DO_NOTHING)
    product_store_group = models.ForeignKey(ProductStoreGroup, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_product'
        unique_together = (('product', 'vendor_party', 'product_store_group'),)


class VideoDataResource(models.Model):
    data_resource = models.OneToOneField(DataResource, models.DO_NOTHING, primary_key=True)
    video_data = models.BinaryField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_data_resource'


class Visit(models.Model):
    visit_id = models.CharField(primary_key=True, max_length=20)
    visitor = models.ForeignKey('Visitor', models.DO_NOTHING, blank=True, null=True)
    user_login_id = models.CharField(max_length=255, blank=True, null=True)
    user_created = models.CharField(max_length=1, blank=True, null=True)
    session_id = models.CharField(max_length=255, blank=True, null=True)
    server_ip_address = models.CharField(max_length=20, blank=True, null=True)
    server_host_name = models.CharField(max_length=255, blank=True, null=True)
    webapp_name = models.CharField(max_length=60, blank=True, null=True)
    initial_locale = models.CharField(max_length=60, blank=True, null=True)
    initial_request = models.CharField(max_length=2000, blank=True, null=True)
    initial_referrer = models.CharField(max_length=2000, blank=True, null=True)
    initial_user_agent = models.CharField(max_length=255, blank=True, null=True)
    user_agent = models.ForeignKey(UserAgent, models.DO_NOTHING, blank=True, null=True)
    client_ip_address = models.CharField(max_length=60, blank=True, null=True)
    client_host_name = models.CharField(max_length=255, blank=True, null=True)
    client_user = models.CharField(max_length=60, blank=True, null=True)
    client_ip_isp_name = models.CharField(max_length=60, blank=True, null=True)
    client_ip_postal_code = models.CharField(max_length=60, blank=True, null=True)
    cookie = models.CharField(max_length=60, blank=True, null=True)
    from_date = models.DateTimeField(blank=True, null=True)
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    client_ip_state_prov_geo_id = models.CharField(max_length=20, blank=True, null=True)
    client_ip_country_geo_id = models.CharField(max_length=20, blank=True, null=True)
    contact_mech_id = models.CharField(max_length=20, blank=True, null=True)
    party_id = models.CharField(max_length=20, blank=True, null=True)
    role_type_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit'


class Visitor(models.Model):
    visitor_id = models.CharField(primary_key=True, max_length=20)
    user_login = models.ForeignKey(UserLogin, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    party_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visitor'


class VisualTheme(models.Model):
    visual_theme_id = models.CharField(primary_key=True, max_length=20)
    visual_theme_set = models.ForeignKey('VisualThemeSet', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visual_theme'


class VisualThemeResource(models.Model):
    visual_theme = models.OneToOneField(VisualTheme, models.DO_NOTHING, primary_key=True)  # The composite primary key (visual_theme_id, resource_type_enum_id, sequence_id) found, that is not supported. The first column is selected.
    resource_type_enum = models.ForeignKey(Enumeration, models.DO_NOTHING)
    sequence_id = models.CharField(max_length=20)
    resource_value = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visual_theme_resource'
        unique_together = (('visual_theme', 'resource_type_enum', 'sequence_id'),)


class VisualThemeSet(models.Model):
    visual_theme_set_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visual_theme_set'


class WebAnalyticsConfig(models.Model):
    web_site_id = models.CharField(primary_key=True, max_length=20)  # The composite primary key (web_site_id, web_analytics_type_id) found, that is not supported. The first column is selected.
    web_analytics_type_id = models.CharField(max_length=20)
    web_analytics_code = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_analytics_config'
        unique_together = (('web_site_id', 'web_analytics_type_id'),)


class WebAnalyticsType(models.Model):
    web_analytics_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_analytics_type'


class WebPage(models.Model):
    web_page_id = models.CharField(primary_key=True, max_length=20)
    page_name = models.CharField(max_length=100, blank=True, null=True)
    web_site = models.ForeignKey('WebSite', models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    content = models.ForeignKey(Content, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_page'


class WebPreferenceType(models.Model):
    web_preference_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_preference_type'


class WebSite(models.Model):
    web_site_id = models.CharField(primary_key=True, max_length=20)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    http_host = models.CharField(max_length=255, blank=True, null=True)
    http_port = models.CharField(max_length=10, blank=True, null=True)
    https_host = models.CharField(max_length=255, blank=True, null=True)
    https_port = models.CharField(max_length=10, blank=True, null=True)
    enable_https = models.CharField(max_length=1, blank=True, null=True)
    standard_content_prefix = models.CharField(max_length=2000, blank=True, null=True)
    secure_content_prefix = models.CharField(max_length=2000, blank=True, null=True)
    cookie_domain = models.CharField(max_length=255, blank=True, null=True)
    visual_theme_set = models.ForeignKey(VisualThemeSet, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    product_store = models.ForeignKey(ProductStore, models.DO_NOTHING, blank=True, null=True)
    allow_product_store_change = models.CharField(max_length=1, blank=True, null=True)
    hosted_path_alias = models.CharField(max_length=60, blank=True, null=True)
    is_default = models.CharField(max_length=1, blank=True, null=True)
    display_maintenance_page = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_site'


class WebSiteContactList(models.Model):
    web_site = models.OneToOneField(WebSite, models.DO_NOTHING, primary_key=True)  # The composite primary key (web_site_id, contact_list_id, from_date) found, that is not supported. The first column is selected.
    contact_list = models.ForeignKey(ContactList, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_site_contact_list'
        unique_together = (('web_site', 'contact_list', 'from_date'),)


class WebSiteContent(models.Model):
    web_site = models.OneToOneField(WebSite, models.DO_NOTHING, primary_key=True)  # The composite primary key (web_site_id, content_id, web_site_content_type_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    web_site_content_type = models.ForeignKey('WebSiteContentType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_site_content'
        unique_together = (('web_site', 'content', 'web_site_content_type', 'from_date'),)


class WebSiteContentType(models.Model):
    web_site_content_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_site_content_type'


class WebSitePathAlias(models.Model):
    web_site = models.OneToOneField(WebSite, models.DO_NOTHING, primary_key=True)  # The composite primary key (web_site_id, path_alias, from_date) found, that is not supported. The first column is selected.
    path_alias = models.CharField(max_length=255)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    alias_to = models.CharField(max_length=255, blank=True, null=True)
    content = models.ForeignKey(Content, models.DO_NOTHING, blank=True, null=True)
    map_key = models.CharField(max_length=100, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_site_path_alias'
        unique_together = (('web_site', 'path_alias', 'from_date'),)


class WebSitePublishPoint(models.Model):
    content = models.OneToOneField(Content, models.DO_NOTHING, primary_key=True)
    template_title = models.CharField(max_length=255, blank=True, null=True)
    style_sheet_file = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    medallion_logo = models.CharField(max_length=255, blank=True, null=True)
    line_logo = models.CharField(max_length=255, blank=True, null=True)
    left_bar_id = models.CharField(max_length=20, blank=True, null=True)
    right_bar_id = models.CharField(max_length=20, blank=True, null=True)
    content_dept = models.CharField(max_length=20, blank=True, null=True)
    about_content_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_site_publish_point'


class WebSiteRole(models.Model):
    party = models.OneToOneField(PartyRole, models.DO_NOTHING, primary_key=True)  # The composite primary key (party_id, role_type_id, web_site_id, from_date) found, that is not supported. The first column is selected.
    role_type_id = models.CharField(max_length=20)
    web_site = models.ForeignKey(WebSite, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_site_role'
        unique_together = (('party', 'role_type_id', 'web_site', 'from_date'),)


class WebUserPreference(models.Model):
    user_login = models.OneToOneField(UserLogin, models.DO_NOTHING, primary_key=True)  # The composite primary key (user_login_id, party_id, visit_id, web_preference_type_id) found, that is not supported. The first column is selected.
    party = models.ForeignKey(Party, models.DO_NOTHING)
    visit_id = models.CharField(max_length=20)
    web_preference_type = models.ForeignKey(WebPreferenceType, models.DO_NOTHING)
    web_preference_value = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_user_preference'
        unique_together = (('user_login', 'party', 'visit_id', 'web_preference_type'),)


class WorkEffort(models.Model):
    work_effort_id = models.CharField(primary_key=True, max_length=20)
    work_effort_type = models.ForeignKey('WorkEffortType', models.DO_NOTHING, blank=True, null=True)
    current_status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    last_status_update = models.DateTimeField(blank=True, null=True)
    work_effort_purpose_type = models.ForeignKey('WorkEffortPurposeType', models.DO_NOTHING, blank=True, null=True)
    work_effort_parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    scope_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    priority = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    percent_complete = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    work_effort_name = models.CharField(max_length=100, blank=True, null=True)
    show_as_enum_id = models.CharField(max_length=20, blank=True, null=True)
    send_notification_email = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    location_desc = models.CharField(max_length=255, blank=True, null=True)
    estimated_start_date = models.DateTimeField(blank=True, null=True)
    estimated_completion_date = models.DateTimeField(blank=True, null=True)
    actual_start_date = models.DateTimeField(blank=True, null=True)
    actual_completion_date = models.DateTimeField(blank=True, null=True)
    estimated_milli_seconds = models.FloatField(blank=True, null=True)
    estimated_setup_millis = models.FloatField(blank=True, null=True)
    estimate_calc_method = models.ForeignKey(CustomMethod, models.DO_NOTHING, db_column='estimate_calc_method', blank=True, null=True)
    actual_milli_seconds = models.FloatField(blank=True, null=True)
    actual_setup_millis = models.FloatField(blank=True, null=True)
    total_milli_seconds_allowed = models.FloatField(blank=True, null=True)
    total_money_allowed = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    money_uom = models.ForeignKey(Uom, models.DO_NOTHING, blank=True, null=True)
    special_terms = models.CharField(max_length=255, blank=True, null=True)
    time_transparency = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    universal_id = models.CharField(max_length=60, blank=True, null=True)
    source_reference_id = models.CharField(max_length=60, blank=True, null=True)
    fixed_asset = models.ForeignKey(FixedAsset, models.DO_NOTHING, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    info_url = models.CharField(max_length=255, blank=True, null=True)
    recurrence_info = models.ForeignKey(RecurrenceInfo, models.DO_NOTHING, blank=True, null=True)
    temp_expr = models.ForeignKey(TemporalExpression, models.DO_NOTHING, blank=True, null=True)
    runtime_data = models.ForeignKey(RuntimeData, models.DO_NOTHING, blank=True, null=True)
    note = models.ForeignKey(NoteData, models.DO_NOTHING, blank=True, null=True)
    service_loader_name = models.CharField(max_length=100, blank=True, null=True)
    quantity_to_produce = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_produced = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity_rejected = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_persons = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv2nd_p_p_perc = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserv_nth_p_p_perc = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    accommodation_map = models.ForeignKey(AccommodationMap, models.DO_NOTHING, blank=True, null=True)
    accommodation_spot = models.ForeignKey(AccommodationSpot, models.DO_NOTHING, blank=True, null=True)
    revision_number = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_modified_date = models.DateTimeField(blank=True, null=True)
    last_modified_by_user_login = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort'


class WorkEffortAssignmentRate(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, rate_type_id, party_id, from_date) found, that is not supported. The first column is selected.
    rate_type = models.ForeignKey(RateType, models.DO_NOTHING)
    party = models.ForeignKey(Party, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    rate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_assignment_rate'
        unique_together = (('work_effort', 'rate_type', 'party', 'from_date'),)


class WorkEffortAssoc(models.Model):
    work_effort_id_from = models.OneToOneField(WorkEffort, models.DO_NOTHING, db_column='work_effort_id_from', primary_key=True)  # The composite primary key (work_effort_id_from, work_effort_id_to, work_effort_assoc_type_id, from_date) found, that is not supported. The first column is selected.
    work_effort_id_to = models.ForeignKey(WorkEffort, models.DO_NOTHING, db_column='work_effort_id_to', related_name='workeffortassoc_work_effort_id_to_set')
    work_effort_assoc_type = models.ForeignKey('WorkEffortAssocType', models.DO_NOTHING)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_assoc'
        unique_together = (('work_effort_id_from', 'work_effort_id_to', 'work_effort_assoc_type', 'from_date'),)


class WorkEffortAssocAttribute(models.Model):
    work_effort_id_from = models.OneToOneField(WorkEffortAssoc, models.DO_NOTHING, db_column='work_effort_id_from', primary_key=True)  # The composite primary key (work_effort_id_from, work_effort_id_to, work_effort_assoc_type_id, attr_name) found, that is not supported. The first column is selected.
    work_effort_id_to = models.CharField(max_length=20)
    work_effort_assoc_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField(blank=True, null=True)
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_assoc_attribute'
        unique_together = (('work_effort_id_from', 'work_effort_id_to', 'work_effort_assoc_type_id', 'attr_name'),)


class WorkEffortAssocType(models.Model):
    work_effort_assoc_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_assoc_type'


class WorkEffortAssocTypeAttr(models.Model):
    work_effort_assoc_type = models.OneToOneField(WorkEffortAssocType, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_assoc_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_assoc_type_attr'
        unique_together = (('work_effort_assoc_type', 'attr_name'),)


class WorkEffortAttribute(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    attr_value = models.CharField(max_length=255, blank=True, null=True)
    attr_description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_attribute'
        unique_together = (('work_effort', 'attr_name'),)


class WorkEffortBilling(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, invoice_id, invoice_item_seq_id) found, that is not supported. The first column is selected.
    invoice = models.ForeignKey(InvoiceItem, models.DO_NOTHING)
    invoice_item_seq_id = models.CharField(max_length=20)
    percentage = models.FloatField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_billing'
        unique_together = (('work_effort', 'invoice', 'invoice_item_seq_id'),)


class WorkEffortContactMech(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, contact_mech_id) found, that is not supported. The first column is selected.
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_contact_mech'
        unique_together = (('work_effort', 'contact_mech'),)


class WorkEffortContactMechNew(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, contact_mech_id, from_date) found, that is not supported. The first column is selected.
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_contact_mech_new'
        unique_together = (('work_effort', 'contact_mech', 'from_date'),)


class WorkEffortContent(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, content_id, work_effort_content_type_id, from_date) found, that is not supported. The first column is selected.
    content = models.ForeignKey(Content, models.DO_NOTHING)
    work_effort_content_type = models.ForeignKey('WorkEffortContentType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_content'
        unique_together = (('work_effort', 'content', 'work_effort_content_type', 'from_date'),)


class WorkEffortContentType(models.Model):
    work_effort_content_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_content_type'


class WorkEffortCostCalc(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, cost_component_type_id, from_date) found, that is not supported. The first column is selected.
    cost_component_type = models.ForeignKey(CostComponentType, models.DO_NOTHING)
    cost_component_calc = models.ForeignKey(CostComponentCalc, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_cost_calc'
        unique_together = (('work_effort', 'cost_component_type', 'from_date'),)


class WorkEffortDeliverableProd(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, deliverable_id) found, that is not supported. The first column is selected.
    deliverable = models.ForeignKey(Deliverable, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_deliverable_prod'
        unique_together = (('work_effort', 'deliverable'),)


class WorkEffortEventReminder(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, sequence_id) found, that is not supported. The first column is selected.
    sequence_id = models.CharField(max_length=20)
    contact_mech = models.ForeignKey(ContactMech, models.DO_NOTHING, blank=True, null=True)
    party = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    reminder_date_time = models.DateTimeField(blank=True, null=True)
    repeat_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    repeat_interval = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    current_count = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    reminder_offset = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    locale_id = models.CharField(max_length=20, blank=True, null=True)
    time_zone_id = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_event_reminder'
        unique_together = (('work_effort', 'sequence_id'),)


class WorkEffortFixedAssetAssign(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, fixed_asset_id, from_date) found, that is not supported. The first column is selected.
    fixed_asset = models.ForeignKey(FixedAsset, models.DO_NOTHING)
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    availability_status = models.ForeignKey(StatusItem, models.DO_NOTHING, related_name='workeffortfixedassetassign_availability_status_set', blank=True, null=True)
    allocated_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_fixed_asset_assign'
        unique_together = (('work_effort', 'fixed_asset', 'from_date'),)


class WorkEffortFixedAssetStd(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, fixed_asset_type_id) found, that is not supported. The first column is selected.
    fixed_asset_type = models.ForeignKey(FixedAssetType, models.DO_NOTHING)
    estimated_quantity = models.FloatField(blank=True, null=True)
    estimated_duration = models.FloatField(blank=True, null=True)
    estimated_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_fixed_asset_std'
        unique_together = (('work_effort', 'fixed_asset_type'),)


class WorkEffortGoodStandard(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, product_id, work_effort_good_std_type_id, from_date) found, that is not supported. The first column is selected.
    product = models.ForeignKey(Product, models.DO_NOTHING)
    work_effort_good_std_type = models.ForeignKey('WorkEffortGoodStandardType', models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    estimated_quantity = models.FloatField(blank=True, null=True)
    estimated_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_good_standard'
        unique_together = (('work_effort', 'product', 'work_effort_good_std_type', 'from_date'),)


class WorkEffortGoodStandardType(models.Model):
    work_effort_good_std_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_good_standard_type'


class WorkEffortIcalData(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)
    ical_data = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_ical_data'


class WorkEffortInventoryAssign(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, inventory_item_id) found, that is not supported. The first column is selected.
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING)
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_inventory_assign'
        unique_together = (('work_effort', 'inventory_item'),)


class WorkEffortInventoryProduced(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, inventory_item_id) found, that is not supported. The first column is selected.
    inventory_item = models.ForeignKey(InventoryItem, models.DO_NOTHING)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_inventory_produced'
        unique_together = (('work_effort', 'inventory_item'),)


class WorkEffortKeyword(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, keyword) found, that is not supported. The first column is selected.
    keyword = models.CharField(max_length=60)
    relevancy_weight = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_keyword'
        unique_together = (('work_effort', 'keyword'),)


class WorkEffortNote(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, note_id) found, that is not supported. The first column is selected.
    note = models.ForeignKey(NoteData, models.DO_NOTHING)
    internal_note = models.CharField(max_length=1, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_note'
        unique_together = (('work_effort', 'note'),)


class WorkEffortPartyAssignment(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, party_id, role_type_id, from_date) found, that is not supported. The first column is selected.
    party = models.ForeignKey(PartyRole, models.DO_NOTHING)
    role_type_id = models.CharField(max_length=20)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    assigned_by_user_login = models.ForeignKey(UserLogin, models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    status_date_time = models.DateTimeField(blank=True, null=True)
    expectation_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, blank=True, null=True)
    delegate_reason_enum = models.ForeignKey(Enumeration, models.DO_NOTHING, related_name='workeffortpartyassignment_delegate_reason_enum_set', blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    must_rsvp = models.CharField(max_length=1, blank=True, null=True)
    availability_status = models.ForeignKey(StatusItem, models.DO_NOTHING, related_name='workeffortpartyassignment_availability_status_set', blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_party_assignment'
        unique_together = (('work_effort', 'party', 'role_type_id', 'from_date'),)


class WorkEffortPurposeType(models.Model):
    work_effort_purpose_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_purpose_type'


class WorkEffortReview(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, user_login_id, review_date) found, that is not supported. The first column is selected.
    user_login = models.ForeignKey(UserLogin, models.DO_NOTHING)
    review_date = models.DateTimeField()
    status = models.ForeignKey(StatusItem, models.DO_NOTHING, blank=True, null=True)
    posted_anonymous = models.CharField(max_length=1, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_review'
        unique_together = (('work_effort', 'user_login', 'review_date'),)


class WorkEffortSearchConstraint(models.Model):
    work_effort_search_result = models.OneToOneField('WorkEffortSearchResult', models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_search_result_id, constraint_seq_id) found, that is not supported. The first column is selected.
    constraint_seq_id = models.CharField(max_length=20)
    constraint_name = models.CharField(max_length=255, blank=True, null=True)
    info_string = models.CharField(max_length=255, blank=True, null=True)
    include_sub_work_efforts = models.CharField(max_length=1, blank=True, null=True)
    is_and = models.CharField(max_length=1, blank=True, null=True)
    any_prefix = models.CharField(max_length=1, blank=True, null=True)
    any_suffix = models.CharField(max_length=1, blank=True, null=True)
    remove_stems = models.CharField(max_length=1, blank=True, null=True)
    low_value = models.CharField(max_length=60, blank=True, null=True)
    high_value = models.CharField(max_length=60, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_search_constraint'
        unique_together = (('work_effort_search_result', 'constraint_seq_id'),)


class WorkEffortSearchResult(models.Model):
    work_effort_search_result_id = models.CharField(primary_key=True, max_length=20)
    visit_id = models.CharField(max_length=20, blank=True, null=True)
    order_by_name = models.CharField(max_length=255, blank=True, null=True)
    is_ascending = models.CharField(max_length=1, blank=True, null=True)
    num_results = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    seconds_total = models.FloatField(blank=True, null=True)
    search_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_search_result'


class WorkEffortSkillStandard(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, skill_type_id) found, that is not supported. The first column is selected.
    skill_type = models.ForeignKey(SkillType, models.DO_NOTHING)
    estimated_num_people = models.FloatField(blank=True, null=True)
    estimated_duration = models.FloatField(blank=True, null=True)
    estimated_cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_skill_standard'
        unique_together = (('work_effort', 'skill_type'),)


class WorkEffortStatus(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, status_id, status_datetime) found, that is not supported. The first column is selected.
    status = models.ForeignKey(StatusItem, models.DO_NOTHING)
    status_datetime = models.DateTimeField()
    set_by_user_login = models.ForeignKey(UserLogin, models.DO_NOTHING, db_column='set_by_user_login', blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_status'
        unique_together = (('work_effort', 'status', 'status_datetime'),)


class WorkEffortSurveyAppl(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, survey_id, from_date) found, that is not supported. The first column is selected.
    survey = models.ForeignKey(Survey, models.DO_NOTHING)
    from_date = models.DateTimeField()
    thru_date = models.DateTimeField(blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_survey_appl'
        unique_together = (('work_effort', 'survey', 'from_date'),)


class WorkEffortTransBox(models.Model):
    process_work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (process_work_effort_id, to_activity_id, transition_id) found, that is not supported. The first column is selected.
    to_activity_id = models.CharField(max_length=60)
    transition_id = models.CharField(max_length=60)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_trans_box'
        unique_together = (('process_work_effort', 'to_activity_id', 'transition_id'),)


class WorkEffortType(models.Model):
    work_effort_type_id = models.CharField(primary_key=True, max_length=20)
    parent_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    has_table = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_type'


class WorkEffortTypeAttr(models.Model):
    work_effort_type = models.OneToOneField(WorkEffortType, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_type_id, attr_name) found, that is not supported. The first column is selected.
    attr_name = models.CharField(max_length=60)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_effort_type_attr'
        unique_together = (('work_effort_type', 'attr_name'),)


class WorkOrderItemFulfillment(models.Model):
    work_effort = models.OneToOneField(WorkEffort, models.DO_NOTHING, primary_key=True)  # The composite primary key (work_effort_id, order_id, order_item_seq_id) found, that is not supported. The first column is selected.
    order = models.ForeignKey(OrderItem, models.DO_NOTHING)
    order_item_seq_id = models.CharField(max_length=20)
    ship_group_seq_id = models.CharField(max_length=20, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_order_item_fulfillment'
        unique_together = (('work_effort', 'order', 'order_item_seq_id'),)


class WorkReqFulfType(models.Model):
    work_req_fulf_type_id = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_req_fulf_type'


class WorkRequirementFulfillment(models.Model):
    requirement = models.OneToOneField(Requirement, models.DO_NOTHING, primary_key=True)  # The composite primary key (requirement_id, work_effort_id) found, that is not supported. The first column is selected.
    work_effort = models.ForeignKey(WorkEffort, models.DO_NOTHING)
    work_req_fulf_type = models.ForeignKey(WorkReqFulfType, models.DO_NOTHING, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_requirement_fulfillment'
        unique_together = (('requirement', 'work_effort'),)


class X509IssuerProvision(models.Model):
    cert_provision_id = models.CharField(primary_key=True, max_length=20)
    common_name = models.CharField(max_length=255, blank=True, null=True)
    organizational_unit = models.CharField(max_length=255, blank=True, null=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    city_locality = models.CharField(max_length=255, blank=True, null=True)
    state_province = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'x509_issuer_provision'


class ZipSalesRuleLookup(models.Model):
    state_code = models.CharField(primary_key=True, max_length=60)  # The composite primary key (state_code, city, country, from_date) found, that is not supported. The first column is selected.
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    from_date = models.DateTimeField()
    id_code = models.CharField(max_length=60, blank=True, null=True)
    taxable = models.CharField(max_length=60, blank=True, null=True)
    ship_cond = models.CharField(max_length=255, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_sales_rule_lookup'
        unique_together = (('state_code', 'city', 'country', 'from_date'),)


class ZipSalesTaxLookup(models.Model):
    zip_code = models.CharField(primary_key=True, max_length=60)  # The composite primary key (zip_code, state_code, city, country, from_date) found, that is not supported. The first column is selected.
    state_code = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    from_date = models.DateTimeField()
    country_fips = models.CharField(max_length=60, blank=True, null=True)
    country_default = models.CharField(max_length=1, blank=True, null=True)
    general_default = models.CharField(max_length=1, blank=True, null=True)
    inside_city = models.CharField(max_length=1, blank=True, null=True)
    geo_code = models.CharField(max_length=60, blank=True, null=True)
    state_sales_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    city_sales_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    city_local_sales_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    country_sales_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    country_local_sales_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    combo_sales_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    state_use_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    city_use_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    city_local_use_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    country_use_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    country_local_use_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    combo_use_tax = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    last_updated_stamp = models.DateTimeField(blank=True, null=True)
    last_updated_tx_stamp = models.DateTimeField(blank=True, null=True)
    created_stamp = models.DateTimeField(blank=True, null=True)
    created_tx_stamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_sales_tax_lookup'
        unique_together = (('zip_code', 'state_code', 'city', 'country', 'from_date'),)
