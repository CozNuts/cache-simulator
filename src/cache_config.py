"""
Cache Configuration Module
Learning about cache parameters and their relationships
"""

class CacheConfig:
    """
    Configuration class for cache parameters
    Learning how cache size, block size, and associativity interact
    """
    
    def __init__(self, cache_size_kb=8, block_size_bytes=64, associativity=2):
        self.cache_size_kb = cache_size_kb
        self.block_size_bytes = block_size_bytes
        self.associativity = associativity
        
        # Calculate derived parameters
        self.cache_size_bytes = cache_size_kb * 1024
        self.num_blocks = self.cache_size_bytes // block_size_bytes
        
        # Handle different associativity cases
        if associativity == 0:  # Fully associative
            self.num_sets = 1
        else:
            self.num_sets = self.num_blocks // associativity
        
        print(f"🎯 Config: {cache_size_kb}KB, {block_size_bytes}B blocks, {associativity}-way")
        print(f"   -> {self.num_blocks} total blocks, {self.num_sets} sets")
    
    def get_address_breakdown(self, address):
        """
        Helper method to understand address mapping
        Useful for debugging and learning
        """
        block_number = address // self.block_size_bytes
        set_index = block_number % self.num_sets
        tag = block_number // self.num_sets
        
        print(f"🔍 Address {address}: block={block_number}, set={set_index}, tag={tag}")
        return set_index, tag
    
    def __str__(self):
        return f"CacheConfig({self.cache_size_kb}KB, {self.block_size_bytes}B, {self.associativity}-way)"