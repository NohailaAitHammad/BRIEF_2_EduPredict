from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


class IGRClipper(BaseEstimator, TransformerMixin):

      def fit(self, X, y=None):
            #claculer du premier quartier
            self.Q1 = np.percentile(X, 25, axis=0)

            #calcul du troisieme quartie
            self.Q3 = np.percentile(X, 75, axis=0)

            #calcul de l'IQR
            self.IQR = self.Q3 - self.Q1

            #bornes inferieure et superieure
            self.lower_bound_ = self.Q1 - 1.5 * self.IQR
            self.upper_bound_ = self.Q3 + 1.5 * self.IQR

            return self

      def transform(self, X):
            X = np.asarray(X)

            #limiter les valeurs aux bornes IQR
            X_clipped = np.clip(
                  X,
                  self.lower_bound_,
                  self.upper_bound_
            )
            # _ Cette valeur a été apprise pendant fit().
            return X_clipped
