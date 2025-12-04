# -*- coding: utf-8 -*-

from odoo import models, fields, api

# ========== EXTENSION DE RES.PARTNER (pour les entreprises et salariés) ==========
class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    # Champs spécifiques entreprise
    groupe_id = fields.Many2one('entreprise.groupe', string="Groupe d'appartenance",
                                help="Groupe d'entreprises auquel appartient cette entreprise")
    siret = fields.Char(string="SIRET")
    
    # Champ pour lier un salarié à son entreprise
    employer_partner_id = fields.Many2one('res.partner', string="Entreprise employeur",
                                         domain=[('is_company', '=', True)],
                                         help="Entreprise qui emploie ce salarié")
    
    # Relations inverses
    employee_ids = fields.One2many('res.partner', 'employer_partner_id', string="Salariés",
                                   domain=[('is_company', '=', False)])
    salarie_count = fields.Integer(string="Nombre de salariés", compute='_compute_salarie_count', store=True)
    
    # Relations avec le groupe
    entreprise_groupe_ids = fields.One2many('res.partner', 'groupe_id', string="Entreprises du groupe",
                                           domain=[('is_company', '=', True)])

    @api.depends('employee_ids')
    def _compute_salarie_count(self):
        for record in self:
            record.salarie_count = len(record.employee_ids)


# ========== GROUPE D'ENTREPRISES ==========
class EntrepriseGroupe(models.Model):
    _name = 'entreprise.groupe'
    _description = "Groupe d'Entreprises"
    _rec_name = 'nom'

    nom = fields.Char(string="Nom du groupe", required=True)
    siren = fields.Char(string="SIREN")
    siege_social = fields.Char(string="Siège Social")
    
    # Relations inverses
    entreprise_ids = fields.One2many('res.partner', 'groupe_id', string="Entreprises du groupe",
                                    domain=[('is_company', '=', True)])
    entreprise_count = fields.Integer(string="Nombre d'entreprises", compute='_compute_entreprise_count', store=True)

    @api.depends('entreprise_ids')
    def _compute_entreprise_count(self):
        for record in self:
            record.entreprise_count = len(record.entreprise_ids)
