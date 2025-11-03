"""
🎨 ULTIMATE VISUALIZER - Cache Performance in Style!
🌟 Professional, engaging, and Instagram-worthy graphs
📈 Because boring data doesn't help anyone learn
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib.colors as mcolors

class Visualizer:
    """
    Creates stunning, professional visualizations that make cache concepts click!
    Perfect for presentations, reports, and showing off your skills
    """
    
    def __init__(self):
        # Modern, vibrant color palette
        self.colors = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
            '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9'
        ]
        
        # Set modern style
        plt.style.use('default')
        plt.rcParams['font.family'] = 'DejaVu Sans'
        plt.rcParams['font.size'] = 11
        plt.rcParams['axes.titleweight'] = 'bold'
        plt.rcParams['axes.labelweight'] = 'bold'
        
        print("🎨 Ultimate Visualizer activated! Get ready for stunning graphs! 🌟")
    
    def _create_modern_axis(self, ax, title):
        """Helper to create modern, clean axes"""
        ax.set_facecolor('#f8f9fa')
        ax.grid(True, alpha=0.3, color='gray', linestyle='-', linewidth=0.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#cccccc')
        ax.spines['bottom'].set_color('#cccccc')
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20, color='#2c3e50')
        return ax
    
    def plot_policy_comparison(self, policy_results):
        """Compare replacement policies with stunning visuals"""
        print("   🎯 Generating Policy Comparison - Which one wins?")
        
        policies = list(policy_results.keys())
        hit_rates = [policy_results[p]['hit_rate'] for p in policies]
        
        # Create figure with modern styling
        fig, ax = plt.subplots(figsize=(12, 7))
        ax = self._create_modern_axis(ax, '🏆 Replacement Policy Showdown')
        
        # Create gradient bars
        gradient_bars = []
        for i, (policy, rate) in enumerate(zip(policies, hit_rates)):
            color = self.colors[i % len(self.colors)]
            gradient = self._create_gradient(color, 0.7, 1.0)
            
            bar = ax.bar(i, rate, color=gradient, edgecolor=color, linewidth=2, 
                        alpha=0.9, width=0.7)
            gradient_bars.append(bar)
            
            # Add value with emoji indicator
            emoji = "🔥" if rate > 75 else "👍" if rate > 60 else "💤"
            ax.text(i, rate + 1, f'{rate:.1f}% {emoji}', 
                   ha='center', va='bottom', fontweight='bold', fontsize=12,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
        
        ax.set_xticks(range(len(policies)))
        ax.set_xticklabels([f'📊 {p}' for p in policies], fontsize=12)
        ax.set_ylabel('Hit Rate (%)', fontsize=12, fontweight='bold')
        ax.set_ylim(0, max(hit_rates) * 1.15)
        
        # Add performance assessment
        best_policy = policies[np.argmax(hit_rates)]
        best_rate = max(hit_rates)
        ax.text(0.5, 0.95, f'🏅 Winner: {best_policy} ({best_rate:.1f}%)', 
               transform=ax.transAxes, ha='center', fontsize=13, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.5", facecolor='gold', alpha=0.9))
        
        plt.tight_layout()
        plt.show()
    
    def plot_size_sensitivity(self, size_results):
        """Show cache size impact with beautiful line chart"""
        print("   💾 Generating Size Impact - Does bigger mean better?")
        
        sizes = list(size_results.keys())
        hit_rates = [size_results[s]['hit_rate'] for s in sizes]
        
        fig, ax = plt.subplots(figsize=(12, 7))
        ax = self._create_modern_axis(ax, '📈 Cache Size: Bigger = Better?')
        
        # Create gradient line with markers
        x_pos = np.arange(len(sizes))
        
        # Main line with gradient
        for i in range(len(sizes)-1):
            ax.plot(x_pos[i:i+2], hit_rates[i:i+2], 
                   color=self.colors[1], linewidth=4, alpha=0.8,
                   marker='o', markersize=10, markerfacecolor='white',
                   markeredgecolor=self.colors[1], markeredgewidth=3)
        
        # Annotate each point with insights
        for i, (size, rate) in enumerate(zip(sizes, hit_rates)):
            # Add insight text
            if i > 0:
                improvement = rate - hit_rates[i-1]
                insight = f"+{improvement:.1f}%" if improvement > 0 else f"{improvement:.1f}%"
                color = "green" if improvement > 0 else "red"
                
                ax.annotate(insight, (x_pos[i], rate),
                           xytext=(0, 25), textcoords='offset points',
                           ha='center', fontweight='bold', color=color,
                           bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
            
            # Size label with emoji
            ax.annotate(f'{size}KB', (x_pos[i], rate),
                       xytext=(0, -35), textcoords='offset points',
                       ha='center', fontweight='bold', fontsize=11,
                       bbox=dict(boxstyle="round,pad=0.4", facecolor=self.colors[0], alpha=0.8))
        
        ax.set_xticks(x_pos)
        ax.set_xticklabels([f'💾 {s}KB' for s in sizes])
        ax.set_ylabel('Hit Rate (%)', fontsize=12, fontweight='bold')
        ax.set_ylim(min(hit_rates) * 0.9, max(hit_rates) * 1.1)
        
        # Add overall trend insight
        trend = "📈 Positive" if hit_rates[-1] > hit_rates[0] else "📉 Negative"
        ax.text(0.02, 0.98, f'Overall Trend: {trend}', 
               transform=ax.transAxes, fontsize=12, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.5", facecolor='lightblue', alpha=0.9))
        
        plt.tight_layout()
        plt.show()
    
    def plot_associativity_impact(self, assoc_results):
        """Show associativity impact with engaging visualization"""
        print("   🔄 Generating Associativity Impact - More ways, more better?")
        
        configs = list(assoc_results.keys())
        hit_rates = [assoc_results[c]['hit_rate'] for c in configs]
        
        fig, ax = plt.subplots(figsize=(12, 7))
        ax = self._create_modern_axis(ax, '🔄 Associativity: Finding the Sweet Spot')
        
        # Create bars with different styles based on associativity
        for i, (config, rate) in enumerate(zip(configs, hit_rates)):
            if "Direct" in config:
                # Direct mapped - simple bar
                bar = ax.bar(i, rate, color=self.colors[0], alpha=0.8, width=0.6)
            else:
                # Associative - fancy gradient bar
                ways = int(config.split('-')[0])
                gradient = self._create_gradient(self.colors[min(ways, 5)], 0.6, 0.9)
                bar = ax.bar(i, rate, color=gradient, alpha=0.9, width=0.6,
                           edgecolor=self.colors[min(ways, 5)], linewidth=2)
            
            # Add configuration label and value
            label = "🎯 Direct" if "Direct" in config else f"🔄 {config}"
            ax.text(i, rate + 1, f'{rate:.1f}%', 
                   ha='center', va='bottom', fontweight='bold', fontsize=11,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
            
            ax.text(i, -max(hit_rates)*0.08, label, 
                   ha='center', va='top', fontweight='bold', fontsize=10,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.7))
        
        ax.set_xticks([])  # Remove x-ticks since we have custom labels
        ax.set_ylabel('Hit Rate (%)', fontsize=12, fontweight='bold')
        ax.set_ylim(0, max(hit_rates) * 1.15)
        
        # Add performance insight
        best_config = configs[np.argmax(hit_rates)]
        ax.text(0.5, 0.92, f'💡 Best: {best_config}', 
               transform=ax.transAxes, ha='center', fontsize=12, fontweight='bold',
               bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgreen', alpha=0.9))
        
        plt.tight_layout()
        plt.show()
    
    def plot_access_pattern(self, access_log, max_points=200):
        """Visualize memory access patterns in a stunning way"""
        print("   🎭 Generating Access Pattern - Watch the cache dance!")
        
        if len(access_log) > max_points:
            step = len(access_log) // max_points
            sampled_log = access_log[::step]
        else:
            sampled_log = access_log
        
        addresses = [entry['address'] for entry in sampled_log]
        results = [entry['result'] for entry in sampled_log]
        sets = [entry.get('set', 0) for entry in sampled_log]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Plot 1: Access pattern over time
        ax1 = self._create_modern_axis(ax1, '🕒 Memory Access Timeline')
        
        colors = ['#4ECDC4' if result == 'HIT' else '#FF6B6B' for result in results]
        sizes = [30 if result == 'HIT' else 50 for result in results]  # Misses are bigger
        
        scatter = ax1.scatter(range(len(addresses)), addresses, c=colors, s=sizes, 
                            alpha=0.7, edgecolors='white', linewidth=0.5)
        
        ax1.set_xlabel('Access Sequence', fontsize=11, fontweight='bold')
        ax1.set_ylabel('Memory Address', fontsize=11, fontweight='bold')
        
        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#4ECDC4', label='🎯 Cache Hit'),
            Patch(facecolor='#FF6B6B', label='💥 Cache Miss')
        ]
        ax1.legend(handles=legend_elements, loc='upper right', fontsize=10)
        
        # Plot 2: Hit/Miss distribution
        ax2 = self._create_modern_axis(ax2, '📊 Hit/Miss Distribution')
        
        hit_count = results.count('HIT')
        miss_count = results.count('MISS')
        total = len(results)
        
        hit_percent = (hit_count / total) * 100
        miss_percent = (miss_count / total) * 100
        
        wedges, texts, autotexts = ax2.pie([hit_count, miss_count], 
                                          labels=[f'Hits: {hit_percent:.1f}%', 
                                                 f'Misses: {miss_percent:.1f}%'],
                                          colors=['#4ECDC4', '#FF6B6B'],
                                          autopct='%1.1f%%', startangle=90,
                                          explode=(0.05, 0))
        
        # Style the text
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(11)
        
        # Add overall performance indicator
        performance = "🔥 EXCELLENT" if hit_percent > 80 else "👍 GOOD" if hit_percent > 60 else "💤 NEEDS WORK"
        ax2.text(0, 0, f'{performance}\n{hit_percent:.1f}%', 
                ha='center', va='center', fontweight='bold', fontsize=12,
                bbox=dict(boxstyle="round,pad=0.8", facecolor='gold', alpha=0.8))
        
        plt.tight_layout()
        plt.show()
    
    def create_comprehensive_dashboard(self, all_results, title="🎯 Cache Performance Master Dashboard"):
        """Create an ultimate dashboard that tells the complete story"""
        print("   🚀 Generating Master Dashboard - The Big Picture!")
        
        fig = plt.figure(figsize=(16, 12))
        fig.suptitle(title, fontsize=18, fontweight='bold', color='#2c3e50', y=0.95)
        
        # Create a 2x2 grid with some spanning
        gs = fig.add_gridspec(3, 3)
        
        # Extract different types of results
        policy_results = {k: v for k, v in all_results.items() if k.startswith('Policy_')}
        size_results = {k: v for k, v in all_results.items() if k.startswith('Size_')}
        assoc_results = {k: v for k, v in all_results.items() if k.startswith('Assoc_')}
        pattern_results = {k: v for k, v in all_results.items() if k.startswith('Pattern_')}
        
        # Plot 1: Policy Comparison (top left)
        ax1 = fig.add_subplot(gs[0, 0])
        if policy_results:
            policies = [k.replace('Policy_', '') for k in policy_results.keys()]
            hit_rates = [policy_results[p]['hit_rate'] for p in policy_results.keys()]
            
            bars = ax1.bar(range(len(policies)), hit_rates, 
                          color=self.colors[:len(policies)], alpha=0.8)
            ax1.set_title('🏆 Policy Showdown', fontweight='bold', fontsize=12)
            ax1.set_ylabel('Hit Rate (%)')
            ax1.set_xticks(range(len(policies)))
            ax1.set_xticklabels(policies, rotation=45)
            
            for bar, rate in zip(bars, hit_rates):
                ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                        f'{rate:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # Plot 2: Size Impact (top middle)
        ax2 = fig.add_subplot(gs[0, 1])
        if size_results:
            sizes = [int(k.replace('Size_', '').replace('KB', '')) for k in size_results.keys()]
            hit_rates = [size_results[s]['hit_rate'] for s in size_results.keys()]
            
            ax2.plot(sizes, hit_rates, 'o-', linewidth=3, markersize=8, 
                    color=self.colors[1], markerfacecolor='white')
            ax2.set_title('💾 Size Matters', fontweight='bold', fontsize=12)
            ax2.set_xlabel('Cache Size (KB)')
            ax2.set_ylabel('Hit Rate (%)')
        
        # Plot 3: Associativity (top right)
        ax3 = fig.add_subplot(gs[0, 2])
        if assoc_results:
            configs = [k.replace('Assoc_', '') for k in assoc_results.keys()]
            hit_rates = [assoc_results[c]['hit_rate'] for c in assoc_results.keys()]
            
            bars = ax3.bar(range(len(configs)), hit_rates, color=self.colors[2], alpha=0.8)
            ax3.set_title('🔄 Associativity Impact', fontweight='bold', fontsize=12)
            ax3.set_ylabel('Hit Rate (%)')
            ax3.set_xticks(range(len(configs)))
            ax3.set_xticklabels(configs)
            
            for bar, rate in zip(bars, hit_rates):
                ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                        f'{rate:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # Plot 4: Pattern Comparison (bottom left - spans 2 columns)
        ax4 = fig.add_subplot(gs[1, :])
        if pattern_results:
            patterns = [k.replace('Pattern_', '') for k in pattern_results.keys()]
            hit_rates = [pattern_results[p]['hit_rate'] for p in pattern_results.keys()]
            
            bars = ax4.bar(range(len(patterns)), hit_rates, 
                          color=self.colors[3:3+len(patterns)], alpha=0.8)
            ax4.set_title('🎭 Memory Access Patterns', fontweight='bold', fontsize=12)
            ax4.set_ylabel('Hit Rate (%)')
            ax4.set_xticks(range(len(patterns)))
            ax4.set_xticklabels(patterns)
            
            for bar, rate in zip(bars, hit_rates):
                ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                        f'{rate:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # Plot 5: Overall Ranking (bottom right)
        ax5 = fig.add_subplot(gs[2, :])
        if all_results:
            # Get top 8 performers
            sorted_results = sorted(all_results.items(), key=lambda x: x[1]['hit_rate'], reverse=True)[:8]
            config_names = [k for k, v in sorted_results]
            hit_rates = [v['hit_rate'] for k, v in sorted_results]
            
            y_pos = np.arange(len(config_names))
            bars = ax5.barh(y_pos, hit_rates, color=self.colors[5], alpha=0.8)
            ax5.set_title('🏅 Top Performers Ranking', fontweight='bold', fontsize=12)
            ax5.set_xlabel('Hit Rate (%)')
            ax5.set_yticks(y_pos)
            ax5.set_yticklabels(config_names)
            
            for bar, rate in zip(bars, hit_rates):
                ax5.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                        f'{rate:.1f}%', va='center', fontweight='bold')
        
        # Style all axes
        for ax in [ax1, ax2, ax3, ax4, ax5]:
            self._create_modern_axis(ax, ax.get_title())
            ax.set_title(ax.get_title(), fontsize=11)  # Reduce title size for subplots
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.90)
        plt.show()
    
    def plot_performance_trend(self, experiment_results):
        """Show performance trends across experiments"""
        print("   📊 Generating Performance Trends - Watch the story unfold!")
        
        experiment_names = list(experiment_results.keys())
        hit_rates = [experiment_results[exp]['hit_rate'] for exp in experiment_names]
        
        fig, ax = plt.subplots(figsize=(14, 8))
        ax = self._create_modern_axis(ax, '🚀 Performance Journey Across Experiments')
        
        # Create an engaging line plot
        x_pos = np.arange(len(experiment_names))
        
        # Main line with gradient effect
        line = ax.plot(x_pos, hit_rates, 'o-', linewidth=4, markersize=12,
                      color=self.colors[0], markerfacecolor='white',
                      markeredgewidth=3, markeredgecolor=self.colors[0],
                      alpha=0.8)[0]
        
        # Add gradient fill under the line
        ax.fill_between(x_pos, hit_rates, alpha=0.2, color=self.colors[0])
        
        # Annotate each point with insights
        for i, (name, rate) in enumerate(zip(experiment_names, hit_rates)):
            # Clean up experiment names
            clean_name = name.replace('Policy_', '').replace('Size_', '').replace('KB', 'KB ').replace('Assoc_', '').replace('Pattern_', '')
            
            # Add value with emoji
            emoji = "🔥" if rate > 80 else "👍" if rate > 60 else "📈"
            ax.annotate(f'{rate:.1f}% {emoji}', (i, rate),
                       xytext=(0, 20), textcoords='offset points',
                       ha='center', fontweight='bold', fontsize=10,
                       bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
            
            # Experiment label
            ax.annotate(clean_name, (i, min(hit_rates) * 0.95),
                       xytext=(0, -30), textcoords='offset points',
                       ha='center', fontweight='bold', fontsize=9, rotation=45,
                       bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.7))
        
        ax.set_xticks(x_pos)
        ax.set_xticklabels([f'🎯' for _ in experiment_names])  # Simple markers
        ax.set_ylabel('Hit Rate (%)', fontsize=12, fontweight='bold')
        ax.set_ylim(min(hit_rates) * 0.9, max(hit_rates) * 1.1)
        
        # Add overall insights
        best_exp = experiment_names[np.argmax(hit_rates)]
        best_rate = max(hit_rates)
        worst_exp = experiment_names[np.argmin(hit_rates)]
        worst_rate = min(hit_rates)
        
        insights_text = f"""🏆 Best: {best_exp.replace('_', ' ')} ({best_rate:.1f}%)
📉 Worst: {worst_exp.replace('_', ' ')} ({worst_rate:.1f}%)
📈 Range: {max(hit_rates)-min(hit_rates):.1f}%"""
        
        ax.text(0.02, 0.98, insights_text, transform=ax.transAxes,
               fontsize=11, fontweight='bold', va='top',
               bbox=dict(boxstyle="round,pad=0.8", facecolor='lightblue', alpha=0.9))
        
        plt.tight_layout()
        plt.show()
    
    def compare_multiple_configs(self, config_results, title="🔍 Configuration Face-Off"):
        """Compare multiple configurations in an engaging way"""
        print("   ⚔️  Generating Configuration Face-Off - Let the battle begin!")
        
        config_names = list(config_results.keys())
        hit_rates = [config_results[config]['hit_rate'] for config in config_names]
        
        fig, ax = plt.subplots(figsize=(14, 8))
        ax = self._create_modern_axis(ax, title)
        
        # Create bars with different colors based on performance
        sorted_indices = np.argsort(hit_rates)[::-1]  # Sort descending
        sorted_names = [config_names[i] for i in sorted_indices]
        sorted_rates = [hit_rates[i] for i in sorted_indices]
        
        bars = ax.bar(range(len(sorted_names)), sorted_rates, 
                     color=[self.colors[i % len(self.colors)] for i in range(len(sorted_names))],
                     alpha=0.8, edgecolor='white', linewidth=2)
        
        # Add performance indicators and values
        for i, (bar, rate, name) in enumerate(zip(bars, sorted_rates, sorted_names)):
            # Clean name for display
            clean_name = name.replace('Pattern_', '').replace('_', ' ')
            
            # Performance indicator
            if i == 0:
                indicator = "🥇 GOLD"
                color = 'gold'
            elif i == 1:
                indicator = "🥈 SILVER" 
                color = 'silver'
            elif i == 2:
                indicator = "🥉 BRONZE"
                color = '#cd7f32'
            else:
                indicator = f"#{i+1}"
                color = 'lightgray'
            
            # Value above bar
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                   f'{rate:.1f}%', ha='center', va='bottom', fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
            
            # Configuration name below
            ax.text(bar.get_x() + bar.get_width()/2, -max(hit_rates)*0.05,
                   clean_name, ha='center', va='top', fontweight='bold', fontsize=10,
                   rotation=45,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.7))
            
            # Rank indicator
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 0.5,
                   indicator, ha='center', va='center', fontweight='bold', 
                   fontsize=9, color='white' if i < 3 else 'black')
        
        ax.set_xticks([])
        ax.set_ylabel('Hit Rate (%)', fontsize=12, fontweight='bold')
        ax.set_ylim(0, max(hit_rates) * 1.15)
        
        plt.tight_layout()
        plt.show()
    
    def _create_gradient(self, base_color, start_alpha, end_alpha):
        """Create a gradient effect for bars"""
        return base_color  # Simple implementation - can be enhanced
    
    def create_animated_intro(self):
        """Create a fun animated introduction (conceptual)"""
        print("\n   🎬 Welcome to Cache Simulator Visualizations!")
        print("   ✨ Get ready for:")
        print("     • Professional-grade graphs")
        print("     • Engaging data storytelling") 
        print("     • Instagram-worthy visualizations")
        print("     • Insights that actually make sense")
        print("     • Fun learning experience! 🚀\n")