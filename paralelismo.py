import time
import multiprocessing

# Função que simula um trabalho pesado (como resolver várias equações complexas)
def resolver_equacoes_pesadas(numero):
    resultado = 0
    # Um loop gigante para forçar o processador a trabalhar
    for i in range(2_000_000): 
        resultado += i * numero
    return resultado

if __name__ == "__main__":
    # Criamos 40 "tarefas" pesadas para serem resolvidas
    tarefas = list(range(1, 41)) 
    
    print("--- INICIANDO PROCESSAMENTO SEQUENCIAL (1 Núcleo sozinho) ---")
    inicio_seq = time.time()
    resultados_seq = []
    
    # O processador faz uma tarefa por vez (como 1 pessoa resolvendo tudo)
    for tarefa in tarefas:
        resultados_seq.append(resolver_equacoes_pesadas(tarefa))
        
    fim_seq = time.time()
    tempo_seq = fim_seq - inicio_seq
    print(f"Tempo Sequencial: {tempo_seq:.2f} segundos\n")

    print("--- INICIANDO PROCESSAMENTO PARALELO (Todos os núcleos trabalhando) ---")
    inicio_paralelo = time.time()
    
    # O Pool pega todos os núcleos livres do seu processador e divide as tarefas entre eles
    with multiprocessing.Pool() as pool:
        resultados_paralelo = pool.map(resolver_equacoes_pesadas, tarefas)
        
    fim_paralelo = time.time()
    tempo_paralelo = fim_paralelo - inicio_paralelo
    print(f"Tempo Paralelo: {tempo_paralelo:.2f} segundos\n")

    print("--- RESULTADO FINAL ---")
    ganho = tempo_seq / tempo_paralelo
    print(f"O processamento paralelo foi {ganho:.2f} vezes mais rápido!")