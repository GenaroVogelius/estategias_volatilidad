


class SpreadVolatilidad():

    def long_stradle(self, first_prima, second_prima, strike, lotes=1, acciones=1):
        maxima_perdida = first_prima + second_prima * lotes * acciones
        break_even_point_inferior = strike - maxima_perdida
        break_even_point_superior = strike + maxima_perdida
        maxima_ganancia = "ilimitada"
        
        return {"maxima_ganancia" : maxima_ganancia, "maxima_perdida": maxima_perdida, "break_even_point_inferior": break_even_point_inferior, "break_even_point_superior": break_even_point_superior}



    def short_stradle(self, first_prima, second_prima, strike, lotes=1, acciones=1):
        maxima_perdida = "ilimitada"
        maxima_ganancia = (first_prima + second_prima) * lotes * acciones
        break_even_point_superior = strike - maxima_ganancia
        break_even_point_inferior = strike + maxima_ganancia

        
        return {"maxima_ganancia" : maxima_ganancia, "maxima_perdida": maxima_perdida, "break_even_point_inferior": break_even_point_inferior, "break_even_point_superior": break_even_point_superior}


        

    def long_strangle(self, call_long, put_long, lotes=1, acciones=1):

        if put_long["strike"] > call_long["strike"]:
            return "El strike del put debe ser menor al strike del call"
        
        maxima_perdida = put_long["prima"] + call_long["prima"] * lotes * acciones
        break_even_point_inferior = put_long["strike"] - maxima_perdida
        break_even_point_superior = call_long["strike"] + maxima_perdida
        maxima_ganancia = "ilimitada"


        print("")
        
        return {"maxima_ganancia" : maxima_ganancia, "maxima_perdida": maxima_perdida, "break_even_point_inferior": break_even_point_inferior, "break_even_point_superior": break_even_point_superior}

    def short_strangle(self, first_prima, second_prima, strike, lotes=1, acciones=1):
        maxima_perdida = "ilimitada"
        maxima_ganancia = first_prima + second_prima * lotes * acciones 
        break_even_point_superior = strike - maxima_ganancia
        break_even_point_inferior = strike + maxima_ganancia
        
        return {"maxima_ganancia" : maxima_ganancia, "maxima_perdida": maxima_perdida, "break_even_point_inferior": break_even_point_inferior, "break_even_point_superior": break_even_point_superior}
        
