import SwiftUI

struct StatsView: View {
    @EnvironmentObject var matchStore: MatchStore
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 25) {
                    // Title
                    Text("GinRummy Statistics")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.primary)
                        .padding(.top)
                    
                    let stats = matchStore.getStatistics()
                    
                    // Overall Stats
                    VStack(spacing: 20) {
                        Text("Overall Statistics")
                            .font(.title2)
                            .fontWeight(.semibold)
                            .frame(maxWidth: .infinity, alignment: .leading)
                        
                        HStack(spacing: 20) {
                            StatCard(
                                title: "Total Matches",
                                value: "\(stats.totalMatches)",
                                color: .blue
                            )
                            
                            StatCard(
                                title: "Zayaka Wins",
                                value: "\(stats.zayakaWins)",
                                color: .blue
                            )
                            
                            StatCard(
                                title: "Brian Wins",
                                value: "\(stats.brianWins)",
                                color: .green
                            )
                        }
                    }
                    .padding()
                    .background(Color(.systemGray6))
                    .cornerRadius(15)
                    
                    // Win Rates
                    if stats.totalMatches > 0 {
                        VStack(spacing: 20) {
                            Text("Win Rates")
                                .font(.title2)
                                .fontWeight(.semibold)
                                .frame(maxWidth: .infinity, alignment: .leading)
                            
                            HStack(spacing: 20) {
                                WinRateCard(
                                    player: "Zayaka",
                                    wins: stats.zayakaWins,
                                    total: stats.totalMatches,
                                    color: .blue
                                )
                                
                                WinRateCard(
                                    player: "Brian",
                                    wins: stats.brianWins,
                                    total: stats.totalMatches,
                                    color: .green
                                )
                            }
                        }
                        .padding()
                        .background(Color(.systemGray6))
                        .cornerRadius(15)
                    }
                    
                    // Average Scores
                    if stats.totalMatches > 0 {
                        VStack(spacing: 20) {
                            Text("Average Scores")
                                .font(.title2)
                                .fontWeight(.semibold)
                                .frame(maxWidth: .infinity, alignment: .leading)
                            
                            HStack(spacing: 20) {
                                AverageScoreCard(
                                    player: "Zayaka",
                                    average: stats.avgZayaka,
                                    color: .blue
                                )
                                
                                AverageScoreCard(
                                    player: "Brian",
                                    average: stats.avgBrian,
                                    color: .green
                                )
                            }
                        }
                        .padding()
                        .background(Color(.systemGray6))
                        .cornerRadius(15)
                    }
                    
                    // Empty State
                    if stats.totalMatches == 0 {
                        VStack(spacing: 20) {
                            Image(systemName: "chart.bar.xaxis")
                                .font(.system(size: 60))
                                .foregroundColor(.gray)
                            
                            Text("No Statistics Available")
                                .font(.title2)
                                .fontWeight(.semibold)
                                .foregroundColor(.gray)
                            
                            Text("Play some games to see statistics here")
                                .font(.body)
                                .foregroundColor(.secondary)
                                .multilineTextAlignment(.center)
                        }
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 50)
                    }
                    
                    Spacer()
                }
                .padding()
            }
            .navigationTitle("Statistics")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

struct StatCard: View {
    let title: String
    let value: String
    let color: Color
    
    var body: some View {
        VStack(spacing: 8) {
            Text(title)
                .font(.caption)
                .fontWeight(.semibold)
                .foregroundColor(.secondary)
                .multilineTextAlignment(.center)
            
            Text(value)
                .font(.title2)
                .fontWeight(.bold)
                .foregroundColor(color)
        }
        .frame(maxWidth: .infinity)
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(10)
    }
}

struct WinRateCard: View {
    let player: String
    let wins: Int
    let total: Int
    let color: Color
    
    var winRate: Double {
        total > 0 ? Double(wins) / Double(total) * 100 : 0
    }
    
    var body: some View {
        VStack(spacing: 8) {
            Text(player)
                .font(.headline)
                .fontWeight(.bold)
                .foregroundColor(color)
            
            Text("\(wins)/\(total)")
                .font(.title3)
                .fontWeight(.semibold)
            
            Text(String(format: "%.1f%%", winRate))
                .font(.caption)
                .foregroundColor(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(10)
    }
}

struct AverageScoreCard: View {
    let player: String
    let average: Double
    let color: Color
    
    var body: some View {
        VStack(spacing: 8) {
            Text(player)
                .font(.headline)
                .fontWeight(.bold)
                .foregroundColor(color)
            
            Text(String(format: "%.1f", average))
                .font(.title2)
                .fontWeight(.bold)
                .foregroundColor(color)
            
            Text("Average")
                .font(.caption)
                .foregroundColor(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(10)
    }
}

#Preview {
    StatsView()
        .environmentObject(MatchStore())
}
