# appointment_webpage/controllers/main.py
from odoo import http
from odoo.http import request
from datetime import datetime

class AppointmentWebpage(http.Controller):

    @http.route('/appointment', type='http', auth="public", website=True)
    def appointment_form(self, **kw):
        doctors = request.env['om_hospital.doctor'].search([])
        patients = request.env['om_hospital.pateint'].search([])
        return request.render('appointment_webpage.appointment_form', {
            'doctors': doctors,
            'patients': patients,
        })

    @http.route('/create/appointment', type='http', auth="public", methods=['POST'], website=True)
    def create_appointment(self, **post):
        # Convert the appointment_time from form to Odoo's expected format
        appointment_time_str = post.get('appointment_time')
        if appointment_time_str:
            appointment_time = datetime.strptime(appointment_time_str, '%Y-%m-%dT%H:%M')
            appointment_time = appointment_time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            appointment_time = None
        
        # Create the appointment record
        request.env['om_hospital.appointment'].sudo().create({
            'ref': post.get('ref'),
            'note': post.get('note'),
            'priority': post.get('priority'),
            'doctor_id': int(post.get('doctor_id')),
            'pateint_id': int(post.get('pateint_id')),
            'appointment_time': appointment_time,
            'booking_Date': post.get('booking_Date'),
            'state': 'draft'
        })
        return request.redirect('/appointment')
