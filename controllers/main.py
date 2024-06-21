# appointment_webpage/controllers/main.py
from odoo import http
from odoo.http import request

class AppointmentWebpage(http.Controller):

    @http.route('/appointment', type='http', auth="public", website=True)
    def appointment_form(self, **kw):
        doctors = request.env['om_hospital.doctor'].search([])
        patients = request.env['om_hospital.pateint'].search([])
        return request.render('appointment_webpage.appointment_form', {
            'doctors': doctors,
            'patients': patients
        })

    @http.route('/create/appointment', type='http', auth="public", methods=['POST'], website=True)
    def create_appointment(self, **post):
        request.env['om_hospital.appointment'].sudo().create({
            'ref': post.get('ref'),
            'prescription': post.get('prescription'),
            'priority': post.get('priority'),
            'doctor_id': int(post.get('doctor_id')),
            'pateint_id': int(post.get('pateint_id')),
            'appointment_time': post.get('appointment_time'),
            'booking_Date': post.get('booking_Date'),
            'note': post.get('note'),
            'state': 'draft'
        })
        return request.redirect('/appointment')
