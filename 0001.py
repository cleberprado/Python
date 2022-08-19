{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMndWoI5fHnPCUg3g/h5guM",
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
        "<a href=\"https://colab.research.google.com/github/cleberprado/Python/blob/main/0001.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NMn8m49oXaIp",
        "outputId": "55a39f4e-7c36-47dd-b9d2-84fdade51f7b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "texto = Curso de Engenharia de Software aprendendo Python\n",
            "Tamanho do texto = 49\n",
            "\n",
            "palavras = ['Curso de Engenharia de Software aprendendo Python']\n",
            "tamanho de palavras = 1\n"
          ]
        }
      ],
      "source": [
        "texto = \"Curso de Engenharia de Software aprendendo Python\"\n",
        "print(f\"texto = {texto}\")\n",
        "print(f\"Tamanho do texto = {len(texto)}\\n\")\n",
        "\n",
        "palavras = texto.split(',')\n",
        "print(f\"palavras = {palavras}\")\n",
        "print(f\"tamanho de palavras = {len(palavras)}\")"
      ]
    }
  ]
}