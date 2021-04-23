import numpy as np
class linearReg:
    def __init__(self, fit_intercept=True):
        self.fit_intercept = fit_intercept
        self.coefficients = None
        self.fit_intercept = None
    
    def fit(self, X, y):
        # Esta función devuelve el modelo lineal ajustado
        # input : X -variable predictora y "y" variable de respuesta
        # output: coeficientes de regresion.
        xtx = np.dot(X.T, X) ## x-traspose time x
        xtx_inv = np.linalg.inv(xtx) ## inversa de los tiempos de transposición x
        xty = np.dot(X.T, y) ## tiempos de transposición de x y
        coefficients = np.dot(xtx_inv, xty)

        if self.fit_intercept:
            self.intercept = coefficients[0]
            self.coefficients = coefficients[1:]
        else:
            self.intercept = 0
            self.coefficients = coefficients

    def predict(self, X):
        # Esta función devuelve los valores predecidos
        # input: arreglo de variables dependientes
        # output: valores predecidos
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)
            return self.intercept + np.dot(X, self.coef_)
            