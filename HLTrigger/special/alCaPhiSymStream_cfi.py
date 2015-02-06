import FWCore.ParameterSet.Config as cms

alCaPhiSymStream = cms.EDFilter('HLTEcalPhiSymFilter',
  barrelDigiCollection = cms.InputTag('ecalDigis', 'ebDigis'),
  endcapDigiCollection = cms.InputTag('ecalDigis', 'eeDigis'),
  barrelUncalibHitCollection = cms.InputTag('ecalUncalibHit', 'EcalUncalibRecHitsEB'),
  endcapUncalibHitCollection = cms.InputTag('ecalUncalibHit', 'EcalUncalibRecHitsEE'),
  barrelHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  endcapHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  statusThreshold = cms.uint32(3),
  useRecoFlag = cms.bool(False),
  ampCut_barrel = cms.double(8),
  ampCut_endcap = cms.double(12),
  phiSymBarrelDigiCollection = cms.string('phiSymEcalDigisEB'),
  phiSymEndcapDigiCollection = cms.string('phiSymEcalDigisEE')
)
