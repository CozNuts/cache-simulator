"""
🔄 Replacement Policies - The Cache's Decision Maker
🤔 When cache is full, who gets kicked out?
🎯 Different strategies for different situations
"""

class ReplacementPolicy:
    """
    Base class for all replacement policies
    The template for making tough cache decisions
    """
    
    def __init__(self, name):
        self.name = name
        self.stats = {"accesses": 0, "hits": 0}
    
    def access(self, blocks, tag, associativity):
        """Handle a cache access - implement in child classes"""
        self.stats["accesses"] += 1
        pass
    
    def get_hit_rate(self):
        """How good is this policy?"""
        if self.stats["accesses"] == 0:
            return 0.0
        return (self.stats["hits"] / self.stats["accesses"]) * 100
    
    def __str__(self):
        return self.name

class LRUPolicy(ReplacementPolicy):
    """
    Least Recently Used - the popular kid
    Kicks out the block that hasn't been used in ages
    """
    
    def __init__(self):
        super().__init__("LRU")
    
    def access(self, blocks, tag, associativity):
        super().access(blocks, tag, associativity)
        
        # Check if we have this block
        if tag in blocks:
            # Move to most recent position
            blocks.remove(tag)
            blocks.append(tag)
            self.stats["hits"] += 1
            return "HIT", None
        else:
            # Handle miss
            if len(blocks) < associativity:
                blocks.append(tag)
                return "MISS", None
            else:
                # Remove least recently used (oldest)
                replaced = blocks.pop(0)
                blocks.append(tag)
                return "MISS", replaced

class FIFOPolicy(ReplacementPolicy):
    """
    First-In-First-Out - the fair approach
    Kicks out whoever has been there the longest
    """
    
    def __init__(self):
        super().__init__("FIFO")
    
    def access(self, blocks, tag, associativity):
        super().access(blocks, tag, associativity)
        
        # FIFO doesn't reorder on hits
        if tag in blocks:
            self.stats["hits"] += 1
            return "HIT", None
        else:
            if len(blocks) < associativity:
                blocks.append(tag)
                return "MISS", None
            else:
                # Remove first one in
                replaced = blocks.pop(0)
                blocks.append(tag)
                return "MISS", replaced

class RandomPolicy(ReplacementPolicy):
    """
    Random - because sometimes you feel lucky
    Completely random replacement
    """
    
    def __init__(self):
        super().__init__("Random")
        import random
        self.random = random
    
    def access(self, blocks, tag, associativity):
        super().access(blocks, tag, associativity)
        
        if tag in blocks:
            self.stats["hits"] += 1
            return "HIT", None
        else:
            if len(blocks) < associativity:
                blocks.append(tag)
                return "MISS", None
            else:
                # Randomly pick a victim
                index = self.random.randint(0, len(blocks) - 1)
                replaced = blocks[index]
                blocks[index] = tag
                return "MISS", replaced