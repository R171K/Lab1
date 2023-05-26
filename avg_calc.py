{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5a270478",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The average of the numbers is: 15.0\n"
     ]
    }
   ],
   "source": [
    "def calculate_average(numbers):\n",
    "    if len(numbers) == 0:\n",
    "        return 0\n",
    "    else:\n",
    "        total = sum(numbers)\n",
    "        average = total / len(numbers)\n",
    "        return average\n",
    "\n",
    "\n",
    "# Example usage\n",
    "number_list = [5, 10, 15, 20, 25]\n",
    "result = calculate_average(number_list)\n",
    "print(f\"The average of the numbers is: {result}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e14579bd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
