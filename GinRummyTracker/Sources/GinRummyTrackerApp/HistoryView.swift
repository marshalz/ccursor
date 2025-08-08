import SwiftUI

struct HistoryView: View {
    @EnvironmentObject var matchStore: MatchStore
    @State private var showingClearAlert = false
    
    var body: some View {
        NavigationView {
            List {
                if matchStore.matches.isEmpty {
                    VStack(spacing: 20) {
                        Image(systemName: "list.bullet.clipboard")
                            .font(.system(size: 60))
                            .foregroundColor(.gray)
                        
                        Text("No Match History")
                            .font(.title2)
                            .fontWeight(.semibold)
                            .foregroundColor(.gray)
                        
                        Text("Start playing games to see your match history here")
                            .font(.body)
                            .foregroundColor(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 50)
                    .listRowBackground(Color.clear)
                } else {
                    ForEach(matchStore.matches.reversed(), id: \.id) { match in
                        MatchRowView(match: match)
                    }
                }
            }
            .navigationTitle("Match History")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Clear All") {
                        showingClearAlert = true
                    }
                    .foregroundColor(.red)
                }
            }
        }
        .alert("Clear All History", isPresented: $showingClearAlert) {
            Button("Cancel", role: .cancel) { }
            Button("Clear All", role: .destructive) {
                matchStore.clearAllMatches()
            }
        } message: {
            Text("Are you sure you want to clear all match history? This action cannot be undone.")
        }
    }
}

struct MatchRowView: View {
    let match: Match
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                VStack(alignment: .leading) {
                    Text("Winner: \(match.winner)")
                        .font(.headline)
                        .fontWeight(.bold)
                        .foregroundColor(match.winner == "Zayaka" ? .blue : .green)
                    
                    Text(match.matchDate, style: .date)
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                }
                
                Spacer()
                
                VStack(alignment: .trailing) {
                    Text("Final Scores")
                        .font(.caption)
                        .foregroundColor(.secondary)
                    
                    HStack(spacing: 15) {
                        VStack {
                            Text("Zayaka")
                                .font(.caption)
                                .foregroundColor(.blue)
                            Text("\(match.zayakaScore)")
                                .font(.title3)
                                .fontWeight(.bold)
                                .foregroundColor(.blue)
                        }
                        
                        VStack {
                            Text("Brian")
                                .font(.caption)
                                .foregroundColor(.green)
                            Text("\(match.brianScore)")
                                .font(.title3)
                                .fontWeight(.bold)
                                .foregroundColor(.green)
                        }
                    }
                }
            }
            
            if !match.gameScores.isEmpty {
                VStack(alignment: .leading, spacing: 5) {
                    Text("Game Scores:")
                        .font(.caption)
                        .fontWeight(.semibold)
                        .foregroundColor(.secondary)
                    
                    Text(match.gameScores)
                        .font(.caption)
                        .foregroundColor(.secondary)
                        .lineLimit(2)
                }
            }
        }
        .padding(.vertical, 8)
    }
}

#Preview {
    HistoryView()
        .environmentObject(MatchStore())
}
