"""
🎮 Cache Simulator - Your Computer Architecture Lab
🚀 Run experiments, see results, actually understand caches!
💡 No more boring textbook explanations
"""

import time
from cache_config import CacheConfig
from cache import Cache
from trace_generator import TraceGenerator
from visualizer import Visualizer

def experiment_basic_functionality():
    """Basic test to understand cache fundamentals"""
    print("=" * 60)
    print("🎓 EXPERIMENT 1: Basic Cache Functionality")
    print("=" * 60)
    
    # Simple configuration for learning
    config = CacheConfig(cache_size_kb=4, block_size_bytes=64, associativity=1)
    cache = Cache(config, policy_name="LRU")
    
    # Simple access pattern to see hits and misses
    addresses = [0, 64, 128, 192, 0, 64, 128, 256]
    
    print("\nRunning basic access pattern...")
    for i, addr in enumerate(addresses):
        result = cache.access(addr)
        print(f"  Access {i}: address {addr:3d} -> {result}")
    
    cache.print_stats()
    return cache

def experiment_policy_comparison():
    """Compare different replacement policies"""
    print("\n" + "=" * 60)
    print("🔬 EXPERIMENT 2: Replacement Policy Comparison")
    print("=" * 60)
    
    generator = TraceGenerator()
    trace = generator.mixed(800)
    
    policies = ["LRU", "FIFO", "RANDOM"]
    results = {}
    
    for policy in policies:
        print(f"\n--- Testing {policy} policy ---")
        config = CacheConfig(cache_size_kb=8, block_size_bytes=64, associativity=4)
        cache = Cache(config, policy_name=policy)
        
        # Run simulation
        start_time = time.time()
        for address in trace:
            cache.access(address)
        end_time = time.time()
        
        stats = cache.get_stats()
        stats['time'] = end_time - start_time
        results[policy] = stats
        
        print(f"  Hit rate: {stats['hit_rate']:.2f}%")
        print(f"  Time: {stats['time']:.3f}s")
    
    return results

def experiment_cache_size_impact():
    """Test how cache size affects performance"""
    print("\n" + "=" * 60)
    print("📈 EXPERIMENT 3: Cache Size Impact")
    print("=" * 60)
    
    generator = TraceGenerator()
    trace = generator.mixed(1000)
    
    sizes = [2, 4, 8, 16, 32]  # KB
    results = {}
    
    for size in sizes:
        print(f"\n--- Testing {size}KB cache ---")
        config = CacheConfig(cache_size_kb=size, block_size_bytes=64, associativity=2)
        cache = Cache(config, policy_name="LRU")
        
        for address in trace:
            cache.access(address)
        
        stats = cache.get_stats()
        results[size] = stats
        print(f"  Hit rate: {stats['hit_rate']:.2f}%")
    
    return results

def experiment_associativity():
    """Test different associativity levels"""
    print("\n" + "=" * 60)
    print("🔄 EXPERIMENT 4: Associativity Impact")
    print("=" * 60)
    
    generator = TraceGenerator()
    trace = generator.looping(loop_size=50, loops=20)
    
    associativities = [1, 2, 4, 8]
    results = {}
    
    for assoc in associativities:
        config_name = "Direct" if assoc == 1 else f"{assoc}-way"
        print(f"\n--- Testing {config_name} ---")
        
        config = CacheConfig(cache_size_kb=8, block_size_bytes=64, associativity=assoc)
        cache = Cache(config, policy_name="LRU")
        
        for address in trace:
            cache.access(address)
        
        stats = cache.get_stats()
        results[config_name] = stats
        print(f"  Hit rate: {stats['hit_rate']:.2f}%")
    
    return results

def experiment_memory_patterns():
    """Test how different memory access patterns affect performance"""
    print("\n" + "=" * 60)
    print("🎭 EXPERIMENT 5: Memory Access Patterns")
    print("=" * 60)
    
    generator = TraceGenerator()
    config = CacheConfig(cache_size_kb=8, block_size_bytes=64, associativity=2)
    results = {}
    
    # Test sequential pattern
    print("\n--- Sequential Pattern ---")
    sequential_trace = generator.sequential(count=1000)
    cache = Cache(config, policy_name="LRU")
    for address in sequential_trace:
        cache.access(address)
    stats = cache.get_stats()
    results["Sequential"] = stats
    print(f"  Hit rate: {stats['hit_rate']:.2f}%")
    
    # Test random pattern
    print("\n--- Random Pattern ---")
    random_trace = generator.random(count=1000)
    cache = Cache(config, policy_name="LRU")
    for address in random_trace:
        cache.access(address)
    stats = cache.get_stats()
    results["Random"] = stats
    print(f"  Hit rate: {stats['hit_rate']:.2f}%")
    
    # Test looping pattern
    print("\n--- Looping Pattern ---")
    looping_trace = generator.looping(loop_size=100, loops=10)
    cache = Cache(config, policy_name="LRU")
    for address in looping_trace:
        cache.access(address)
    stats = cache.get_stats()
    results["Looping"] = stats
    print(f"  Hit rate: {stats['hit_rate']:.2f}%")
    
    # Test mixed pattern
    print("\n--- Mixed Pattern ---")
    mixed_trace = generator.mixed(count=1000)
    cache = Cache(config, policy_name="LRU")
    for address in mixed_trace:
        cache.access(address)
    stats = cache.get_stats()
    results["Mixed"] = stats
    print(f"  Hit rate: {stats['hit_rate']:.2f}%")
    
    return results

def debug_small_example():
    """Small example to understand cache behavior"""
    print("\n" + "=" * 60)
    print("🐛 DEBUG: Understanding Cache Sets")
    print("=" * 60)
    
    config = CacheConfig(cache_size_kb=1, block_size_bytes=16, associativity=2)
    cache = Cache(config, policy_name="LRU")
    
    # Enable debug to see what's happening
    cache.debug_on()
    
    # Small trace that shows set behavior
    test_addresses = [0, 16, 32, 48, 0, 16, 64, 80]
    
    print("Address breakdown:")
    for addr in test_addresses:
        set_idx = cache._get_set_index(addr)
        tag = cache._get_tag(addr)
        print(f"  Address {addr:3d} -> set {set_idx}, tag {tag}")
    
    print("\nRunning simulation...")
    for addr in test_addresses:
        result = cache.access(addr)
        print(f"  Address {addr} -> {result}")
    
    cache.debug_off()
    cache.print_stats()
    return cache

def run_quick_demo():
    """Quick demo for first-time users"""
    print("\n" + "=" * 60)
    print("🚀 QUICK DEMO: Cache Simulator in Action")
    print("=" * 60)
    
    print("\n📖 What we're about to see:")
    print("  • How cache hits and misses work")
    print("  • Different replacement policies in action")
    print("  • How cache size affects performance")
    print("  • The impact of memory access patterns")
    print("  • Professional visualizations of results")
    
    # Quick cache demo
    print("\n🎯 Quick Cache Demo:")
    config = CacheConfig(cache_size_kb=2, block_size_bytes=32, associativity=1)
    cache = Cache(config, policy_name="LRU")
    
    demo_addresses = [0, 32, 64, 0, 32, 96, 128, 0]
    print("  Addresses: [0, 32, 64, 0, 32, 96, 128, 0]")
    
    for i, addr in enumerate(demo_addresses):
        result = cache.access(addr)
        print(f"  Access {i}: 0x{addr:08X} -> {result}")
    
    cache.print_stats()

def main():
    """Main function - run all learning experiments"""
    print("🚀 Starting Cache Simulator Learning Project")
    print("Project started: December 2024")
    print("Current date: [Current Month] 2025")
    print("This project helped me understand computer architecture concepts")
    print()
    
    try:
        # Initialize visualizer
        viz = Visualizer()
        
        # Quick demo first
        run_quick_demo()
        
        # Run experiments
        print("\n" + "=" * 60)
        print("🏃 RUNNING FULL EXPERIMENTS")
        print("=" * 60)
        
        # Experiment 1: Basic functionality
        cache1 = experiment_basic_functionality()
        
        # Experiment 2: Policy comparison
        policy_results = experiment_policy_comparison()
        
        # Experiment 3: Cache size impact
        size_results = experiment_cache_size_impact()
        
        # Experiment 4: Associativity
        assoc_results = experiment_associativity()
        
        # Experiment 5: Memory patterns
        pattern_results = experiment_memory_patterns()
        
        # Debug example
        debug_cache = debug_small_example()
        
        # Create visualizations
        print("\n" + "=" * 60)
        print("📊 GENERATING VISUALIZATIONS")
        print("=" * 60)
        
        # Basic comparisons
        viz.plot_policy_comparison(policy_results)
        viz.plot_size_sensitivity(size_results)
        viz.plot_associativity_impact(assoc_results)
        viz.compare_multiple_configs(pattern_results, "Memory Access Pattern Comparison")
        
        # Comprehensive dashboard
        all_results = {}
        all_results.update({f"Policy_{k}": v for k, v in policy_results.items()})
        all_results.update({f"Size_{k}KB": v for k, v in size_results.items()})
        all_results.update({f"Assoc_{k}": v for k, v in assoc_results.items()})
        all_results.update({f"Pattern_{k}": v for k, v in pattern_results.items()})
        
        viz.create_comprehensive_dashboard(all_results, "Complete Cache Simulation Summary")
        
        # Access pattern visualization
        if hasattr(cache1, 'access_log') and cache1.access_log:
            viz.plot_access_pattern(cache1.access_log)
        
        # Performance trend across all experiments
        viz.plot_performance_trend(all_results)
        
        print("\n🎉 ALL EXPERIMENTS COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("📚 WHAT YOU LEARNED FROM THIS PROJECT:")
        print("  ✅ How CPU caches actually work in real processors")
        print("  ✅ Why replacement policies matter (LRU vs FIFO vs Random)")
        print("  ✅ How cache size directly affects program performance")
        print("  ✅ What associativity means and why it's important")
        print("  ✅ How different memory access patterns impact caching")
        print("  ✅ How to analyze and visualize computer architecture concepts")
        print("  ✅ Practical Python programming for systems simulation")
        print()
        print("💡 YOU NOW UNDERSTAND WHAT YOUR PROFESSOR WAS TALKING ABOUT!")
        print("🎓 Ready to ace your computer architecture exams! 💪")
        
        # Final summary
        print("\n" + "=" * 60)
        print("📈 PROJECT SUMMARY")
        print("=" * 60)
        print(f"• Experiments run: 5")
        print(f"• Cache configurations tested: {len(all_results)}")
        print(f"• Replacement policies compared: 3")
        print(f"• Memory patterns analyzed: 4")
        print(f"• Visualizations created: 6+")
        print("• Knowledge gained: Priceless 💎")
        
    except Exception as e:
        print(f"\n❌ Error during simulation: {e}")
        print("This is part of the learning process!")
        print("Common issues to check:")
        print("  • Make sure all files are in the correct location")
        print("  • Check that all dependencies are installed")
        print("  • Verify Python version (3.6+ required)")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()