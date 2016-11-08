import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = "80X_dataRun2_Prompt_ICHEP16JEC_v0"

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/0A61CD3D-7455-E611-B742-0025905B85DC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/147E2900-7555-E611-BF8B-0025905A48C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/1AD3B693-7155-E611-814F-0025905A48C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/207DB223-7255-E611-BD8E-0025905B8592.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/224B7613-7155-E611-AB76-0025905B85CA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/3027C821-7255-E611-9C8C-0025905B85CA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/32686213-7155-E611-82A3-0025905B85CA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/3AEC1622-7255-E611-B197-0025905B856E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/40C4DA7C-7055-E611-8FE7-0CC47A78A42C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/42B33642-7255-E611-B5BE-0CC47A78A4BA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/448AABF8-7755-E611-A9FA-0025905B8582.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/62091A13-7055-E611-ABDB-0CC47A4C8E1C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/721C6AF2-7255-E611-A57E-0025905B85DC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/80ED20DB-7155-E611-8A85-0CC47A78A45A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/8E6829C5-6E55-E611-94DF-0CC47A4C8E1C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/94FB3728-7355-E611-B1F6-0CC47A78A3D8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/9665CC4A-7855-E611-97C8-0CC47A78A3D8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/98933D34-7055-E611-88FC-0CC47A78A4BA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/9A7C8583-7555-E611-A7EE-0CC47A4D762E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/A4DC847E-7555-E611-BA23-0025905B85DC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/A66440F7-7055-E611-B4B7-0025905A48C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/AE496D14-7155-E611-8208-0025905B8592.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/B0F01539-7355-E611-BA04-0CC47A7452D8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/B4D45F16-7355-E611-913D-0CC47A4C8E64.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/C82B0AB0-6E55-E611-A5DE-0CC47A78A45A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/CA0D2CF1-7255-E611-A727-0CC47A4C8E2A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/D6C6B2F0-7255-E611-9C64-0025905A60B8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/DABB257D-7055-E611-BB04-0CC47A4C8F10.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/DEF3D7F0-7255-E611-B8F9-0CC47A78A42C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/E04738EF-7255-E611-BDC3-0CC47A4D764A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/E4E2D294-7055-E611-B7AA-0CC47A4C8E64.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/E69C0FE7-7055-E611-9E40-0CC47A4D762E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/F88BD221-7255-E611-97E3-0025905A48D8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/FA5F7E7E-7055-E611-8095-0025905B856E.root'
    )
)

process.load('JetMETCorrections.Configuration.JetCorrectors_cff')

process.ak4PFchsCorrectedJets   = cms.EDProducer('CorrectedPFJetProducer',
    src         = cms.InputTag('ak4PFJetsCHS'),
    correctors  = cms.VInputTag('ak4PFCHSL1FastL2L3Corrector')
)

process.load("PhysicsTools/JetMCAlgos/HadronAndPartonSelector_cfi")  
process.load("PhysicsTools/JetMCAlgos/AK4PFJetsMCFlavourInfos_cfi")
#process.ak4JetFlavourInfos.jets = cms.InputTag("ak4PFchsCorrectedJets")
process.ak4JetFlavourInfos.jets = cms.InputTag("ak4PFJetsCHS")

process.check = cms.EDAnalyzer("RECOAnalyzer",
    vertices = cms.InputTag("offlinePrimaryVertices"),
    #jets = cms.InputTag("ak4PFchsCorrectedJets"),
    jets = cms.InputTag("ak4PFJetsCHS"),
    btags = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
    flavorinfo = cms.InputTag("ak4JetFlavourInfos"),
    genparticles = cms.InputTag("genParticles"),
    electrons = cms.InputTag("gedGsfElectrons"),
    beamspot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("particleFlowEGamma"),
    muons = cms.InputTag("muons"),
    debug = cms.bool(False)
)

process.TFileService = cms.Service("TFileService", 
    fileName = cms.string("histo_elgun_pu35.root"),
    closeFileFast = cms.untracked.bool(True)
)

#process.p = cms.Path(process.ak4PFCHSL1FastL2L3CorrectorChain + process.ak4PFchsCorrectedJets + process.selectedHadronsAndPartons + process.ak4JetFlavourInfos + process.check)
process.p = cms.Path(process.selectedHadronsAndPartons + process.ak4JetFlavourInfos + process.check)
