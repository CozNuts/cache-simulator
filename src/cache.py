"""
🔥 Cache Simulator - Where Theory Meets Reality
🎮 Simulating what actually happens when your code runs
💻 Because cache misses are why your program is slow
"""

from replacement_policies import LRUPolicy, FIFOPolicy, RandomPolicy

class Cache:
    """
    Your personal cache lab - break it, fix it, learn from it!
    """
    
    def __init__(self, config, policy_name="LRU"):
        self.config = config
        self.stats = {
            'accesses': 0,
            'hits': 0,
            'misses': 0,
            'replacements': 0
        }
        
        # Build the actual cache structure
        self.sets = [[] for _ in range(config.num_sets)]
        self._setup_policy(policy_name)
        
        # Debug tools for when you're confused
        self.debug_mode = False
        self.access_log = []
        
        print(f"✅ Cache ready: {policy_name} policy, {config.num_sets} sets")
    
    def _setup_policy(self, policy_name):
        """Choose your cache strategy"""
        policy_name = policy_name.upper()
        
        if policy_name == "LRU":
            self.policy = LRUPolicy()
        elif policy_name == "FIFO":
            self.policy = FIFOPolicy()
        elif policy_name == "RANDOM":
            self.policy = RandomPolicy()
        else:
            print(f"❓ Unknown policy, using LRU")
            self.policy = LRUPolicy()
    
    def access(self, address):
        """
        Process a memory access
        Returns: "HIT" or "MISS"
        """
        self.stats['accesses'] += 1
        
        # Figure out where this address goes
        set_index = self._get_set_index(address)
        tag = self._get_tag(address)
        
        if self.debug_mode:
            print(f"🔍 Access: 0x{address:08X} -> set {set_index}, tag {tag}")
        
        # Let the policy handle the actual work
        result, replaced = self.policy.access(
            self.sets[set_index], 
            tag, 
            self.config.associativity
        )
        
        # Track what happened
        if result == "HIT":
            self.stats['hits'] += 1
        else:
            self.stats['misses'] += 1
            if replaced is not None:
                self.stats['replacements'] += 1
        
        # Keep a log for analysis
        if len(self.access_log) < 1000:
            self.access_log.append({
                'address': address,
                'set': set_index,
                'result': result
            })
        
        return result
    
    def _get_set_index(self, address):
        """Which set does this address belong to?"""
        block_num = address // self.config.block_size_bytes
        return block_num % self.config.num_sets
    
    def _get_tag(self, address):
        """Extract the tag from address"""
        block_num = address // self.config.block_size_bytes
        return block_num // self.config.num_sets
    
    def get_stats(self):
        """Get performance numbers"""
        total = self.stats['accesses']
        hit_rate = (self.stats['hits'] / total * 100) if total > 0 else 0
        
        return {
            'accesses': total,
            'hits': self.stats['hits'],
            'misses': self.stats['misses'],
            'hit_rate': hit_rate,
            'replacements': self.stats['replacements'],
            'policy': str(self.policy)
        }
    
    def print_stats(self):
        """Show me the results!"""
        stats = self.get_stats()
        
        print("\n" + "="*50)
        print("📊 CACHE PERFORMANCE REPORT")
        print("="*50)
        print(f"Config: {self.config}")
        print(f"Policy: {stats['policy']}")
        print("-"*50)
        print(f"Total accesses: {stats['accesses']:,}")
        print(f"Hits: {stats['hits']:,} ({stats['hit_rate']:.1f}%)")
        print(f"Misses: {stats['misses']:,} ({100-stats['hit_rate']:.1f}%)")
        print(f"Replacements: {stats['replacements']:,}")
        
        # Simple grade
        if stats['hit_rate'] > 80:
            grade = "A+ 🎉"
        elif stats['hit_rate'] > 70:
            grade = "B+ 👍"
        elif stats['hit_rate'] > 60:
            grade = "C+ 📈"
        else:
            grade = "Needs work 💪"
        
        print(f"Performance: {grade}")
        print("="*50)
    
    def debug_on(self):
        """Turn on debug mode to see what's happening"""
        self.debug_mode = True
        print("🐛 Debug mode ON")
    
    def debug_off(self):
        """Turn off debug mode"""
        self.debug_mode = False
        print("🐛 Debug mode OFF")