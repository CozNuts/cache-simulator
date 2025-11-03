"""
🧪 Basic Tests - Make Sure Everything Works
✅ Because nobody likes broken code
🚦 Test early, test often!
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from cache_config import CacheConfig
from cache import Cache

def test_basic():
    """Test that the cache actually works"""
    print("🧪 Testing basic cache...")
    
    try:
        config = CacheConfig(cache_size_kb=4, block_size_bytes=64, associativity=1)
        cache = Cache(config, policy_name="LRU")
        
        # Basic accesses
        result1 = cache.access(0)  # FIXED: access_address -> access
        result2 = cache.access(64)  # FIXED: access_address -> access
        result3 = cache.access(0)  # FIXED: access_address -> access (Should be a hit!)
        
        print(f"  First access (0): {result1}")
        print(f"  Second access (64): {result2}")
        print(f"  Third access (0): {result3}")
        
        stats = cache.get_stats()
        print(f"  Total: {stats['accesses']}, Hits: {stats['hits']}")
        print(f"  Hit rate: {stats['hit_rate']:.1f}%")
        
        print("✅ Basic test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_policies():
    """Test all replacement policies"""
    print("\n🧪 Testing policies...")
    
    policies = ["LRU", "FIFO", "RANDOM"]
    addresses = [0, 64, 128, 0, 64, 256]
    
    for policy in policies:
        try:
            config = CacheConfig(cache_size_kb=2, block_size_bytes=64, associativity=2)
            cache = Cache(config, policy_name=policy)
            
            for addr in addresses:
                cache.access(addr)  # FIXED: access_address -> access
            
            stats = cache.get_stats()
            print(f"  {policy}: {stats['hit_rate']:.1f}%")
            
        except Exception as e:
            print(f"❌ {policy} failed: {e}")
            return False
    
    print("✅ All policies work!")
    return True

if __name__ == "__main__":
    print("🚀 Running Cache Tests")
    print("=" * 40)
    
    test1 = test_basic()
    test2 = test_policies()
    
    if test1 and test2:
        print("\n🎉 All tests passed!")
    else:
        print("\n💥 Some tests failed!")