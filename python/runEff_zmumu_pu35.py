import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = "80X_dataRun2_Prompt_ICHEP16JEC_v0"

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/0AEA09D9-6355-E611-9846-0CC47A4C8EC6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/0CFABC06-6255-E611-BC06-0CC47A78A42C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/0E7927D9-6755-E611-9A0E-0CC47A78A45A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/18154007-6255-E611-9326-0CC47A78A440.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/1A332408-6255-E611-8E54-0025905A60DA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/2E673F5E-6C55-E611-84EB-0025905B85CA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/3ADAAD02-6255-E611-A1EB-0CC47A4D7638.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/4849E606-6255-E611-8E73-0CC47A4D7690.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/4EC7B701-6255-E611-8F3C-0025905A48EC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/5CD36E26-6755-E611-87CF-0025905B858C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/62ABB82B-6755-E611-99C3-0CC47A4D765A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/6CC791CD-6655-E611-A475-0CC47A4C8F10.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/6CFFB6CF-6655-E611-95E8-0CC47A78A456.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/7AA5ECDE-6355-E611-9F73-0025905A60DA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/7C1F6F0E-6855-E611-AC75-0CC47A4D75F2.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/801A4B25-6755-E611-A00A-0CC47A4D762E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/88A56F98-6455-E611-B782-0CC47A4C8EB6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/8A0D1716-6C55-E611-BFC5-0025905B856E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/8CBA8CB4-6755-E611-B43E-0CC47A78A456.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/8CE49276-6655-E611-990D-0CC47A78A456.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/8E92164C-6755-E611-A6B5-0CC47A7452D8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/9EA2FF00-6355-E611-A5F8-0CC47A78A45A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/A4A12D29-6755-E611-80E7-0025905B856E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/A69CF103-6255-E611-A5ED-0CC47A78A478.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/AAE2C69B-6455-E611-8C5B-0025905A48C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/B0CBB4B1-6755-E611-9047-0025905A48C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/B4857C98-6455-E611-A7B5-0025905A60BC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/BEE728E0-6355-E611-B39D-0025905B8592.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/C2233479-6655-E611-A217-0CC47A78A426.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/C4EC61FF-6455-E611-A35C-0025905B85B6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/CC014007-6255-E611-B95D-0CC47A78A440.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/D29E2BFD-6455-E611-96C9-0025905A48EC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/E67BAE72-6255-E611-A798-0CC47A7452D8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/ECC07B23-6755-E611-9A84-0025905A60E4.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/F0BCA7CA-6655-E611-AA01-0025905B856E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/F0E5BA06-6255-E611-A091-0CC47A78A42C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/F2767126-6755-E611-820F-0CC47A78A42C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/F6058F13-6555-E611-9D3D-0CC47A78A3D8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValZMM_13/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU35-v1/10000/FC03F11E-6755-E611-8223-0CC47A4D75F2.root'
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
    fileName = cms.string("histo_zmumu_pu35.root"),
    closeFileFast = cms.untracked.bool(True)
)

#process.p = cms.Path(process.ak4PFCHSL1FastL2L3CorrectorChain + process.ak4PFchsCorrectedJets + process.selectedHadronsAndPartons + process.ak4JetFlavourInfos + process.check)
process.p = cms.Path(process.selectedHadronsAndPartons + process.ak4JetFlavourInfos + process.check)
