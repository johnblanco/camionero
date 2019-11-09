from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, RadioField, SelectField


class CalculateCostForm(Form):

    positive_number_msg = 'Debe ser un número positivo'
    required_msg = 'Campo obligatorio, revisar valor'

    km = IntegerField('Recorrido del viaje en Km (ida)', [validators.required(message=required_msg),
                                                          validators.NumberRange(min=0,
                                                                                 message=positive_number_msg)])
    peajes = IntegerField('Cantidad de peajes (ida)', [validators.required(message=required_msg),
                                                       validators.NumberRange(min=0, message=positive_number_msg)])

    frontera = RadioField('¿Hay cruce de frontera?', choices=[('y', 'Si'), ('n', 'No')],
                                   validators=[validators.required(message=required_msg)],default='n')

    toneladas = IntegerField('Toneladas transportadas (ida)', [validators.required(message=required_msg),
                                                               validators.NumberRange(min=0,
                                                                                      message=positive_number_msg)])

    tiempo_total = IntegerField('Tiempo total de traslado en el viaje (ida) [horas]',
                                [validators.required(message=required_msg),
                                 validators.NumberRange(min=0,
                                                        message=positive_number_msg)])

    tiempo_descarga = IntegerField('Tiempo total de carga en origen + descarga en destino [Horas]',
                                   [validators.required(message=required_msg),
                                    validators.NumberRange(min=0,
                                                           message=positive_number_msg)])

    otros_tiempos = IntegerField('Otros tiempos (Esperas, colas, lavados, etc.) [Horas]',
                                 [validators.required(message=required_msg),
                                  validators.NumberRange(min=0,
                                                         message=positive_number_msg)])

    retorno_con_carga = RadioField('¿El viaje de retorno es con carga?', choices=[('y', 'Si'), ('n', 'No')],
                                   validators=[validators.required(message=required_msg)],default='n')

    ayudantes = IntegerField('Cantidad ayudantes en el viaje',
                             [validators.required(message=required_msg),
                              validators.NumberRange(min=0,
                                                     message=positive_number_msg)],default=0)

    viaticos_cortos = IntegerField('Cantidad de viáticos cortos por empleado',
                             [validators.required(message=required_msg),
                              validators.NumberRange(min=0,
                                                     message=positive_number_msg)],default=0)

    viaticos_largos = IntegerField('Cantidad de viáticos largos por empleado',
                                   [validators.required(message=required_msg),
                                    validators.NumberRange(min=0,
                                                           message=positive_number_msg)], default=0)

    pernocte_radio = RadioField('¿El viaje implica pernocte?', choices=[('y', 'Si'), ('n', 'No')],
                                   validators=[validators.required(message=required_msg)], default='n')

    pernocte_camion = RadioField('¿El pernocte se realiza en el camión?', choices=[('y', 'Si'), ('n', 'No')],
                                validators=[validators.required(message=required_msg)], default='y')

    empresa_costos_alojamiento = RadioField('¿La empresa se hace cargo de los costos de alojamiento?', choices=[('y', 'Si'), ('n', 'No')],
                                 validators=[validators.required(message=required_msg)], default='n')

    costo_alojamiento = IntegerField('Costo de alojamiento durante pernocte [$]',
                                   [validators.required(message=required_msg),
                                    validators.NumberRange(min=0,
                                                           message=positive_number_msg)], default=0)

#¿La empresa se hace cargo de los costos de alojamiento?

#Costo de alojamiento durante pernocte [$]
