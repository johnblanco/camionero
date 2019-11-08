from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, RadioField, SelectField


class CalculateCostForm(Form):
    km = IntegerField('Recorrido del viaje en Km (ida)', [validators.required(message='Requerido'),
                                                          validators.NumberRange(min=0,
                                                                                 message='Debe ser mayor que 0')])
    peajes = IntegerField('Cantidad de peajes (ida)', [validators.required(message='Requerido'),
                                                       validators.NumberRange(min=0, message='Debe ser mayor que 0')])

    frontera = BooleanField('¿Hay cruce de frontera?')

    toneladas = IntegerField('Toneladas transportadas (ida)', [validators.required(message='Requerido'),
                                                               validators.NumberRange(min=0,
                                                                                      message='Debe ser mayor que 0')])

    tiempo_total = IntegerField('Tiempo total de traslado en el viaje (ida) [horas]',
                                [validators.required(message='Requerido'),
                                 validators.NumberRange(min=0,
                                                        message='Debe ser mayor que 0')])

    tiempo_descarga = IntegerField('Tiempo total de carga en origen + descarga en destino [Horas]',
                                   [validators.required(message='Requerido'),
                                    validators.NumberRange(min=0,
                                                           message='Debe ser mayor que 0')])

    otros_tiempos = IntegerField('Otros tiempos (Esperas, colas, lavados, etc.) [Horas]',
                                 [validators.required(message='Requerido'),
                                  validators.NumberRange(min=0,
                                                         message='Debe ser mayor que 0')])

    retorno_con_carga = RadioField('¿El viaje de retorno es con carga?', choices=[('y', 'Si'), ('n', 'No')],
                                   validators=[validators.required(message='Requerido')])

    ayudantes = IntegerField('Cantidad ayudantes en el viaje',
                             [validators.required(message='Requerido'),
                              validators.NumberRange(min=0,
                                                     message='Debe ser mayor que 0')])

# ¿Número de ayudantes en el viaje?
