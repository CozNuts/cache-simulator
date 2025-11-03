"""
🎲 Memory Trace Generator - Create Realistic Workloads
📊 Different access patterns = different cache behavior
🎯 Because real programs don't access memory randomly
"""

import random

class TraceGenerator:
    """
    Generate different types of memory access patterns
    See how your cache handles different workloads
    """
    
    def __init__(self, seed=42):
        random.seed(seed)
        self.generated_traces = 0
    
    def sequential(self, start=0, count=1000, step=4):
        """Sequential access - like scanning an array"""
        print(f"📈 Sequential: {count} accesses, step {step}")
        trace = [start + i * step for i in range(count)]
        self.generated_traces += 1
        return trace
    
    def random(self, max_address=10000, count=1000):
        """Random access - the worst case for caches"""
        print(f"🎲 Random: {count} accesses up to {max_address}")
        trace = [random.randint(0, max_address) for _ in range(count)]
        self.generated_traces += 1
        return trace
    
    def looping(self, loop_size=100, loops=10, stride=4):
        """Looping pattern - common in programs"""
        print(f"🔄 Looping: {loops} loops of {loop_size} accesses")
        trace = []
        for loop in range(loops):
            for i in range(loop_size):
                address = (i * stride) % (loop_size * stride)
                trace.append(address)
        self.generated_traces += 1
        return trace
    
    def mixed(self, count=2000):
        """Mixed pattern - more like real programs"""
        print(f"🌈 Mixed: {count} realistic accesses")
        
        # Combine different patterns
        seq = self.sequential(0, count//3, 4)
        rand = [random.randint(0, 5000) for _ in range(count//3)]
        loop = self.looping(50, count//150)
        
        # Shuffle them together
        trace = seq + rand + loop
        random.shuffle(trace)
        
        self.generated_traces += 1
        return trace[:count]
    
    def save_trace(self, filename, addresses):
        """Save trace to file for later use"""
        try:
            with open(filename, 'w') as f:
                for addr in addresses:
                    f.write(f"{addr}\n")
            print(f"💾 Saved: {filename} ({len(addresses)} addresses)")
            return True
        except Exception as e:
            print(f"❌ Save failed: {e}")
            return False
    
    def load_trace(self, filename):
        """Load trace from file"""
        try:
            addresses = []
            with open(filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        addresses.append(int(line))
            print(f"📁 Loaded: {filename} ({len(addresses)} addresses)")
            return addresses
        except FileNotFoundError:
            print(f"❌ File not found: {filename}")
            return []