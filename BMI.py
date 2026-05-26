"""Useful for calculating BMIs (Body Mass Indexes) using the Imperial and Metric unit systems.\n
Classes
-------
BodyMassIndex: Is returned by calculation functions and can also be used by itself to represent a Body Mass Index, or BMI.\n
Imperial: Contains the function using the Imperial BMI formula. To calculate the Body Mass Index using the Imperial formula, use the function: 'bmi.'\n
Metric: Contains the function using the Metric BMI formula. To calculate the Body Mass Index using the Metric formula, use the function: 'bmi.'\n

Created by FragNag_Productions
------------------------------
"""
class BodyMassIndex:
    """Defines a body mass index.
    """
    def __init__(self, bmi: float):
        self.bmi = bmi
    def __repr__(self):
        return self.bmi
    def __str__(self):
        return str(self.bmi)
    @property
    def category(self) -> str:
        """Returns the category of the BMI (Body Mass Index) that can be either Underweight, Healthy, Overweight, or Obese.

        Categories
        ----------
        Underweight: Under 18.5.\n
        Healthy: 18.5 to 24.9.\n
        Overweight: 25 to 29.9.\n
        Obese: 30 or over.\n

        Returns:
            str: One of the categories above base on the Body Mass Index.
        """
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Healthy"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
class Imperial:
    @staticmethod
    def bmi(heightIn: float, weightLbs: float) -> BodyMassIndex:
        """Returns the Body Mass Index using the Imperial formula.

        Formula
        -------
        703 * weight (lbs) / height (in)²

        Args:
            heightIn (float): The height in inches.
            weightLbs (float): The weight in pounds.

        Raises:
            ZeroDivisionError: When the height is set to 0.

        Returns:
            BodyMassIndex: The Body Mass Index that was calculated using the formula above.
        """
        if heightIn == 0:
            raise ZeroDivisionError()
        else:
            return BodyMassIndex(bmi=703 * weightLbs / pow(heightIn, 2))
class Metric:
    @staticmethod
    def bmi(heightM: float, weightKg: float) -> BodyMassIndex:
        """Returns the Body Mass Index using the Metric formula.

        Formula
        -------
        weight (kg) / height (m)²

        Args:
            heightM (float): The height in meters.
            weightKg (float): The weight in kilograms.

        Raises:
            ZeroDivisionError: When the height is set to 0.

        Returns:
            BodyMassIndex: The Body Mass Index that was calculated using the formula above.
        """
        if heightM == 0:
            raise ZeroDivisionError()
        else:
            return BodyMassIndex(bmi=weightKg / pow(heightM, 2))