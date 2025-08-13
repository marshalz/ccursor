import SwiftUI

struct ScoreEntryView: View {
    @EnvironmentObject var matchStore: MatchStore
    @State private var zayakaScore = ""
    @State private var brianScore = ""
    @State private var showingWinnerAlert = false
    @State private var winnerMessage = ""
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 20) {
                    // Title
                    Text("GinRummy Score Tracker")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.primary)
                        .padding(.top)
                    
                    // Score Entry Section
                    VStack(spacing: 15) {
                        Text("Enter Game Scores")
                            .font(.title2)
                            .fontWeight(.semibold)
                            .frame(maxWidth: .infinity, alignment: .leading)
                        
                        HStack(spacing: 20) {
                            // Zayaka's Score
                            VStack(alignment: .leading, spacing: 8) {
                                Text("Zayaka's Score")
                                    .font(.headline)
                                    .fontWeight(.bold)
                                    .foregroundColor(.blue)
                                
                                TextField("Enter score", text: $zayakaScore)
                                    .keyboardType(.numberPad)
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .font(.system(size: 24, weight: .bold))
                                    .frame(height: 50)
                            }
                            
                            // Brian's Score
                            VStack(alignment: .leading, spacing: 8) {
                                Text("Brian's Score")
                                    .font(.headline)
                                    .fontWeight(.bold)
                                    .foregroundColor(.green)
                                
                                TextField("Enter score", text: $brianScore)
                                    .keyboardType(.numberPad)
                                    .textFieldStyle(RoundedBorderTextFieldStyle())
                                    .font(.system(size: 24, weight: .bold))
                                    .frame(height: 50)
                            }
                        }
                        
                        // Buttons
                        HStack(spacing: 15) {
                            Button(action: addScores) {
                                Text("Add Scores")
                                    .font(.title3)
                                    .fontWeight(.bold)
                                    .foregroundColor(.white)
                                    .frame(maxWidth: .infinity)
                                    .frame(height: 50)
                                    .background(Color.blue)
                                    .cornerRadius(10)
                            }
                            
                            Button(action: clearFields) {
                                Text("Clear")
                                    .font(.title3)
                                    .fontWeight(.bold)
                                    .foregroundColor(.white)
                                    .frame(maxWidth: .infinity)
                                    .frame(height: 50)
                                    .background(Color.gray)
                                    .cornerRadius(10)
                            }
                        }
                    }
                    .padding()
                    .background(Color(.systemGray6))
                    .cornerRadius(15)
                    
                    // Current Totals Section
                    VStack(spacing: 15) {
                        Text("Current Match Totals")
                            .font(.title2)
                            .fontWeight(.semibold)
                            .frame(maxWidth: .infinity, alignment: .leading)
                        
                        HStack(spacing: 30) {
                            VStack {
                                Text("Zayaka")
                                    .font(.headline)
                                    .fontWeight(.bold)
                                    .foregroundColor(.blue)
                                
                                Text("\(matchStore.currentZayakaTotal)")
                                    .font(.system(size: 36, weight: .bold))
                                    .foregroundColor(.blue)
                            }
                            
                            VStack {
                                Text("Brian")
                                    .font(.headline)
                                    .fontWeight(.bold)
                                    .foregroundColor(.green)
                                
                                Text("\(matchStore.currentBrianTotal)")
                                    .font(.system(size: 36, weight: .bold))
                                    .foregroundColor(.green)
                            }
                        }
                        .padding()
                        .background(Color(.systemGray6))
                        .cornerRadius(15)
                    }
                    
                    // Status
                    if !matchStore.gameScores.isEmpty {
                        VStack(alignment: .leading, spacing: 10) {
                            Text("Recent Game Scores")
                                .font(.headline)
                                .fontWeight(.semibold)
                            
                            ForEach(matchStore.gameScores.suffix(3), id: \.self) { score in
                                Text(score)
                                    .font(.subheadline)
                                    .foregroundColor(.secondary)
                            }
                        }
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .padding()
                        .background(Color(.systemGray6))
                        .cornerRadius(15)
                    }
                    
                    Spacer()
                }
                .padding()
            }
            .navigationTitle("Score Entry")
            .navigationBarTitleDisplayMode(.inline)
        }
        .alert("Match Complete!", isPresented: $showingWinnerAlert) {
            Button("OK") { }
        } message: {
            Text(winnerMessage)
        }
    }
    
    private func addScores() {
        let zayaka = Int(zayakaScore) ?? 0
        let brian = Int(brianScore) ?? 0
        
        if zayaka == 0 && brian == 0 {
            return
        }
        
        matchStore.addGameScore(zayakaScore: zayaka, brianScore: brian)
        
        // Clear fields
        zayakaScore = ""
        brianScore = ""
        
        // Check if match ended
        if matchStore.currentZayakaTotal >= 100 || matchStore.currentBrianTotal >= 100 {
            let winner = matchStore.currentZayakaTotal >= 100 ? "Zayaka" : "Brian"
            winnerMessage = "Winner: \(winner)\nFinal Scores:\nZayaka: \(matchStore.currentZayakaTotal)\nBrian: \(matchStore.currentBrianTotal)"
            showingWinnerAlert = true
        }
    }
    
    private func clearFields() {
        zayakaScore = ""
        brianScore = ""
    }
}

#Preview {
    ScoreEntryView()
        .environmentObject(MatchStore())
}
