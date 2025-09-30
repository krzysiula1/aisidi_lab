#include <iostream>
#include <vector>
#include <string>
#include "monitor.h"

int const threadsCounts = 4; // liczba w�tk�w

int const bufferSize = 9;

class Buffer
{
private:
    Semaphore mutex;
    Semaphore empty;
    Semaphore full;
    Semaphore semA;
    Semaphore semB;



    std::vector<char> values;

    void print(std::string name)
    {
        std::cout << "\n ###" << name << " " << values.size() << "[";
        for (auto v : values)
            std::cout << v << ",";
        std::cout << "] ###\n";
    }

public:
    Buffer() : mutex(1), empty(0), full(bufferSize), semA(0), semB(0)
    {
    }

    void put(char value)
    {
        full.p();
        mutex.p();
        values.push_back(value);
        print("P");
        if (values.size() == 1)
        {
            if (value == 'A')
            {
                semA.v();
            }
            else
            {
                semB.v();
            }
        }
        if (values.size() > 3)
        {
            empty.v();
        }
        mutex.v();
    }

    void getA()
    {
        semA.p();
        empty.p();
        mutex.p();
        values.erase(values.begin());
        print("A removed");
        full.v();
        if (values.front() == 'A'){
            semA.v();
        }
        else{
            semB.v();
        }
        mutex.v();
    }

    void getB()
    {
        semB.p();
        empty.p();
        mutex.p();
        values.erase(values.begin());
        print("B removed");
        full.v();
        if (values.front() == 'A')
        {
            semA.v();
        }
        else
        {
            semB.v();
        }
        mutex.v();
    }
};

Buffer buffer;

void *threadProdA(void *arg)
{
    for (int i = 0; i < 20; ++i)
    {
        buffer.put('A');
    }
    return NULL;
}

void *threadProdB(void *arg)
{
    for (int i = 0; i < 20; ++i)
    {
        buffer.put('B');
    }
    return NULL;
}

void *threadConsA(void *arg)
{
    for (int i = 0; i < 30; ++i)
    {
        buffer.getA();
    }
    return NULL;
}

void *threadConsB(void *arg)
{
    for (int i = 0; i < 30; ++i)
    {
        buffer.getB();
    }
    return NULL;
}

int main()
{
#ifdef _WIN32
    HANDLE tid[threadsCounts];
    DWORD id;

    // utworzenie w�tk�w
    tid[0] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadProdA, 0, 0, &id);
    tid[1] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadProdB, 0, 0, &id);
    tid[2] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadConsA, 0, 0, &id);
    tid[3] = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)threadConsB, 0, 0, &id);

    // czekaj na zako�czenie w�tk�w
    for (int i = 0; i <= threadsCounts; i++)
        WaitForSingleObject(tid[i], INFINITE);
#else
    pthread_t tid[threadsCounts];

    // utworzenie w�tk�w
    pthread_create(&(tid[0]), NULL, threadProd, NULL);
    pthread_create(&(tid[1]), NULL, threadProd, NULL);
    pthread_create(&(tid[2]), NULL, threadConsA, NULL);
    pthread_create(&(tid[3]), NULL, threadConsB, NULL);

    // czekaj na zako�czenie w�tk�w
    for (int i = 0; i < threadsCounts; i++)
        pthread_join(tid[i], (void **)NULL);
#endif
    return 0;
}
