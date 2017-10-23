TOP := $(shell cd ..; pwd)

include $(TOP)/build/dsc.version

OUTPUT_DIR := $(TOP)/output
STAGING_DIR := $(OUTPUT_DIR)/staging
INTERMEDIATE_DIR := $(OUTPUT_DIR)/intermediate
RELEASE_DIR := $(OUTPUT_DIR)/release

IB_DIR := $(shell cd ../../pal/installer/InstallBuilder; pwd)
UNAME_P := $(shell uname -p)
ifeq ($(UNAME_P),x86_64)
 PF_ARCH := x64
else
 PF_ARCH := x86
endif
CONFIG_VERSION := 1.1.1

ifeq ($(BUILD_OMS_VAL),1)
SHORT_NAME=omsconfig
LONG_NAME=Operations Management Suite Agent Configuration
PROVIDES=dscpkg
DESCRIPTION=Operations Management Suite Agent Configuration
RUN_AS_USER=omsagent
else
SHORT_NAME=dsc
LONG_NAME=Windows Powershell Desired State Configuration for Linux
PROVIDES=dscpackage
DESCRIPTION=Windows Powershell Desired State Configuration for Linux
RUN_AS_USER=root
endif

SHORT_NAME_DSC=dsc

ifeq ($(BUILD_OMS),BUILD_OMS)
PROVIDERS:=nxOMSPerfCounter
PROVIDERS+=nxOMSSyslog
PROVIDERS+=nxOMSCustomLog
PROVIDERS+=nxOMSSudoCustomLog
PROVIDERS+=nxOMSGenerateInventoryMof
PROVIDERS+=nxService
PROVIDERS+=nxPackage
PROVIDERS+=nxUser
PROVIDERS+=nxGroup
PROVIDERS+=nxOMSPlugin
PROVIDERS+=nxAvailableUpdates
PROVIDERS+=nxOMSKeyMgmt
PROVIDERS+=nxFileInventory
PROVIDERS+=nxOMSAutomationWorker
PROVIDERS+=nxOMSAgentNPMConfig
PROVIDERS+=nxOMSAuditdPlugin
PROVIDERS+=nxOMSContainers
else
PROVIDERS:=nxUser
PROVIDERS+=nxGroup
PROVIDERS+=nxService
PROVIDERS+=nxPackage
PROVIDERS+=nxIPAddress
PROVIDERS+=nxComputer
PROVIDERS+=nxFirewall
PROVIDERS+=nxDNSServerAddress
PROVIDERS+=nxMySqlDatabase
PROVIDERS+=nxMySqlGrant
PROVIDERS+=nxMySqlUser
PROVIDERS+=nxAvailableUpdates
PROVIDERS+=nxFileInventory
PROVIDERS+=nxOMSAutomationWorker
endif

#List of Providers for DSC that are not in OMS
DSCPROVIDERS:=nxScript
DSCPROVIDERS+=nxFile
DSCPROVIDERS+=nxFileLine
DSCPROVIDERS+=nxArchive
DSCPROVIDERS+=nxEnvironment
DSCPROVIDERS+=nxSshAuthorizedKeys

ifeq ("$(wildcard /usr/bin/dpkg-deb)","")
DPKG_LOCATION="--DPKG_LOCATION=$(IB_DIR)/tools/bin/dpkg-deb-$(PF_ARCH)"
else
DPKG_LOCATION=
endif

all:
ifeq ($(BUILD_RPM),1)
	@echo "========================= Make DSC installer"
	sudo rm -rf $(STAGING_DIR) $(INTERMEDIATE_DIR) 
	mkdir -p $(RELEASE_DIR) $(STAGING_DIR) $(INTERMEDIATE_DIR)
	python $(IB_DIR)/installbuilder.py \
		--BASE_DIR=$(TOP) \
		--TARGET_DIR=$(RELEASE_DIR) \
		--INTERMEDIATE_DIR=$(INTERMEDIATE_DIR) \
		--STAGING_DIR=$(STAGING_DIR) \
		--PACKAGE_TYPE=RPM \
		--PF=Linux \
		--PFMAJOR=1 \
		--PFMINOR=0 \
		--PFARCH=$(PF_ARCH) \
		--PFDISTRO=ULINUX \
		--VERSION=$(CONFIG_VERSION) \
		--RELEASE=$(DSC_BUILDVERSION_BUILDNR) \
		--BUILD_OMS=$(BUILD_OMS_VAL) \
		--SHORT_NAME=$(SHORT_NAME) \
		--SHORT_NAME_DSC=$(SHORT_NAME_DSC) \
		--LONG_NAME="$(LONG_NAME)" \
		--PROVIDES=$(PROVIDES) \
		--PROVIDERS="$(PROVIDERS)" \
		--DSCPROVIDERS="$(DSCPROVIDERS)" \
		--DESCRIPTION="$(DESCRIPTION)" \
                --RUN_AS_USER="$(RUN_AS_USER)" \
		--OUTPUTFILE=$(SHORT_NAME)-$(CONFIG_VERSION)-$(DSC_BUILDVERSION_BUILDNR).ssl_$(SSL_VERSION).$(PF_ARCH) \
		--DATAFILE_PATH=$(TOP)/installbuilder/datafiles \
		Base_DSC.data
endif

ifeq ($(BUILD_DPKG),1)
	@echo "========================= Make DSC installer"
ifeq ($(BUILD_OMS_VAL),1)
	egrep -q "^omsagent:" /etc/passwd; if [ $$? -ne 0 ]; then echo "Creating omsagent user ..."; sudo /usr/sbin/useradd -r -c "OMS agent" -d /var/opt/microsoft/omsagent/run -s /bin/bash omsagent; fi
endif
	sudo rm -rf $(STAGING_DIR) $(INTERMEDIATE_DIR) 
	mkdir -p $(RELEASE_DIR) $(STAGING_DIR) $(INTERMEDIATE_DIR)
	python $(IB_DIR)/installbuilder.py \
		--BASE_DIR=$(TOP) \
		--TARGET_DIR=$(RELEASE_DIR) \
		--INTERMEDIATE_DIR=$(INTERMEDIATE_DIR) \
		--STAGING_DIR=$(STAGING_DIR) \
		--PACKAGE_TYPE=DPKG \
		--PF=Linux \
		--PFMAJOR=1 \
		--PFMINOR=0 \
		--PFARCH=$(PF_ARCH) \
		--PFDISTRO=ULINUX \
		--VERSION=$(CONFIG_VERSION) \
		--RELEASE=$(DSC_BUILDVERSION_BUILDNR) \
		--BUILD_OMS=$(BUILD_OMS_VAL) \
		--SHORT_NAME=$(SHORT_NAME) \
		--SHORT_NAME_DSC=$(SHORT_NAME_DSC) \
		--LONG_NAME="$(LONG_NAME)" \
		--PROVIDES=$(PROVIDES) \
		--PROVIDERS="$(PROVIDERS)" \
		--DSCPROVIDERS="$(DSCPROVIDERS)" \
		--DESCRIPTION="$(DESCRIPTION)" \
                --RUN_AS_USER="$(RUN_AS_USER)" \
		--OUTPUTFILE=$(SHORT_NAME)-$(CONFIG_VERSION)-$(DSC_BUILDVERSION_BUILDNR).ssl_$(SSL_VERSION).$(PF_ARCH) \
		$(DPKG_LOCATION) \
		--DATAFILE_PATH=$(TOP)/installbuilder/datafiles \
		Base_DSC.data
endif
