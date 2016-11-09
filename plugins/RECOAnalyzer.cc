// -*- C++ -*-
//
// Package:    TriggerEff/RECOAnalyzer
// Class:      RECOAnalyzer
// 
/**\class RECOAnalyzer RECOAnalyzer.cc TriggerEff/RECOAnalyzer/plugins/RECOAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Dylan Sheldon Rankin
//         Created:  Tue, 12 Jul 2016 15:16:15 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/PatCandidates/interface/Jet.h"

#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/BTauReco/interface/JetTag.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "SimDataFormats/JetMatching/interface/JetFlavour.h"
#include "SimDataFormats/JetMatching/interface/JetFlavourInfoMatching.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TTree.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TLorentzVector.h"

typedef math::XYZPoint Point;

//
// class declaration
//

class RECOAnalyzer : public edm::EDAnalyzer {
   public:
      explicit RECOAnalyzer(const edm::ParameterSet&);
      ~RECOAnalyzer();

   private:
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

      // ----------member data ---------------------------
      edm::EDGetTokenT<reco::VertexCollection> vtxToken_;
      edm::EDGetTokenT<std::vector<reco::GenParticle>> genToken_;
      edm::EDGetTokenT<std::vector<reco::PFJet>> jetToken_;
      edm::EDGetTokenT<reco::JetTagCollection> bToken_;
      edm::EDGetTokenT<reco::JetFlavourInfoMatchingCollection> flavToken_;
      edm::EDGetTokenT<std::vector<reco::GsfElectron>> elToken_;
      edm::EDGetTokenT<reco::BeamSpot> bsToken_;
      edm::EDGetTokenT<std::vector<reco::Conversion>> convToken_;
      edm::EDGetTokenT<std::vector<reco::Muon>> muToken_;
/*
 * These are the collections that we plan to import and use in the rest of the analyzer.
 */

      TH1F *nvtx;
      TH1F *elnum, *elden, *munum, *muden, *btnum, *btden;
      TH1F *elnum3, *elden3, *munum3, *muden3, *btnum3, *btden3;
      TH1F *mtnum, *mtden, *mtnum3, *mtden3;

      TH2F *elcutflow, *mucutflow;
      TH1F *eletanum, *eletaden, *muetanum, *muetaden, *btetanum, *btetaden;
      TH1F *eletanum3, *eletaden3, *muetanum3, *muetaden3, *btetanum3, *btetaden3;
      TH1F *mtetanum, *mtetaden, *mtetanum3, *mtetaden3;
      TH2F *eletacutflow, *muetacutflow;
      TH2F *eldist, *mudist;
      TH2F *btdist, *mtdist;

/*
 * These are the histograms that we will fill in the analyzer.
 */

      bool debug;

  struct JetRefCompare :
    public std::binary_function<edm::RefToBase<reco::Jet>, edm::RefToBase<reco::Jet>, bool> {
    inline bool operator () (const edm::RefToBase<reco::Jet> &j1,
			     const edm::RefToBase<reco::Jet> &j2) const
    { return j1.id() < j2.id() || (j1.id() == j2.id() && j1.key() < j2.key()); }
  };

  typedef std::map<edm::RefToBase<reco::Jet>, unsigned int, JetRefCompare> FlavourMap;

};

RECOAnalyzer::RECOAnalyzer(const edm::ParameterSet& iConfig):
    vtxToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertices"))),
    genToken_(consumes<std::vector<reco::GenParticle>>(iConfig.getParameter<edm::InputTag>("genparticles"))),
    jetToken_(consumes<std::vector<reco::PFJet>>(iConfig.getParameter<edm::InputTag>("jets"))),
    bToken_(consumes<reco::JetTagCollection>(iConfig.getParameter<edm::InputTag>("btags"))),
    flavToken_(consumes<reco::JetFlavourInfoMatchingCollection>(iConfig.getParameter<edm::InputTag>("flavorinfo"))),
    elToken_(consumes<std::vector<reco::GsfElectron>>(iConfig.getParameter<edm::InputTag>("electrons"))),
    bsToken_(consumes<reco::BeamSpot>(iConfig.getParameter<edm::InputTag>("beamspot"))),
    convToken_(consumes<std::vector<reco::Conversion>>(iConfig.getParameter<edm::InputTag>("conversions"))),
    muToken_(consumes<std::vector<reco::Muon>>(iConfig.getParameter<edm::InputTag>("muons"))),
    debug(iConfig.getParameter<bool>("debug"))
/*
 * This takes the information given in the cmsRun config file (runEff.py) and stores it in the tokens we defined earlier.
 */

{
    edm::Service<TFileService> fs;
/*
 * This defines the fileservice, which allows us to store the histograms we are going to define in a file.
 */

    nvtx      = fs->make<TH1F>( "nvtx", "nvtx" , 250, 0, 250);
/*
 * This is an example of how to define the histograms we are interested in and specify the name/title/binning
 * The syntax should be self evident (the" fs->make<TH1F>" is required in order for the fileservice file to recognize which histogram you want to save.
 * A similar syntax can be used to save TTrees and other TObjects
 */
    elnum     = fs->make<TH1F>( "elnum", "elnum" , 100, 0, 1000);
    elden     = fs->make<TH1F>( "elden", "elden" , 100, 0, 1000);
    elnum3     = fs->make<TH1F>( "elnum3", "elnum3" , 100, 0, 1000);
    elden3     = fs->make<TH1F>( "elden3", "elden3" , 100, 0, 1000);
/*
 * The "3" suffix here is meant to indicate the genParticle status code used to define the efficiencies
 */
    munum     = fs->make<TH1F>( "munum", "munum" , 100, 0, 1000);
    muden     = fs->make<TH1F>( "muden", "muden" , 100, 0, 1000);
    munum3     = fs->make<TH1F>( "munum3", "munum3" , 100, 0, 1000);
    muden3     = fs->make<TH1F>( "muden3", "muden3" , 100, 0, 1000);
    btnum     = fs->make<TH1F>( "btnum", "btnum" , 100, 0, 1000);
    btden     = fs->make<TH1F>( "btden", "btden" , 100, 0, 1000);
    btnum3     = fs->make<TH1F>( "btnum3", "btnum3" , 100, 0, 1000);
    btden3     = fs->make<TH1F>( "btden3", "btden3" , 100, 0, 1000);
    mtnum     = fs->make<TH1F>( "mtnum", "mtnum" , 100, 0, 1000);
    mtden     = fs->make<TH1F>( "mtden", "mtden" , 100, 0, 1000);
    mtnum3     = fs->make<TH1F>( "mtnum3", "mtnum3" , 100, 0, 1000);
    mtden3     = fs->make<TH1F>( "mtden3", "mtden3" , 100, 0, 1000);
    eletanum     = fs->make<TH1F>( "eletanum", "eletanum" , 60, -3, 3);
    eletaden     = fs->make<TH1F>( "eletaden", "eletaden" , 60, -3, 3);
    eletanum3     = fs->make<TH1F>( "eletanum3", "eletanum3" , 60, -3, 3);
    eletaden3     = fs->make<TH1F>( "eletaden3", "eletaden3" , 60, -3, 3);
    muetanum     = fs->make<TH1F>( "muetanum", "muetanum" , 60, -3, 3);
    muetaden     = fs->make<TH1F>( "muetaden", "muetaden" , 60, -3, 3);
    muetanum3     = fs->make<TH1F>( "muetanum3", "muetanum3" , 60, -3, 3);
    muetaden3     = fs->make<TH1F>( "muetaden3", "muetaden3" , 60, -3, 3);
    btetanum     = fs->make<TH1F>( "btetanum", "btetanum" , 60, -3, 3);
    btetaden     = fs->make<TH1F>( "btetaden", "btetaden" , 60, -3, 3);
    btetanum3     = fs->make<TH1F>( "btetanum3", "btetanum3" , 60, -3, 3);
    btetaden3     = fs->make<TH1F>( "btetaden3", "btetaden3" , 60, -3, 3);
    mtetanum     = fs->make<TH1F>( "mtetanum", "mtetanum" , 60, -3, 3);
    mtetaden     = fs->make<TH1F>( "mtetaden", "mtetaden" , 60, -3, 3);
    mtetanum3     = fs->make<TH1F>( "mtetanum3", "mtetanum3" , 60, -3, 3);
    mtetaden3     = fs->make<TH1F>( "mtetaden3", "mtetaden3" , 60, -3, 3);
    elcutflow = fs->make<TH2F>( "elcutflow", "elcutflow", 50, 0., 500., 10, 0.5, 10.5);
    mucutflow = fs->make<TH2F>( "mucutflow", "mucutflow", 50, 0., 500., 10, 0.5, 10.5);
    eletacutflow = fs->make<TH2F>( "eletacutflow", "eletacutflow", 60, -3., 3., 10, 0.5, 10.5);
    muetacutflow = fs->make<TH2F>( "muetacutflow", "muetacutflow", 60, -3., 3., 10, 0.5, 10.5);
    eldist = fs->make<TH2F>( "eldist", "eldist", 50, 0., 500., 60, -3., 3.);
    mudist = fs->make<TH2F>( "mudist", "mudist", 50, 0., 500., 60, -3., 3.);
    btdist = fs->make<TH2F>( "btdist", "btdist", 50, 0., 500., 60, -3., 3.);
    mtdist = fs->make<TH2F>( "mtdist", "mtdist", 50, 0., 500., 60, -3., 3.);
}

RECOAnalyzer::~RECOAnalyzer()
{
}

void
RECOAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

    
    std::vector<TLorentzVector> rmv;
    std::vector<TLorentzVector> rmtv;
    std::vector<TLorentzVector> rev;
    std::vector<TLorentzVector> retv;
    TLorentzVector tmpvec;

    edm::Handle<reco::VertexCollection> vertices;
    iEvent.getByToken(vtxToken_, vertices);
    if (vertices->empty()) return; // skip the event if no PV found
    nvtx->Fill(vertices->size());
    Point PVtx = vertices->at(0).position();

    edm::Handle<reco::JetTagCollection> bTagHandle;
    iEvent.getByToken(bToken_, bTagHandle);
    const reco::JetTagCollection & bTags = *(bTagHandle.product());
/*
 * This is the standard way to get the collection you are interested in from the input file.
 */

    FlavourMap flavours;
    //Get flavour matching collection
    edm::Handle<reco::JetFlavourInfoMatchingCollection> jetMC;
    iEvent.getByToken(flavToken_, jetMC);
    for (reco::JetFlavourInfoMatchingCollection::const_iterator iter = jetMC->begin(); iter != jetMC->end(); iter++) {
        unsigned int fl = std::abs(iter->second.getHadronFlavour());
        flavours.insert(FlavourMap::value_type(iter->first, fl));
    }

    edm::Handle<std::vector<reco::PFJet>> jets;
    iEvent.getByToken(jetToken_, jets);
    for (const reco::PFJet &j : *jets) {
        if (j.pt() < 25) continue;
        bool match = false;
        double bdisc = -1.;
        int jflav = 0;
        tmpvec.SetPtEtaPhiE(j.pt(), j.eta(), j.phi(), j.energy());
        for (unsigned int i = 0; i != bTags.size(); ++i) {
            TLorentzVector tmpvec1;
            tmpvec1.SetPtEtaPhiE(bTags[i].first->pt(),bTags[i].first->eta(),bTags[i].first->phi(),bTags[i].first->energy());
            if (tmpvec.DeltaR(tmpvec1)<0.3 && fabs((tmpvec.Pt()-tmpvec1.Pt())/tmpvec.Pt()) < 0.5 ) { //this is the matching criteria (dR<0.3 and dpT/pT<0.5)
                 match = true;
                 bdisc = bTags[i].second;
                 edm::RefToBase<reco::Jet> aJet = bTags[i].first;
                 if (flavours.find (aJet) == flavours.end()) {
                 } else {
                   jflav = flavours[aJet];
                 }
                 break;
            }
        }
        if (match && abs(jflav)==5) { //if properly matched and the mcTruth flavour is a b-jet
            btden->Fill(j.pt());
            btetaden->Fill(j.eta());
            if (bdisc>0.460) { //current (2016) loose operating point
                btnum->Fill(j.pt());
                btetanum->Fill(j.eta());
            }
        }
        if (match && (abs(jflav)==21 or abs(jflav)<4)) {// if properly matched and mcTrth flavour is not b (udscg)
            mtden->Fill(j.pt());
            mtetaden->Fill(j.eta());
            if (bdisc>0.460) {
                mtnum->Fill(j.pt());
                mtetanum->Fill(j.eta());
            }
        }
    }

    edm::Handle<std::vector<reco::GenParticle>> genparts;
    iEvent.getByToken(genToken_, genparts);
    for (unsigned int i = 0; i != bTags.size(); ++i) {
        if (bTags[i].first->pt() < 25) continue;
        bool match = false;
        double bdisc = -1;
        TLorentzVector tmpvec, tmpvec1;
        tmpvec.SetPtEtaPhiE(bTags[i].first->pt(),bTags[i].first->eta(),bTags[i].first->phi(),bTags[i].first->energy());
        for (const reco::GenParticle &g : *genparts) {
            if (g.pt() < 20 or g.status()!=3 or abs(g.pdgId())!=5) continue;
            tmpvec1.SetPtEtaPhiE(g.pt(),g.eta(),g.phi(),g.energy());
            //if (tmpvec.DeltaR(tmpvec1)<0.3 && fabs((tmpvec.Pt()-tmpvec1.Pt())/tmpvec.Pt()) < 0.5 ) {
            if (tmpvec.DeltaR(tmpvec1)<0.3) {// no dpT/pT requirement
                 match = true;
                 bdisc = bTags[i].second;
                 break;
            }
        }
        if (match) {
            btden3->Fill(tmpvec1.Pt());
            btetaden3->Fill(tmpvec1.Eta());
            btdist->Fill(tmpvec1.Pt(),tmpvec1.Eta());
            if (bdisc>0.460) {
                btnum3->Fill(tmpvec1.Pt());
                btetanum3->Fill(tmpvec1.Eta());
            }
        }
        match = false;
        for (const reco::GenParticle &g : *genparts) {
            if (g.pt() < 20 or g.status()!=3 or (abs(g.pdgId())>3 and abs(g.pdgId())<=5) ) continue; //only udsg for mistag
            tmpvec1.SetPtEtaPhiE(g.pt(),g.eta(),g.phi(),g.energy());
            //if (tmpvec.DeltaR(tmpvec1)<0.3 && fabs((tmpvec.Pt()-tmpvec1.Pt())/tmpvec.Pt()) < 0.5 ) {
            if (tmpvec.DeltaR(tmpvec1)<0.3) {
                 match = true;
                 bdisc = bTags[i].second;
                 break;
            }
        }
        if (match) {
            mtden3->Fill(tmpvec1.Pt());
            mtden3->Fill(tmpvec1.Eta());
            mtdist->Fill(tmpvec1.Pt(),tmpvec1.Eta());
            if (bdisc>0.460) {
                mtnum3->Fill(tmpvec1.Pt());
                mtetanum3->Fill(tmpvec1.Eta());
            }
        }
    }

    edm::Handle<reco::ConversionCollection> conversions;
    iEvent.getByToken(convToken_, conversions);
    edm::Handle<reco::BeamSpot> bsHandle;
    iEvent.getByToken(bsToken_, bsHandle);
    const reco::BeamSpot &beamspot = *bsHandle.product();

    edm::Handle<std::vector<reco::GsfElectron>> electrons;
    iEvent.getByToken(elToken_, electrons);
    //int ec = 0;
    for (const reco::GsfElectron &e : *electrons) {
        //ec++;
        //std::cout<<"\nEl"<<ec<<" ";
        if (e.pt() < 10) continue;
        //std::cout<<"pt ";
        //std::cout<<"conv ";
        bool fail = false;
        elcutflow->Fill(e.pt(),1);
        eletacutflow->Fill(e.eta(),1);
        double Ooemoop = 999.;
        if (e.ecalEnergy()==0) Ooemoop = 999.;
        else if (!std::isfinite(e.ecalEnergy())) Ooemoop = 998.;
        else Ooemoop = (1.0/e.ecalEnergy() - e.eSuperClusterOverP()/e.ecalEnergy());
        if (fabs(e.superCluster()->eta())<1.4442) {
            if (e.full5x5_sigmaIetaIeta() >= 0.0103) {
                fail = true;
                elcutflow->Fill(e.pt(),2);
                eletacutflow->Fill(e.eta(),2);
            }
            //std::cout<<"sihih ";
            if (fabs(e.deltaEtaSuperClusterTrackAtVtx()) >= 0.0105) {
                fail = true;
                elcutflow->Fill(e.pt(),3);
                eletacutflow->Fill(e.eta(),3);
            }
            //std::cout<<"deta ";
            if (fabs(e.deltaPhiSuperClusterTrackAtVtx()) >= 0.115) {
                fail = true;
                elcutflow->Fill(e.pt(),4);
                eletacutflow->Fill(e.eta(),4);
            }
            //std::cout<<"dphi ";
            if (e.hcalOverEcal() >= 0.104) {
                fail = true;
                elcutflow->Fill(e.pt(),5);
                eletacutflow->Fill(e.eta(),5);
            }
            //std::cout<<"hoe ";
            if (Ooemoop >= 0.102) {
                fail = true;
                elcutflow->Fill(e.pt(),6);
                eletacutflow->Fill(e.eta(),6);
            }
            //std::cout<<"eop ";
            if (fabs(e.gsfTrack()->dxy(PVtx)) >= 0.0261) {
                fail = true;
                elcutflow->Fill(e.pt(),7);
                eletacutflow->Fill(e.eta(),7);
            }
            //std::cout<<"dxy ";
            if (fabs(e.gsfTrack()->dz(PVtx)) >= 0.41) {
                fail = true;
                elcutflow->Fill(e.pt(),8);
                eletacutflow->Fill(e.eta(),8);
            }
            //std::cout<<"dz ";
            if (e.gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) > 2) {
                fail = true;
                elcutflow->Fill(e.pt(),9);
                eletacutflow->Fill(e.eta(),9);
            }
            //std::cout<<"nhits ";
        }
        else if (fabs(e.superCluster()->eta())<1.556) continue;
        else if (fabs(e.superCluster()->eta())<2.5) {
            if (e.full5x5_sigmaIetaIeta() >= 0.0301) {
                fail = true;
                elcutflow->Fill(e.pt(),2);
                eletacutflow->Fill(e.eta(),2);
            }
            //std::cout<<"sihih ";
            if (fabs(e.deltaEtaSuperClusterTrackAtVtx()) >= 0.00814) {
                fail = true;
                elcutflow->Fill(e.pt(),3);
                eletacutflow->Fill(e.eta(),3);
            }
            //std::cout<<"deta ";
            if (fabs(e.deltaPhiSuperClusterTrackAtVtx()) >= 0.182) {
                fail = true;
                elcutflow->Fill(e.pt(),4);
                eletacutflow->Fill(e.eta(),4);
            }
            //std::cout<<"dphi ";
            if (e.hcalOverEcal() >= 0.0897) {
                fail = true;
                elcutflow->Fill(e.pt(),5);
                eletacutflow->Fill(e.eta(),5);
            }
            //std::cout<<"hoe ";
            if (Ooemoop >= 0.126) {
                fail = true;
                elcutflow->Fill(e.pt(),6);
                eletacutflow->Fill(e.eta(),6);
            }
            //std::cout<<"eop ";
            if (fabs(e.gsfTrack()->dxy(PVtx)) >= 0.118) {
                fail = true;
                elcutflow->Fill(e.pt(),7);
                eletacutflow->Fill(e.eta(),7);
            }
            //std::cout<<"dxy ";
            if (fabs(e.gsfTrack()->dz(PVtx)) >= 0.822) {
                fail = true;
                elcutflow->Fill(e.pt(),8);
                eletacutflow->Fill(e.eta(),8);
            }
            //std::cout<<"dz ";
            if (e.gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) > 1) {
                fail = true;
                elcutflow->Fill(e.pt(),9);
                eletacutflow->Fill(e.eta(),9);
            }
            //std::cout<<"nhits ";
        }
        else continue;
        if (ConversionTools::hasMatchedConversion(e, conversions, beamspot.position())) {
            fail = true;
            elcutflow->Fill(e.pt(),10);
            eletacutflow->Fill(e.eta(),10);
            }
        //if (fabs(e.convDist()) < 0.02 && fabs(e.convDcot()) < 0.02) fail = true;
        if (fail) continue;
        tmpvec.SetPtEtaPhiE(e.pt(),e.eta(),e.phi(),e.energy());
        rev.push_back(tmpvec);
        if (fabs(e.superCluster()->eta())<1.4442) {
            if (e.full5x5_sigmaIetaIeta() >= 0.0101) continue;
            if (fabs(e.deltaEtaSuperClusterTrackAtVtx()) >= 0.00926) continue;
            if (fabs(e.deltaPhiSuperClusterTrackAtVtx()) >= 0.0336) continue;
            if (e.hcalOverEcal() >= 0.0597) continue;
            if (Ooemoop >= 0.012) continue;
            if (fabs(e.gsfTrack()->dxy(PVtx)) >= 0.0111) continue;
            if (fabs(e.gsfTrack()->dz(PVtx)) >= 0.0466) continue;
            if (e.gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) > 2) continue;
        }
        else {
            if (e.full5x5_sigmaIetaIeta() >= 0.0279) continue;
            if (fabs(e.deltaEtaSuperClusterTrackAtVtx()) >= 0.00724) continue;
            if (fabs(e.deltaPhiSuperClusterTrackAtVtx()) >= 0.0918) continue;
            if (e.hcalOverEcal() >= 0.0615) continue;
            if (Ooemoop >= 0.00999) continue;
            if (fabs(e.gsfTrack()->dxy(PVtx)) >= 0.0351) continue;
            if (fabs(e.gsfTrack()->dz(PVtx)) >= 0.417) continue;
            if (e.gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) > 1) continue;
        }
        retv.push_back(tmpvec);
    }

    edm::Handle<std::vector<reco::Muon>> muons;
    iEvent.getByToken(muToken_, muons);
    for (const reco::Muon &m : *muons) {
        if (m.pt() < 10) continue;
        if (!(m.innerTrack().isNonnull() and m.innerTrack().isAvailable())) continue;
        if (!(m.globalTrack().isNonnull() and m.globalTrack().isAvailable())) continue;
        bool fail = false;
        mucutflow->Fill(m.pt(),1);
        muetacutflow->Fill(m.eta(),1);
        if (!m.isPFMuon()) {
            fail = true;
            mucutflow->Fill(m.pt(),2);
            muetacutflow->Fill(m.eta(),2);
        }
        if (!(m.isGlobalMuon() || m.isTrackerMuon())) {
            fail = true;
            mucutflow->Fill(m.pt(),3);
            muetacutflow->Fill(m.eta(),3);
        }
        tmpvec.SetPtEtaPhiE(m.pt(),m.eta(),m.phi(),m.energy());
        if (!fail) {
            rmv.push_back(tmpvec);
        }
        if (m.globalTrack()->normalizedChi2() >= 10) {
            fail = true;
            mucutflow->Fill(m.pt(),4);
            muetacutflow->Fill(m.eta(),4);
        }
        if (m.globalTrack()->hitPattern().numberOfValidMuonHits() == 0) {
            fail = true;
            mucutflow->Fill(m.pt(),5);
            muetacutflow->Fill(m.eta(),5);
        }
        if (m.numberOfMatchedStations() <= 1) {
            fail = true;
            mucutflow->Fill(m.pt(),6);
            muetacutflow->Fill(m.eta(),6);
        }
        if (fabs(m.muonBestTrack()->dxy(PVtx)) >= 0.2) {
            fail = true;
            mucutflow->Fill(m.pt(),7);
            muetacutflow->Fill(m.eta(),7);
        }
        if (fabs(m.muonBestTrack()->dz(PVtx)) >= 0.5) {
            fail = true;
            mucutflow->Fill(m.pt(),8);
            muetacutflow->Fill(m.eta(),8);
        }
        if (m.innerTrack()->hitPattern().numberOfValidPixelHits() == 0) {
            fail = true;
            mucutflow->Fill(m.pt(),9);
            muetacutflow->Fill(m.eta(),9);
        }
        if (m.innerTrack()->hitPattern().trackerLayersWithMeasurement() <= 5) {
            fail = true;
            mucutflow->Fill(m.pt(),10);
            muetacutflow->Fill(m.eta(),10);
        }
        if (fail) continue;
        rmtv.push_back(tmpvec);
    }

    for (const reco::GenParticle &g : *genparts) {
        //std::cout<<"\nGenPart ID"<<g.pdgId()<<" Stat"<<g.status()<<" Pt"<<g.pt();
        if (g.pt() < 10 or g.status()!=1) continue;
        if (abs(g.pdgId())!=11 and abs(g.pdgId())!=13) continue;
        tmpvec.SetPtEtaPhiE(g.pt(),g.eta(),g.phi(),g.energy());
        int pid = abs(g.pdgId());
        bool match = false;
        if (pid==11) {
            elden->Fill(g.pt());
            eletaden->Fill(g.eta());
            eldist->Fill(g.pt(),g.eta());
            for (unsigned int i=0; i<rev.size(); i++) {
                if (tmpvec.DeltaR(rev[i])<0.3 && fabs((g.pt()-rev[i].Pt())/g.pt()) < 0.5 ) {
                    match=true;
                    break;
                }
            }
            if (match) {
                elnum->Fill(g.pt());
                eletanum->Fill(g.eta());
            }
        }
        if (pid==13) {
            muden->Fill(g.pt());
            muetaden->Fill(g.eta());
            mudist->Fill(g.pt(),g.eta());
            for (unsigned int i=0; i<rmv.size(); i++) {
                if (tmpvec.DeltaR(rmv[i])<0.3 && fabs((g.pt()-rmv[i].Pt())/g.pt()) < 0.5 ) {
                    match=true;
                    break;
                }
            }
            if (match) {
                munum->Fill(g.pt());
                muetanum->Fill(g.eta());
            }
        }
    }

    for (const reco::GenParticle &g : *genparts) {
        if (debug) std::cout<<"\nGenPart ID"<<g.pdgId()<<" Stat"<<g.status()<<" Pt"<<g.pt();
        if (g.pt() < 10 or (g.status()!=23 and g.status()!=3)) continue;
        if (abs(g.pdgId())!=11 and abs(g.pdgId())!=13) continue;
        tmpvec.SetPtEtaPhiE(g.pt(),g.eta(),g.phi(),g.energy());
        int pid = abs(g.pdgId());
        bool match = false;
        if (pid==11) {
            elden3->Fill(g.pt());
            eletaden3->Fill(g.eta());
            for (unsigned int i=0; i<rev.size(); i++) {
                if (tmpvec.DeltaR(rev[i])<0.3 && fabs((g.pt()-rev[i].Pt())/g.pt()) < 0.5 ) {
                    match=true;
                    break;
                }
            }
            if (match) {
                elnum3->Fill(g.pt());
                eletanum3->Fill(g.eta());
            }
        }
        if (pid==13) {
            muden3->Fill(g.pt());
            muetaden3->Fill(g.eta());
            for (unsigned int i=0; i<rmv.size(); i++) {
                if (tmpvec.DeltaR(rmv[i])<0.3 && fabs((g.pt()-rmv[i].Pt())/g.pt()) < 0.5 ) {
                    match=true;
                    break;
                }
            }
            if (match) {
                munum3->Fill(g.pt());
                muetanum3->Fill(g.eta());
            }
        }
    }

}

//define this as a plug-in
DEFINE_FWK_MODULE(RECOAnalyzer);
