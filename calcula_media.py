'''
## Lista 04 - Exercício 28

Faça um programa para entrar com 5 números e imprimir a média desses números.

O programa deve assumir que a entrada e saída seja exatamente no formato dado nos exemplos a seguir.
**Não adicione outras mensagens ou mude a capitalização das letras pois se fizer isso o teste não passará!**

---

**Exemplo 01:**

Entrada:
```
1 2 3 4 5
```
Saída:
```
3.00
```

---

**Exemplo 02:**

Entrada:
```
-10 -20 -30 -40 -50
```
Saída:
```
-30.00
```

---

**Exemplo 03:**

Entrada:
```
4 4 4 4 4
```
Saída:
```
4.00
```

'''
# Entrada de dados
numeros = list(map(float, input().split()))

# Cálculo da média
media = sum(numeros) / len(numeros)

# Saída formatada
print(f"{media:.2f}")
