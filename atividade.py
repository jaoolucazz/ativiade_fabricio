import numpy as np

class Perceptron:
  def __init__(self):
    self.w1 = np.random.uniform(-1, 1)
    self.w2 = np.random.uniform(-1, 1)
    self.w3 = np.random.uniform(-1, 1)
    self.bias = np.random.uniform(-1, 1)

  def _funcao_degrau(self, soma_ponderada):
    return 1 if soma_ponderada >= 0 else 0

  def treino(self, inputs, outputs, learning_rate=0.1, epochs=100):
    for _ in range(epochs):
      for j in range(len(inputs)):
        soma_ponderada = (self.w1 * inputs[j][0] +
                          self.w2 * inputs[j][1] +
                          self.w3 * inputs[j][2] +
                          self.bias)
        
        previsao = self._funcao_degrau(soma_ponderada)

        erro = outputs[j] - previsao

        self.w1 += learning_rate * erro * inputs[j][0]
        self.w2 += learning_rate * erro * inputs[j][1]
        self.w3 += learning_rate * erro * inputs[j][2] 
        self.bias += learning_rate * erro

    print("Treinamento concluído!")
    print(f"Pesos finais: w1={self.w1:.2f}, w2={self.w2:.2f}, w3={self.w3:.2f}, bias={self.bias:.2f}")

  def predict(self, input_data):
    soma_ponderada = (self.w1 * input_data[0] +
                      self.w2 * input_data[1] +
                      self.w3 * input_data[2] +
                      self.bias)
    return self._funcao_degrau(soma_ponderada)

inputs = np.array([
    [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
    [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]
])

print("--- Iniciando Treinamento para Porta Lógica XOR ---")
outputs_xor = np.array([0, 1, 1, 0, 1, 0, 0, 1])  

p_xor = Perceptron()
print(f"Pesos iniciais (XOR): w1={p_xor.w1:.2f}, w2={p_xor.w2:.2f}, w3={p_xor.w3:.2f}, bias={p_xor.bias:.2f}")

p_xor.treino(inputs, outputs_xor, epochs=100)

print("\n--- Testando o Perceptron XOR ---")
for i in range(len(inputs)):
    print(f"Previsão para {list(inputs[i])}: {p_xor.predict(inputs[i])} (Esperado: {outputs_xor[i]})")

