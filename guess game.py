{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOvZYLGexs2wZqCZrVVB1LJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/anam0001/Anam-Mid-BQ-2.0-CIT-python/blob/main/guess%20game.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KCBHkRj0A6VP",
        "outputId": "ed943b12-9bfd-4d4e-e55c-bbd1b92f918a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a name to guess: Saba\n",
            "Wrong answer!!! Try again\n",
            "You only have 4 turns.\n",
            "\n",
            "\n",
            "Enter a name to guess: Laiba\n",
            "Wrong answer!!! Try again\n",
            "You only have 3 turns.\n",
            "\n",
            "\n",
            "Enter a name to guess: Ali\n",
            "Wrong answer!!! Try again\n",
            "You only have 2 turns.\n",
            "\n",
            "\n",
            "Enter a name to guess: Umar\n",
            "Wrong answer!!! Try again\n",
            "You only have 1 turns.\n",
            "\n",
            "\n",
            "Enter a name to guess: Hafsa\n",
            "Wrong answer!!! Try again\n",
            "You only have 0 turns.\n",
            "\n",
            "\n"
          ]
        }
      ],
      "source": [
        "\n",
        "word=\"Anam\"\n",
        "i=1\n",
        "while i<=5:\n",
        "  guess=input(\"Enter a name to guess: \")\n",
        "  if word==guess:\n",
        "    print(\"Congratulations 🎉🎉🎉\")\n",
        "    print(\"You guess the right name :) \")\n",
        "    break\n",
        "\n",
        "  else:\n",
        "    remain=5-i\n",
        "    print(\"Wrong answer!!! Try again\")\n",
        "    print(f\"You only have {remain} turns.\\n\\n\")\n",
        "\n",
        "    i+=1"
      ]
    }
  ]
}