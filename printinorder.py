# LeetCode 1114: Print in Order

import threading
import time
from threading import Lock, Condition, Event, Semaphore

# Approach 1: Using Threading Locks (Most Common)
class Foo:
    def __init__(self):
        self.first_done = Lock()
        self.second_done = Lock()
        
        # Initially acquire both locks so second() and third() will block
        self.first_done.acquire()
        self.second_done.acquire()

    def first(self, printFirst):
        """
        printFirst() outputs "first". Do not change or remove this line.
        """
        printFirst()
        # Release the lock so second() can proceed
        self.first_done.release()

    def second(self, printSecond):
        """
        printSecond() outputs "second". Do not change or remove this line.
        """
        # Wait for first() to complete
        with self.first_done:
            printSecond()
            # Release the lock so third() can proceed
            self.second_done.release()

    def third(self, printThird):
        """
        printThird() outputs "third". Do not change or remove this line.
        """
        # Wait for second() to complete
        with self.second_done:
            printThird()

# Approach 2: Using Threading Events (Cleaner)
class Foo2:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst):
        printFirst()
        self.first_done.set()  # Signal that first is done

    def second(self, printSecond):
        self.first_done.wait()  # Wait for first to complete
        printSecond()
        self.second_done.set()  # Signal that second is done

    def third(self, printThird):
        self.second_done.wait()  # Wait for second to complete
        printThird()

# Approach 3: Using Semaphores
class Foo3:
    def __init__(self):
        # Semaphores with initial count 0 (blocked)
        self.sem_second = Semaphore(0)
        self.sem_third = Semaphore(0)

    def first(self, printFirst):
        printFirst()
        self.sem_second.release()  # Allow second to proceed

    def second(self, printSecond):
        self.sem_second.acquire()  # Wait for first to complete
        printSecond()
        self.sem_third.release()   # Allow third to proceed

    def third(self, printThird):
        self.sem_third.acquire()   # Wait for second to complete
        printThird()

# Approach 4: Using Condition Variables
class Foo4:
    def __init__(self):
        self.condition = Condition()
        self.step = 0

    def first(self, printFirst):
        with self.condition:
            printFirst()
            self.step = 1
            self.condition.notify_all()

    def second(self, printSecond):
        with self.condition:
            while self.step != 1:
                self.condition.wait()
            printSecond()
            self.step = 2
            self.condition.notify_all()

    def third(self, printThird):
        with self.condition:
            while self.step != 2:
                self.condition.wait()
            printThird()

# Approach 5: Using Atomic Counter with Busy Waiting (Not Recommended)
class Foo5:
    def __init__(self):
        self.counter = 0
        self.lock = Lock()

    def first(self, printFirst):
        printFirst()
        with self.lock:
            self.counter = 1

    def second(self, printSecond):
        # Busy wait - not efficient but works
        while True:
            with self.lock:
                if self.counter >= 1:
                    break
            time.sleep(0.001)  # Small sleep to avoid busy spinning
        
        printSecond()
        with self.lock:
            self.counter = 2

    def third(self, printThird):
        # Busy wait - not efficient but works
        while True:
            with self.lock:
                if self.counter >= 2:
                    break
            time.sleep(0.001)  # Small sleep to avoid busy spinning
        
        printThird()

# Testing framework
def test_foo_class(FooClass, test_name):
    print(f"Testing {test_name}:")
    
    test_cases = [
        [1, 2, 3],  # Normal order
        [1, 3, 2],  # Third before second
        [2, 1, 3],  # Second before first
        [2, 3, 1],  # First is last
        [3, 1, 2],  # Complex reordering
        [3, 2, 1]   # Reverse order
    ]
    
    for case in test_cases:
        result = []
        
        def printFirst():
            result.append("first")
        
        def printSecond():
            result.append("second")
        
        def printThird():
            result.append("third")
        
        foo = FooClass()
        threads = []
        
        # Create threads based on the input order
        thread_map = {
            1: lambda: foo.first(printFirst),
            2: lambda: foo.second(printSecond),
            3: lambda: foo.third(printThird)
        }
        
        for num in case:
            thread = threading.Thread(target=thread_map[num])
            threads.append(thread)
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        output = "".join(result)
        expected = "firstsecondthird"
        status = "✓" if output == expected else "✗"
        print(f"  {status} Input {case} → '{output}' (expected: '{expected}')")
    
    print()

if __name__ == "__main__":
    # Test all approaches
    approaches = [
        (Foo, "Threading Locks"),
        (Foo2, "Threading Events"), 
        (Foo3, "Semaphores"),
        (Foo4, "Condition Variables"),
        (Foo5, "Atomic Counter (Busy Wait)")
    ]
    
    for foo_class, name in approaches:
        test_foo_class(foo_class, name)
    
    print("Synchronization Mechanisms Explained:")
    print()
    
    print("1. Threading Locks:")
    print("   - Acquire locks initially to block second() and third()")
    print("   - Release locks in sequence to allow next method")
    print("   - Simple but can be tricky with proper acquire/release")
    print()
    
    print("2. Threading Events:")
    print("   - Use Event objects as signals between threads")
    print("   - wait() blocks until set() is called")
    print("   - Clean and intuitive approach")
    print()
    
    print("3. Semaphores:")
    print("   - Initialize with count 0 to block initially")
    print("   - release() increments count, acquire() decrements")
    print("   - Good for counting resources")
    print()
    
    print("4. Condition Variables:")
    print("   - Use shared state with condition checking")
    print("   - wait() releases lock and blocks until notified")
    print("   - More complex but very powerful")
    print()
    
    print("5. Atomic Counter (Not Recommended):")
    print("   - Uses busy waiting which wastes CPU cycles")
    print("   - Included for educational purposes only")
    print("   - Always prefer blocking synchronization primitives")
    print()
    
    print("Best Practices:")
    print("- Events are usually the cleanest for simple ordering")
    print("- Locks work well but require careful management")
    print("- Avoid busy waiting in production code")
    print("- Consider deadlock potential with multiple locks")
    print("- Test thoroughly with different thread scheduling")