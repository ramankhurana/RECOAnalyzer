import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = "80X_dataRun2_Prompt_ICHEP16JEC_v0"

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/008F73B2-4856-E611-9DA2-0025905B859A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/0415447D-4B56-E611-8667-0CC47A4C8E2A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/06B0D5BE-4956-E611-B700-0025905A610C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/124ACEA5-4B56-E611-8716-003048FFD7CE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/12A4A682-4B56-E611-803E-0CC47A4C8E38.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/12F5CD22-4C56-E611-9B3F-0025905A6094.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/1479C27F-4C56-E611-B6EF-0CC47A4D7664.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/18B76CBC-4B56-E611-92B2-0CC47A4D7654.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/26193CCD-4B56-E611-B41B-0025905B8574.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/26DD5620-4C56-E611-AB9A-0025905B85C6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/285365F1-4956-E611-9561-0CC47A78A360.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/285DD4AF-4956-E611-B483-0CC47A4D76D2.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/2C334713-4956-E611-B3B3-0CC47A4C8E46.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/2C6F00B2-4B56-E611-AF85-0CC47A4D7650.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/2E6A57D3-4956-E611-84F7-0025905B8594.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/3024758C-4856-E611-8F6C-0CC47A4D75F2.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/307D77D5-4956-E611-A1AD-0025905B85CA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/348F4C60-4C56-E611-B23C-0CC47A4D7614.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/367881B7-4856-E611-A806-0025905B85C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/3CC244CB-4956-E611-A786-0CC47A4C8E7E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/3E7C94D3-4956-E611-B7C6-0025905B85DE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/4AA102C6-4956-E611-A08A-0CC47A4D762E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/4CAF3302-4A56-E611-9387-0025905A607A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/4E68FFE2-4B56-E611-A67C-0CC47A4D7628.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/50438D90-4C56-E611-8E6D-0CC47A78A2F6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/5C170EE5-4B56-E611-8EAD-0CC47A78A414.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/5CE5DE8A-4856-E611-8F2A-0CC47A4C8EB0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/62C1ADFB-4956-E611-B37D-0025905B85B2.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/641CE7E7-4956-E611-957B-0025905A60A0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/64A2E326-4C56-E611-A877-0025905A6092.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/6826C43B-4C56-E611-9B30-0CC47A4D760A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/68993997-4956-E611-90C8-0025905A6084.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/6EF901C1-4B56-E611-B243-0025905B8568.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/70C1E778-4856-E611-AC10-0CC47A74525A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/723446FE-4956-E611-8CA4-0025905A48B2.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/7286BEF5-4B56-E611-9513-0025905A612C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/729FE88C-4956-E611-A256-0025905A613C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/78428823-4C56-E611-A887-0025905A60E4.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/84B2927D-4856-E611-8391-0CC47A4D761A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/86000922-4C56-E611-AEFD-0025905B85DE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/8A20480F-4C56-E611-B644-0CC47A78A408.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/8A4854FF-4A56-E611-9A9A-0025905A6138.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/8CA41A16-4C56-E611-B7CF-0CC47A4D75F0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/8CCFCA98-4856-E611-9FE1-0CC47A4D7640.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/9016099C-4856-E611-BFA5-0CC47A4C8E1E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/98373719-4C56-E611-8A02-0CC47A78A418.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/9AD3ADE8-4956-E611-9B61-0025905A60C6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/A0140516-4C56-E611-9AC1-0CC47A78A340.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/A0BEE378-4C56-E611-AF5C-0CC47A4C8E8A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/A0C0E10F-4C56-E611-AF63-0CC47A4D75F8.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/A4CD7BF8-4956-E611-945A-0025905B858A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/A6C2017D-4856-E611-B7A9-0CC47A4D762A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/A82BAEC6-4B56-E611-AE7D-0025905A48F0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/A8D36099-4B56-E611-885C-0025905A6118.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/AEBB149B-4856-E611-9128-0025905A48FC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/AEE66903-4C56-E611-B019-0025905B858C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/B008F196-4956-E611-8AFD-0CC47A78A2F6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/B0C147CD-4956-E611-A2E6-0CC47A78A30E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/BE6ACB21-4C56-E611-9D56-0025905B8604.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/BEE9C921-4C56-E611-9832-0025905B85C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/C023FC30-4C56-E611-A6F7-0CC47A4C8E20.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/C47C068C-4856-E611-A156-0CC47A4D76BE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/C48556E9-4B56-E611-B5A7-0025905A60FE.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/C6B47886-4C56-E611-B86A-0CC47A74525A.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/C6EA141E-4C56-E611-B0C8-0025905B85BC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/CC2B97CF-4956-E611-8482-0025905B85A2.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/D2B9EBFA-4956-E611-B1AC-0025905B855E.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/D4F1E820-4C56-E611-9DB7-0025905A612C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/D82269CD-4956-E611-B3B4-0CC47A4C8F18.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/D89ECCC5-4956-E611-9736-0025905A48C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/D8A7A4B2-4956-E611-8543-0CC47A4D7602.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/D8AFA003-4A56-E611-BE47-0025905B8576.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/DC83669F-4C56-E611-87CC-0025905A60A0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/DE6A7C91-4C56-E611-BA3D-0025905B8582.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/DE7B0EC4-4956-E611-817D-0CC47A4C8E70.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/E0A48905-4956-E611-AF9F-0CC47A4C8F10.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/E23C3D0A-4C56-E611-896B-0CC47A4D7664.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/E406095E-4C56-E611-9F90-0CC47A78A41C.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/EA4C7D8F-4B56-E611-B4CC-0025905A6068.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/EA8D4A2B-4C56-E611-A6E5-0025905A48C0.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/ECCA6CA0-4856-E611-A269-0CC47A4C8E96.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/EE9A0B25-4E56-E611-A5C8-0025905A60DA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/F0C3CE0B-4C56-E611-8761-0025905A48BA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/F2A5A005-4C56-E611-AB25-0025905B85B6.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/F2B62457-4C56-E611-819F-0025905B8596.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/F4F8351E-4956-E611-A86C-0025905A48F2.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/F803B58B-4856-E611-BE40-0CC47A4D7630.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/FE2E5214-4C56-E611-912E-0025905B85CA.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/FEBE5823-4C56-E611-AF31-0025905B85EC.root',
       '/store/relval/CMSSW_8_1_0_pre9/RelValSingleElectronPt35Extended/GEN-SIM-RECO/PU25ns_81X_mcRun2_asymptotic_v2_2023tiltedPU140-v1/10000/FEF89150-4C56-E611-A414-0025905A4964.root'
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
    fileName = cms.string("histo_elgun_pu140.root"),
    closeFileFast = cms.untracked.bool(True)
)

#process.p = cms.Path(process.ak4PFCHSL1FastL2L3CorrectorChain + process.ak4PFchsCorrectedJets + process.selectedHadronsAndPartons + process.ak4JetFlavourInfos + process.check)
process.p = cms.Path(process.selectedHadronsAndPartons + process.ak4JetFlavourInfos + process.check)
